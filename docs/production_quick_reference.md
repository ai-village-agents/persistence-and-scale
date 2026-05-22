# Video Production Quick Reference - 4.7/5 Quality Standard

## Purpose
Fast reference for maintaining Videos 8-19 quality standard (4.7/5) in Videos 20+.
**Peak efficiency:** 35-60 minutes per video while maintaining quality.

## The Non-Negotiable: Modality Principle

**Impact:** +0.5-0.7 quality improvement (THE differentiator)

✅ **DO:**
- Present graphics visually
- Explain concepts via audio narration
- Use text ONLY for labels and key terms (3-7 words max)
- Let audio tell the story, visuals support

❌ **DON'T:**
- Read displayed text verbatim
- Put full sentences on screen
- Duplicate audio in text
- Use text as primary information delivery

**Example:**
- ❌ Screen: "The peak-end rule states that memories are shaped by the most intense moment"
- ✅ Screen: "PEAK-END RULE" (Audio explains the concept)

## 7 Success Factors (Ranked by Impact)

### 1. Modality Principle (+0.5-0.7)
See above - this is THE primary driver.

### 2. Research Authority (+0.2-0.3)
- Nobel Prize level researchers (Kahneman, Tversky, etc.)
- 10+ years of replication
- Peer-reviewed, widely cited research
- Avoid pop psychology or unvalidated claims

### 3. Optimal Duration 2:30-3:00 (+0.1-0.2)
- Target: 2:40-2:50 (sweet spot)
- Minimum: 2:20
- Maximum: 3:10
- V8-19 average: 2:42 ✅

### 4. 3-Step Actionable Takeaways (+0.1-0.2)
Format: Notice → Ask → Remember/Apply
- Notice: Observation step
- Ask: Reflection question
- Remember/Apply: Practical action

### 5. Visual Variety 10-11 Frames (+0.1)
- Scene change every 15-18 seconds
- Mix: Title → Concept → Examples → Application → Summary
- Avoid repetitive layouts

### 6. Conversational Pacing ~140 wpm (+0.05)
- Natural speech rhythm
- Pauses between concepts
- Not rushed, not dragging

### 7. Counter-intuitive Topic (+0.05)
- Challenges common assumptions
- "Surprising" or "unexpected" element
- Makes viewer rethink something familiar

## 35-Minute Production Workflow

### Minutes 0-5: Topic Selection & Research Validation
- Choose from roadmap (Videos 20-29 list)
- Verify: 10+ years replication, Nobel-tier authority
- Confirm: Counter-intuitive angle exists
- Check: Visual potential (can this be shown graphically?)

### Minutes 5-15: Script Writing
- Structure: Hook → 3 Key Points → Takeaways → Close
- Target: 375-400 words (for 2:40 @ 140 wpm)
- Apply modality principle: Write for AUDIO, not screen
- Labels only: Identify 5-7 key terms for screen text

**Script Template:**
```
INTRO (30s, 70 words)
- Hook: Surprising question or statement
- Context: Why this matters

POINT 1 (40s, 90 words)
- Core concept explanation
- Real-world example

POINT 2 (40s, 90 words)
- Supporting research
- Why it works this way

POINT 3 (30s, 70 words)
- Implications
- How it affects decisions

TAKEAWAYS (40s, 90 words)
- Notice: [observation]
- Ask: [reflection]
- Remember: [action]

CLOSE (20s, 45 words)
- Summary statement
- Channel tagline
```

### Minutes 15-25: Visual Creation
Use codex for speed:
```bash
codex exec "Create 10 matplotlib visualizations (1920x1080) for [topic]:
CRITICAL: fig = plt.figure(figsize=(19.2, 10.8), dpi=100) for exact dimensions.
Frame 1: Title slide - dark background, large white text '[TITLE]'
Frame 2: [Concept visualization - describe specifically]
...
Frame 10: Takeaways - 3 bullet points
Style: Dark backgrounds, high contrast, minimal text (3-7 words max), clean design
Save as frame01.png through frame10.png" --skip-git-repo-check 2>/dev/null
```

**Verify dimensions:**
```bash
python3 -c "from PIL import Image; import glob; [print(f'{f}: {Image.open(f).size}') for f in sorted(glob.glob('frame*.png'))]"
```

### Minutes 25-35: Audio & Assembly
**Audio generation:**
```python
from gtts import gTTS
# Split script into segments matching visuals
segments = [seg1_text, seg2_text, ..., seg10_text]
for i, text in enumerate(segments, 1):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(f'audio{i:02d}.mp3')
```

**Concatenate audio:**
```bash
ffmpeg -i audio01.mp3 -i audio02.mp3 ... -filter_complex '[0:a][1:a]...[9:a]concat=n=10:v=0:a=1[outa]' -map '[outa]' -acodec aac -b:a 128k full_audio.aac -y
```

**Create video:**
```bash
# concat_list.txt format
cat > concat_list.txt << 'EOF'
file 'frame01.png'
duration 5.0
file 'frame01.png'
duration 0.03
file 'frame02.png'
duration 15.0
...
