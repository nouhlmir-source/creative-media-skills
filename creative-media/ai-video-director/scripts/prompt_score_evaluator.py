#!/usr/bin/env python3
"""prompt_score_evaluator.py - Score AI video prompts across 5 layers.

Usage:
  python prompt_score_evaluator.py "your prompt here"
  python prompt_score_evaluator.py prompts.json --format json
  python prompt_score_evaluator.py --demo
"""

import json, sys, argparse, os

SUBJECT = ["man","woman","person","figure","character","astronaut","soldier","child","robot","creature","wearing","young","old"]
ACTION  = ["walk","run","stand","sit","jump","fly","fall","turn","move","dance","fight","swim","slowly","quickly","floating"]
ENV     = ["forest","city","ocean","desert","mountain","street","room","space","dawn","dusk","night","sunset","fog","rain","snow","beach","field"]
CINEMA  = ["shot","angle","dolly","pan","tilt","zoom","tracking","handheld","wide","close","medium","aerial","pov","overhead","lens","bokeh"]
AESTH   = ["cinematic","film","35mm","16mm","grain","vintage","muted","warm","cool","desaturated","vibrant","neon","photorealistic","painterly","gritty"]
LIMITS  = {"runway":150,"pika":100,"kling":200,"sora":500,"default":200}

def score(prompt, platform="default", label=""):
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
    issues = []
    if s  == 0: issues.append("MISSING Subject: add who/what is in the shot")
    if a  == 0: issues.append("MISSING Action: add what is happening")
    if e  == 0: issues.append("MISSING Environment: add location and lighting")
    if c  == 0: issues.append("MISSING Cinematography: add shot size and camera move")
    if ae == 0: issues.append("WEAK Aesthetic: add film stock or style reference")
    if w > lim: issues.append(f"TOO LONG: {w} words > {lim} limit for {platform}")
    if w < 10:  issues.append("TOO SHORT: expand prompt with more detail")
    rating = "EXCELLENT" if total>=85 else "GOOD" if total>=70 else "FAIR" if total>=50 else "POOR"
    return {"label": label or "Prompt", "platform": platform, "word_count": w,
            "total_score": total, "rating": rating,
            "layers": {"subject":s,"action":a,"env":e,"cinema":c,"aesthetic":ae},
            "issues": issues}

def demo():
    return [
        score("A weathered fisherman pulls a heavy net from the stormy ocean at dawn. Medium wide shot, slow handheld push. Rocky coastline, overcast sky. Shot on 16mm film, muted blue-green tones.", "runway", "Strong prompt"),
        score("A person walking somewhere nice.", "runway", "Weak prompt"),
        score("Young woman in a red dress stands in a foggy forest at night. Mysterious and cinematic.", "pika", "Missing cinema"),
    ]

def report(results):
    print("="*60)
    print("AI VIDEO PROMPT SCORE")
    print("="*60)
    for r in results:
        print(f"\n{r['label']}  [{r['rating']}]  {r['total_score']}/100  ({r['word_count']} words)")
        ls = r["layers"]
        print(f"  S={ls['subject']} A={ls['action']} E={ls['env']} C={ls['cinema']} Ae={ls['aesthetic']}")
        for i in r["issues"]: print(f"  ! {i}")
    print("="*60)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", nargs="?")
    p.add_argument("--format", choices=["text","json"], default="text")
    p.add_argument("--platform", choices=list(LIMITS.keys()), default="default")
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    if args.demo or not args.input:
        results = demo()
    elif os.path.exists(args.input):
        with open(args.input) as f: data = json.load(f)
        results = [score(s["prompt"], s.get("platform", args.platform), s.get("label","")) for s in data.get("shots",[])]
    else:
        results = [score(args.input, args.platform)]
    print(json.dumps(results, indent=2)) if args.format=="json" else report(results)

if __name__ == "__main__":
    main()
