# Creative Media Skills

Claude Code skills for video editors, AI specialists, and directors.

## Skills in This Domain

### video-editor-pro
Expert post-production advisor for cut strategy, color grading, and delivery.
- Supports DaVinci Resolve, Premiere Pro, Final Cut, Avid
- - Python tool: edit_pace_analyzer.py
  - - Activate: Using the video-editor-pro skill, [question]
   
    - ### ai-video-director
    - AI video generation and direction specialist.
    - - Platform selection, prompt planning, AI + live footage hybrid
      - - Supports RunwayML, Sora, Pika, Kling, Stable Video
        - - Python tool: prompt_score_evaluator.py
          - - Activate: Using the ai-video-director skill, [question]
           
            - ### video-prompt-engineer
            - Specialist in writing, diagnosing, and optimizing AI video prompts.
            - - Write, fix, and A/B test prompts for any text-to-video platform
              - - Python tools: prompt_score_evaluator.py, prompt_ab_comparator.py
                - - Activate: Using the video-prompt-engineer skill, [question]
                 
                  - ## Skill Selection Guide
                 
                  - | Task | Skill |
                  - |---|---|
                  - | Editing timeline in Resolve/Premiere | video-editor-pro |
                  - | Delivery specs for YouTube, TikTok, broadcast | video-editor-pro |
                  - | Color grading workflow | video-editor-pro |
                  - | Generating AI video shots | ai-video-director |
                  - | Choosing AI platform | ai-video-director |
                  - | Integrating AI with live footage | ai-video-director |
                  - | Writing prompt for RunwayML/Pika/Kling | video-prompt-engineer |
                  - | Fixing bad AI video output | video-prompt-engineer |
                  - | A/B testing prompt variants | video-prompt-engineer |
                 
                  - ## Python Tools (zero dependencies)
                 
                  - python creative-media/video-editor-pro/scripts/edit_pace_analyzer.py --demo
                  - python creative-media/ai-video-director/scripts/prompt_score_evaluator.py --demo
                  - python creative-media/video-prompt-engineer/scripts/prompt_ab_comparator.py --demo
                 
                  - ## Installation
                 
                  - Claude Code: cp -r creative-media/ ~/.claude/skills/
                  - Any agent: Copy skill folder to your agent skills directory
                 
                  - Version: 1.0.0 | April 2026
