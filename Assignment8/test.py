import gtts
while True:
    x = input("enter text: ")
    # y = x.split(" ")
    z = gtts.gTTS(x, lang="en")
    n = "sdf.mp3"
    z.save(n)