#!/usr/bin/env python3
"""prompt_ab_comparator.py - Compare two AI video prompts A vs B.

Usage:
  python prompt_ab_comparator.py prompts_ab.json
    python prompt_ab_comparator.py prompts_ab.json --format json
      python prompt_ab_comparator.py --demo
      """

import json, sys, argparse, os

SUBJECT = ["man","woman","person","figure","character","astronaut","child","robot","creature"]
ACTION  = ["walk","run","stand","sit","jump","fly","fall","turn","move","dance","slowly","quickly"]
ENV     = ["forest","city","ocean","desert","mountain","street","room","space","dawn","night","fog"]
CINEMA  = ["shot","angle","dolly","pan","tilt","zoom","tracking","handheld","wide","close","medium"]
AESTH   = ["cinematic","film","35mm","16mm","grain","vintage","muted","warm","cool","desaturated"]
LIMITS  = {"runway":150,"pika":100,"kling":200,"sora":500,"default":200}

def score(prompt, platform="default"):
      p = prompt.lower()
      w = len(prompt.split())
      lim = LIMITS.get(platform, 200)
      s  = min(20, sum(1 for x in SUBJECT if x in p) * 7)
      a  = min(20, sum(1 for x in ACTION  if x in p) * 6)
      e  = min(20, sum(1 for x in ENV     if x in p) * 6)
      c  = min(20, sum(1 for x in CINEMA  if x in p) * 5)
      ae = min(20, sum(1 for x in AESTH   if x in p) * 6)
      total = s + a + e + c + ae
      if w > lim: total = max(0, total - min(15, (w - lim)//10*3))
            return {"score": total, "words": w, "layers": {"subject":s,"action":a,"env":e,"cinema":c,"aesthetic":ae}}

def compare_pair(pair, platform):
      a = score(pair["a"], platform)
    b = score(pair["b"], platform)
    winner = "A" if a["score"] > b["score"] else "B" if b["score"] > a["score"] else "TIE"
    diff = abs(a["score"] - b["score"])
    adv_a = [k for k in a["layers"] if a["layers"][k] > b["layers"][k]]
    adv_b = [k for k in b["layers"] if b["layers"][k] > a["layers"][k]]
    return {"label": pair.get("label","Shot"), "platform": platform,
                        "a": {"score":a["score"],"words":a["words"]}, "b": {"score":b["score"],"words":b["words"]},
                        "winner": winner, "diff": diff, "advantages_a": adv_a, "advantages_b": adv_b,
                        "recommendation": f"Use Prompt {winner}" if winner!="TIE" else "Test both outputs"}

def demo():
      return {"platform":"runway","pairs":[
          {"label":"Opening shot",
                    "a":"A person walks in a city at night.",
                    "b":"A lone detective walks down a rain-soaked city street at night. Medium wide shot, slow tracking. Neon reflections. Shot on 35mm, teal and orange grade."},
          {"label":"Character reveal",
                    "a":"Young woman stands in forest. Mysterious and cinematic.",
                    "b":"A young woman in a white dress stands at the edge of a misty forest at dawn. Static medium shot, shallow depth. Film grain, warm palette."}
]}

def print_report(results):
      print("="*60)
    print("A/B PROMPT COMPARISON")
    print("="*60)
    for r in results:
              print(f"\n{r['label']}  [{r['platform']}]")
              print(f"  A: {r['a']['score']}/100  ({r['a']['words']} words)")
              print(f"  B: {r['b']['score']}/100  ({r['b']['words']} words)")
              print(f"  WINNER: {r['winner']}  (diff: {r['diff']})")
              print(f"  {r['recommendation']}")

def main():
      p = argparse.ArgumentParser()
    p.add_argument("input", nargs="?")
    p.add_argument("--format", choices=["text","json"], default="text")
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    if args.demo or not args.input:
              data = demo()
elif os.path.exists(args.input):
        with open(args.input) as f: data = json.load(f)
else:
        print("Error: file not found", file=sys.stderr); sys.exit(1)
      results = [compare_pair(pair, data.get("platform","default")) for pair in data.get("pairs",[])]
    print(json.dumps(results,indent=2)) if args.format=="json" else print_report(results)

if __name__ == "__main__":
      main()
