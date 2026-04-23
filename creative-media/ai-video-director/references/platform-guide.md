# AI Video Platform Guide

## Platform Comparison

| Platform | Quality | Speed | Cost | Lip Sync | Max Duration |
|---|---|---|---|---|---|
| RunwayML Gen-3 | Best | Medium | High | No | 10s |
| Sora | Excellent | Slow | TBD | No | 60s |
| Pika 2.0 | Good | Fast | Low | No | 10s |
| Kling | Good | Medium | Low | Yes | 5min |
| Luma Dream Machine | Good | Fast | Low | No | 5s |
| Stable Video | Variable | Fast (local) | Free | No | Custom |

## RunwayML Gen-3

Best for: Cinematic motion, character consistency, branded content
Max duration: 10 seconds per clip
Resolution: Up to 1280x768

Prompting tips:
- Always include camera movement (dolly, pan, tracking, handheld)
- - Specify shot size (wide, medium, close-up)
  - - Keep prompts under 150 words
    - - Use cinematic references: "Deakins-style cinematography"
      - - Add motion speed: slow motion, real-time, time-lapse
       
        - ## Pika 2.0
       
        - Best for: Fast iteration, social media, quick prototypes
        - Max duration: 10 seconds
       
        - Prompting tips:
        - - Shorter is better: 20-60 words ideal
          - - Keyword-heavy prompts work well
            - - Use --ar flag for aspect ratio (16:9, 9:16, 1:1)
             
              - ## Kling AI
             
              - Best for: Fluid motion, lip sync, longer clips
              - Max duration: Up to 5 minutes via extension
             
              - Prompting tips:
              - - Strong response to action verbs
                - - Best platform for lip sync — add "natural mouth movement, speaking clearly"
                  - - Good at facial expressions — specify them explicitly
                   
                    - ## Sora
                   
                    - Best for: Complex scenes, long-form narratives, physics simulation
                    - Max duration: Up to 60 seconds
                   
                    - Prompting tips:
                    - - Works well with narrative descriptive language
                      - - Can handle multi-event prompts
                        - - Longer prompts work better than other platforms
                         
                          - ## AI Integration Workflow
                         
                          - Step 1 - Pre-production:
                          - 1. Create shot list with AI candidates marked
                            2. 2. Write prompt templates for consistent look
                               3. 3. Choose platform based on shot requirements
                                 
                                  4. Step 2 - Generation:
                                  5. 1. Test prompts on 1-2 representative shots first
                                     2. 2. Generate 3-5 variations per shot
                                        3. 3. Note successful prompt patterns
                                          
                                           4. Step 3 - Post-production:
                                           5. 1. Convert AI output to project color space
                                              2. 2. Match grain/noise to live footage
                                                 3. 3. Conform frame rate
                                                    4. 4. Apply consistent LUT across all AI shots
                                                       5. 5. QC for AI artifacts (flickering, morphing edges)
                                                         
                                                          6. Last updated: April 2026
