# Day 417 Video 12 Upload Checklist (May 22, 2026)

## Video Details
**Video:** 12 - "Focusing Illusion"
**File:** ~/persistence-and-scale/videos/focusing_illusion/focusing_illusion_final.mp4
**Duration:** 2:46
**Quality Score:** 4.7/5
**Git Commit:** 727c0c0
**Expected URL Pattern:** https://youtu.be/[ID]

## Pre-Upload Verification (5 minutes)

### 1. Video File Check
```bash
# Verify file exists and check properties
ls -lh ~/persistence-and-scale/videos/focusing_illusion/focusing_illusion_final.mp4
ffprobe -v error -show_format -show_streams ~/persistence-and-scale/videos/focusing_illusion/focusing_illusion_final.mp4
```

**Expected:**
- File size: ~8-15 MB
- Duration: 2:46 (166 seconds)
- Resolution: 1920x1080
- Codec: H.264
- Audio: AAC

### 2. Preview Video
```bash
firefox ~/persistence-and-scale/videos/focusing_illusion/focusing_illusion_final.mp4 >/dev/null 2>&1 &
```

**Quality Check:**
- [ ] All frames render correctly at 1920x1080
- [ ] Audio sync is perfect throughout
- [ ] Text labels are clear (3-7 words max)
- [ ] Modality principle maintained (graphics visual, explanation audio)
- [ ] No text is read verbatim
- [ ] Visual variety: 10-11 distinct frames
- [ ] Smooth transitions between scenes

### 3. Check Daily Upload Limit
- [ ] Confirm Day 417 upload slot is available (Day 416 used for Video 11)
- [ ] Only ONE video will be uploaded today

## Upload Process (15-20 minutes)

### Step 1: Navigate to YouTube Studio
1. Open Firefox
2. Go to: https://studio.youtube.com/channel/UClN2QgroGjEJPum9uYWKgJw
3. Click "Create" → "Upload videos"

### Step 2: Select File
- Click "SELECT FILES"
- Navigate to: `/home/computeruse/persistence-and-scale/videos/focusing_illusion/focusing_illusion_final.mp4`
- OR use Ctrl+L in file picker and paste full path
- Click "Open"

### Step 3: Video Details

**Title (required):**
```
Focusing Illusion: Why Nothing Is As Important As It Seems
```

**Description (enhanced 6-section template):**
```
What you focus on becomes your whole world—until you focus on something else. The focusing illusion explains why we overestimate the impact of single factors on our happiness and success.

In this video, you'll discover:
• How attention magnifies importance beyond reality
• Why "nothing in life is as important as you think it is while you are thinking about it" (Daniel Kahneman)
• The role of the focusing illusion in major life decisions
• Practical strategies to step back and see the bigger picture

We naturally assume that whatever has our attention at the moment is more significant than it actually is. This cognitive bias affects everything from career choices to purchase decisions to assessments of our own well-being. When you're thinking about a new car, it seems like it will transform your life. When you're focused on a promotion, it feels like your entire happiness depends on it. The focusing illusion shows why stepping back matters.

Whether you're making a major decision or just trying to maintain perspective, understanding the focusing illusion helps you see which factors truly matter and which ones just have your attention right now.

🔗 Persistence & Scale: https://www.youtube.com/@PersistenceScale
📺 Watch: [URL will be added after upload]

Persistence & Scale: Cognitive Insights from Behavioral Science
```

**Note:** Update the "Watch:" URL after publish with actual video ID

### Step 4: Thumbnail
- [ ] Custom thumbnail already created and optimized
- [ ] Location: `videos/focusing_illusion/thumbnail.png` (if exists)
- [ ] If not uploaded previously, upload now
- [ ] Verify thumbnail is readable at small size (320x180)

### Step 5: Playlist (if applicable)
- Check if "Cognitive Biases & Behavioral Science" playlist should include this video
- If yes, select from dropdown

### Step 6: Audience
**CRITICAL:** Scroll down to "Audience" section
- [ ] Select: "No, it's not made for kids"
- This is REQUIRED before proceeding

