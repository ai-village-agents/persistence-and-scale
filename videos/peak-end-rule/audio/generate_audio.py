from gtts import gTTS
import os

# Frame 2: Hook (15 seconds)
text_02 = """Think about your best vacation. You probably remember it as amazing. But if you could replay every moment, you'd find hours of boredom, discomfort, travel stress. So why does memory feel so different from reality?"""
tts_02 = gTTS(text=text_02, lang='en', slow=False)
tts_02.save('frame02_narration.mp3')
print("✅ Frame 2 audio generated")

# Frame 3: The Rule (20 seconds)
text_03 = """Here's the answer: Your memory doesn't average your experiences. It shortcuts. It takes the most intense moment—the peak—and the final moment—the end—and judges the entire experience by just those two data points. Everything else fades."""
tts_03 = gTTS(text=text_03, lang='en', slow=False)
tts_03.save('frame03_narration.mp3')
print("✅ Frame 3 audio generated")

# Frame 4: The Research (25 seconds)
text_04 = """Daniel Kahneman proved this with colonoscopy patients. Group A had a shorter, more painful procedure. Group B had the same pain, but doctors added extra time at the end with low discomfort. Group B remembered the experience as less painful, even though they suffered longer. The ending changed the memory."""
tts_04 = gTTS(text=text_04, lang='en', slow=False)
tts_04.save('frame04_narration.mp3')
print("✅ Frame 4 audio generated")

# Frame 5: Why It Happens (20 seconds)
text_05 = """Your brain evolved to remember lessons, not archives. The peak tells you what's important. The end tells you the outcome. Those are the parts that help you decide whether to repeat the experience. The middle? It doesn't help predictions, so your brain discards it."""
tts_05 = gTTS(text=text_05, lang='en', slow=False)
tts_05.save('frame05_narration.mp3')
print("✅ Frame 5 audio generated")

# Frame 6: Movies Example (20 seconds)
text_06 = """Think about movies. A film can drag for an hour, but if the final act is brilliant, you walk out calling it great. The ending rewrites your memory of everything before it. That's the peak-end rule in action."""
tts_06 = gTTS(text=text_06, lang='en', slow=False)
tts_06.save('frame06_narration.mp3')
print("✅ Frame 6 audio generated")

# Frame 7: Relationships Example (20 seconds)
text_07 = """Or relationships. Years of daily mundane moments matter less to memory than a handful of peak experiences—an amazing trip, a crisis handled together—and how it ended. Breakups rewrite entire histories. Endings have disproportionate power."""
tts_07 = gTTS(text=text_07, lang='en', slow=False)
tts_07.save('frame07_narration.mp3')
print("✅ Frame 7 audio generated")

# Frame 8: The Design Implication (25 seconds)
text_08 = """Once you know this, you can design experiences differently. Don't aim for consistent mediocrity. Create memorable peaks—moments of surprise, delight, intensity. And end strong. The last five minutes shape memory more than the first fifty-five."""
tts_08 = gTTS(text=text_08, lang='en', slow=False)
tts_08.save('frame08_narration.mp3')
print("✅ Frame 8 audio generated")

# Frame 9: Takeaway (25 seconds)
text_09 = """Three ways to use the peak-end rule. One: Notice when your memory diverges from reality. What peaks stand out? Two: Deliberately design peak moments and strong endings into experiences you create. Three: Apply everywhere—end meetings with wins, end dates with highlights, end projects with celebration."""
tts_09 = gTTS(text=text_09, lang='en', slow=False)
tts_09.save('frame09_narration.mp3')
print("✅ Frame 9 audio generated")

# Frame 10: Closing (5 seconds)
text_10 = """Memory is not a recording. It's a story."""
tts_10 = gTTS(text=text_10, lang='en', slow=False)
tts_10.save('frame10_narration.mp3')
print("✅ Frame 10 audio generated")

print("\n✅ All audio narration files generated for Video 11!")
