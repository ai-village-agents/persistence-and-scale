from gtts import gTTS
import subprocess
import os

os.chdir('audio')

# Frame 1: 5 seconds of silence
subprocess.run(['ffmpeg', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', 
                '-t', '5', '-acodec', 'aac', '-b:a', '128k', 
                'frame01_silence.aac', '-y'], 
               capture_output=True)

# Frame 2
text2 = "In 1973, Amos Tversky and Daniel Kahneman asked people a simple question: In English, are there more words that start with the letter K, or more words that have K as their third letter?"
tts2 = gTTS(text=text2, lang='en', slow=False)
tts2.save('frame02.mp3')

# Frame 3
text3 = "Most people said words starting with K are more common. They're not. Words with K in the third position—like \"acknowledge\" or \"awkward\"—are roughly twice as frequent. But they're harder to recall."
tts3 = gTTS(text=text3, lang='en', slow=False)
tts3.save('frame03.mp3')

# Frame 4
text4 = "This is the availability heuristic. We judge how likely or common something is by how easily examples come to mind. The easier the recall, the more frequent or probable we assume it is. And usually, that works fine."
tts4 = gTTS(text=text4, lang='en', slow=False)
tts4.save('frame04.mp3')

# Frame 5
text5 = "But ease of recall isn't always correlated with actual frequency. Vivid events, recent experiences, and emotionally charged memories come to mind more readily—even when they're rare."
tts5 = gTTS(text=text5, lang='en', slow=False)
tts5.save('frame05.mp3')

# Frame 6
text6 = "After a plane crash makes headlines, people overestimate the danger of flying and avoid air travel. Yet statistically, driving becomes more dangerous during these periods as people shift to cars."
tts6 = gTTS(text=text6, lang='en', slow=False)
tts6.save('frame06.mp3')

# Frame 7
text7 = "Doctors overdiagnose conditions they've recently seen. Investors overweight recent market trends. Jurors overestimate the likelihood of dramatic testimony scenarios."
tts7 = gTTS(text=text7, lang='en', slow=False)
tts7.save('frame07.mp3')

# Frame 8
text8 = "The heuristic isn't a flaw—it's a feature that usually serves us well. But it systematically misfires when memory vividness and actual probability diverge."
tts8 = gTTS(text=text8, lang='en', slow=False)
tts8.save('frame08.mp3')

# Frame 9
text9 = "Tversky and Kahneman showed this isn't about intelligence or education. Even experts fall prey when working outside careful statistical analysis. The bias operates at the level of intuitive judgment."
tts9 = gTTS(text=text9, lang='en', slow=False)
tts9.save('frame09.mp3')

# Frame 10
text10 = "Three ways to notice the availability heuristic at work: One, when making probability judgments, ask what's actually making examples come to mind. Two, distinguish between \"I can easily recall examples\" and \"this is actually common.\" Three, when something feels obviously frequent, check if recent vivid exposure might be driving that feeling."
tts10 = gTTS(text=text10, lang='en', slow=False)
tts10.save('frame10.mp3')

print("Audio generation complete!")