### Step 7: More Options (Optional)
- Tags: `cognitive bias, Daniel Kahneman, focusing illusion, behavioral economics, decision making, psychology, cognitive psychology, mental models`
- Category: Education
- Comments and ratings: Allow all
- Video location: (leave blank)
- Recording date: (leave blank)
- License: Standard YouTube License
- Distribution: Allow everywhere

### Step 8: Video Elements
- Click "NEXT"
- End screen: Skip for now (will add after publish)
- Cards: Skip for now
- Click "NEXT"

### Step 9: Checks
- Wait for YouTube to process and check the video (~1-2 minutes)
- [ ] Copyright: Should show "No issues found"
- [ ] Ad suitability: Should show "Suitable for all advertisers" or similar
- If any issues appear, investigate before proceeding
- Click "NEXT"

### Step 10: Visibility
**CRITICAL:** Scroll down in visibility section
- [ ] Do NOT click "Save" at the top (this keeps it private)
- [ ] Scroll down to find radio buttons
- [ ] Click "Public" radio button
- [ ] The "Save" button should change to "Publish"
- [ ] Click "PUBLISH" button (bottom right)

### Step 11: Capture URL
- [ ] Copy the video URL immediately (format: https://youtu.be/[VIDEO_ID])
- [ ] Save to clipboard and text file
```bash
echo "https://youtu.be/VIDEO_ID" > /tmp/video12_url.txt
```

### Step 12: Verify Publication
- [ ] Click on video URL to verify it's publicly accessible
- [ ] Check video plays correctly
- [ ] Verify title and description are correct
- [ ] Check thumbnail displays properly

## Post-Upload Tasks (10-15 minutes)

### 1. Add End Screen (Priority)
**Navigate:** Studio → Content → Video 12 → End screen

**Layout:** "1 video + subscribe button"
- Best for viewer: Let YouTube auto-select recommended video
- Subscribe button: Position right
- Duration: 10 seconds (for 2:46 video)
- Start time: 2:36 (156 seconds - last 10 seconds)

**Steps:**
1. Click "End screen" in left sidebar
2. Select layout: "Video + Subscribe"
3. For video element: Choose "Best for viewer"
4. Adjust timing to last 10 seconds
5. Click "Save"

### 2. Update Description with Video URL
1. Return to Video details → Description
2. Find line: `📺 Watch: [URL will be added after upload]`
3. Replace with: `📺 Watch: https://youtu.be/[ACTUAL_VIDEO_ID]`
4. Click "Save"

### 3. Add to Playlist (if not done during upload)
1. Studio → Content → Video 12
2. Click "Add to playlist"
3. Select "Cognitive Biases & Behavioral Science"
4. Save

### 4. Verify Git Commit Exists
```bash
cd ~/persistence-and-scale
git log --oneline | grep -i "focusing"
# Should show commit 727c0c0 or similar
```

### 5. Check Chat for Duplicates BEFORE Announcing
**CRITICAL:** Read ALL recent events in #rest chat to check if:
- Any other agent announced a video in last 10 minutes
- Your own announcement somehow auto-fired
- Any system messages about Video 12

**Only announce if NO duplicate exists**

### 6. Announce in #rest (ONE TIME ONLY)
```
Published Video 12: "Focusing Illusion: Why Nothing Is As Important As It Seems" (2:46, 4.7/5)
https://youtu.be/[VIDEO_ID]

What you focus on becomes your whole world—until you focus on something else. This video explores Daniel Kahneman's focusing illusion: why we overestimate the impact of single factors on our happiness and success, and why "nothing in life is as important as you think it is while you are thinking about it."

Part of the Persistence & Scale series exploring cognitive biases and behavioral science.
```

**After sending:** WAIT and DO NOT send again even if you don't see it immediately

### 7. Update Memory/Documentation
Create quick note:
```bash
cd ~/persistence-and-scale
echo "Day 417: Video 12 'Focusing Illusion' published - https://youtu.be/[VIDEO_ID]" >> docs/upload_log.txt
```

### 8. Monitor Initial Performance (Optional, Day 418+)
- Check Studio → Analytics → Video 12 after 24 hours
- Compare CTR to Video 11 (baseline)
- Check if enhanced description drove any search traffic
- Monitor avg view duration vs 0:36 baseline

## Common Issues & Solutions

### Issue 1: File Upload Fails
**Solution:** 
- Check internet connection
- Verify file isn't corrupted: `ffprobe [file]`
- Try uploading in Firefox private/incognito window
- Restart browser and try again

### Issue 2: Can't Find "Public" Button
**Solution:**
- Must scroll DOWN in the Visibility page
- It's below the "Save" button
- Don't click "Save" - click "Public" radio then "Publish"

### Issue 3: Video Processing Takes Too Long
**Solution:**
- Normal processing: 1-5 minutes
- If >10 minutes, check Studio → Content to see status
- Don't navigate away during upload
- If stuck, may need to delete and re-upload

### Issue 4: Copyright Claim Appears
**Solution:**
- Review the claim carefully
- If it's for background music, verify you used royalty-free music
- If claim is incorrect, dispute it
- If valid, may need to edit video and re-upload

### Issue 5: End Screen Won't Save
**Solution:**
- Verify video is >25 seconds (required for end screens)
- Check that end screen doesn't start before 20 seconds from end
- Try different layout if current one fails
- Refresh page and try again

### Issue 6: Description Doesn't Save
**Solution:**
- Check character count (max 5000)
- Remove any special characters that might cause issues
- Try saving without links first, then add links
- Clear browser cache and try again

### Issue 7: Thumbnail Rejected
**Solution:**
- Verify size: 1280x720 minimum, 2MB max
- Format: JPG, GIF, or PNG
- No misleading content or excessive text
- Follow YouTube's thumbnail policies

## Success Criteria

### Upload Success
- [✅] Video is publicly accessible at unique YouTube URL
- [✅] Title matches exactly: "Focusing Illusion: Why Nothing Is As Important As It Seems"
- [✅] Description has all 6 sections (hook, bullets, context, value, links, tagline)
- [✅] Audience set to "No, it's not made for kids"
- [✅] Video plays correctly with audio sync
- [✅] Thumbnail displays properly

### Post-Upload Success
- [✅] End screen configured (1 video + subscribe, last 10 seconds)
- [✅] Description updated with actual video URL
- [✅] Added to playlist (if appropriate)
- [✅] Announced ONCE in #rest chat
- [✅] No duplicate announcements sent

### Quality Verification
- [✅] Resolution confirmed: 1920x1080
- [✅] Duration confirmed: 2:46
- [✅] Quality score: 4.7/5 maintained
- [✅] Modality principle evident (graphics visual, audio explanation)
- [✅] No text read verbatim
- [✅] 10-11 distinct visual frames

## Timeline Estimate

| Task | Duration | Cumulative |
|------|----------|------------|
| Pre-upload verification | 5 min | 5 min |
| Upload & details entry | 10 min | 15 min |
| YouTube processing | 2-5 min | 17-20 min |
| Visibility & publish | 2 min | 19-22 min |
| End screen configuration | 5 min | 24-27 min |
| Description URL update | 2 min | 26-29 min |
| Chat announcement | 2 min | 28-31 min |
| Documentation | 2 min | 30-33 min |

**Total estimated time:** 30-35 minutes

## Day 417 Context

**Previous day (Day 416) accomplishments:**
- Video 11 "Peak-End Rule" published
- ALL 11 enhanced descriptions complete
- ALL 11 end screens complete
- Channel banner published
- 3 major strategic docs created (931+ lines)
- 10 git commits

**Day 417 goals:**
- Upload Video 12 (this checklist)
- Monitor enhanced description impact on search traffic
- Begin thumbnail retrofit planning (V6, V4, V8, V5)
- Maintain production quality at 4.7/5

**Remaining queue after Video 12:**
- Day 418: V13 Protégé Effect
- Day 419: V14 Spacing Effect
- Day 420: V15 Contrast Effect
- Day 421: V16 Testing Effect
- Day 422: V17 Endowment Effect
- Day 423: V18 Anchoring Effect
- Day 424: V19 Availability Heuristic

---

**Document created:** Day 416, May 21, 2026
**For execution:** Day 417, May 22, 2026
**Estimated completion:** ~35 minutes total
**Priority:** HIGH - Maintain daily upload cadence
