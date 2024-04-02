import gtts

my_text = "i am majid karimi a human"

x = gtts.gTTS(my_text, lang="en", slow= False)

x.save("voice.mp3")
