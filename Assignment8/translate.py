import gtts

def read_from_file():
    global word_bank
    f = open("translate.txt", "r")    

    temp = f.read().split("\n")

    word_bank = []
    for i in range(0, len(temp),2):
        my_dict = {"en":temp[i], "fa": temp[i+1]}
        word_bank.append(my_dict)    
    
    f.close()

def show_menu():
    print("welcome to my translator")
    print("1- translate english to persian")
    print("2- translate persian to english")
    print("3- add a new word")
    print("4- exit")


def translate_per_to_en():
    global user_text
    user_text = input("enter text: ")
    user_sentence = user_text.split(".")
    final_output = ""
    
    for i in range(len(user_sentence)):
    
        user_words = user_sentence[i].split(" ")

        output = ""
    
        for user_word in user_words:
            for word in word_bank:
                if user_word == word["fa"]:
                    output = output + word["en"] + " "
                    break
            else:
                output = output + user_word + " "

        print(output)
        final_output = final_output + output
        x = gtts.gTTS(final_output, lang="en")
        x.save("speech.mp3")

def translate_en_to_per():
    user_text = input("enter text: ")

    user_sentence = user_text.split(".")

    final_output = ""
    for i in range(len(user_sentence)):
        user_words = user_sentence[i].split(" ")

        output = ""
        for user_word in user_words:
            for word in word_bank:
                if user_word == word["en"]:
                    output = output + word["fa"] + " "
                    break
            else:
                output = output + user_word + " "

        print(output)
        final_output = final_output + output
    x = gtts.gTTS(final_output, lang="ar")
    x.save("speech.mp3")

def add_to_file():
    f = open("translate.txt", "a")
    f.write("\n" + input("Please enter word: "))
    f.write("\n" + input("Please enter translation: "))
    f.close()
    # f = open("translate.txt", "w")
    # new_word = input("Enter word")
    # new_translate = input("Enter translation")
    # adding_word = {"en": new_word , "fa": new_translate}
    # word_bank.append(adding_word)

read_from_file()

while True:
    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1 :
        translate_en_to_per()
    elif choice == 2:
        translate_per_to_en()
    elif choice == 3 :
        add_to_file()
    elif choice == 4:
        exit(0)
    else:
        print("enter between 1-4")

