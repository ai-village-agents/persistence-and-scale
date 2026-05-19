from gtts import gTTS
import os

# Frame 2: Hook (15 seconds)
text_02 = """Look at this image. At first, you might see one thing. But once someone points out there's something else hidden here... you can never go back to not seeing it. That's the ratchet effect."""
tts_02 = gTTS(text=text_02, lang='en', slow=False)
tts_02.save('frame02_narration.mp3')
print("✅ Frame 2 audio generated")

# Frame 3: The Concept (20 seconds)
text_03 = """A ratchet is a mechanical device that only moves in one direction. Push it forward, and it clicks into place. Try to push it backward, and it locks. Knowledge works the same way. Once learned, it can't be unlearned. Your brain builds pathways that only go forward."""
tts_03 = gTTS(text=text_03, lang='en', slow=False)
tts_03.save('frame03_narration.mp3')
print("✅ Frame 3 audio generated")

# Frame 4: Example 1 - Reading (25 seconds)
text_04 = """Think about reading. When you first learned, you saw individual letters. C. A. T. But now? You can't look at those letters without seeing the word 'cat.' You can't turn off reading. The pathway is permanent. You've ratcheted forward, and there's no going back."""
tts_04 = gTTS(text=text_04, lang='en', slow=False)
tts_04.save('frame04_narration.mp3')
print("✅ Frame 4 audio generated")

# Frame 5: Example 2 - Concept Understanding (25 seconds)
text_05 = """Or consider compound interest. Before you understand it, numbers grow mysteriously. But once someone shows you the formula, once you see how each step builds on the last, you can never look at savings the same way. The ratchet has clicked forward."""
tts_05 = gTTS(text=text_05, lang='en', slow=False)
tts_05.save('frame05_narration.mp3')
print("✅ Frame 5 audio generated")

# Frame 6: Why It Happens (20 seconds)
text_06 = """This happens because learning physically changes your brain. Neural pathways form, strengthen, and become automatic. It's not about willpower or memory. It's structural. Your brain has literally reorganized itself around this new understanding."""
tts_06 = gTTS(text=text_06, lang='en', slow=False)
tts_06.save('frame06_narration.mp3')
print("✅ Frame 6 audio generated")

# Frame 7: Why It Matters (25 seconds)
text_07 = """Understanding the ratchet effect changes how you approach learning. You can't undo knowledge, so choose carefully what you expose yourself to. But more importantly, recognize that every small piece of learning is permanent progress. It compounds. It builds on itself. Forward only."""
tts_07 = gTTS(text=text_07, lang='en', slow=False)
tts_07.save('frame07_narration.mp3')
print("✅ Frame 7 audio generated")

# Frame 8: The Opportunity (20 seconds)
text_08 = """This is why consistency beats intensity. Each small learning session clicks the ratchet forward one notch. You might not notice it immediately, but you can't slip backward. Every session is a permanent step, even when it feels small."""
tts_08 = gTTS(text=text_08, lang='en', slow=False)
tts_08.save('frame08_narration.mp3')
print("✅ Frame 8 audio generated")

# Frame 9: Takeaway - 3 Steps (25 seconds)
text_09 = """Three steps to use the ratchet effect. One: Notice what you've already ratcheted forward on. What can you no longer unsee? Two: Choose deliberately what knowledge to make permanent. Three: Trust the process. Small consistent clicks forward compound into major progress."""
tts_09 = gTTS(text=text_09, lang='en', slow=False)
tts_09.save('frame09_narration.mp3')
print("✅ Frame 9 audio generated")

# Frame 10: Closing (5 seconds)
text_10 = """Progress you can't undo."""
tts_10 = gTTS(text=text_10, lang='en', slow=False)
tts_10.save('frame10_narration.mp3')
print("✅ Frame 10 audio generated")

print("\n✅ All audio narration files generated!")
