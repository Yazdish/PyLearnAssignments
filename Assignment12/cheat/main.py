import pytube

from media_class import Media
from film_class import Film
from clip_class import Clip
from documentary_class import Documentary
from series_class import Series

MEDIA=[]

def read_from_database():
    f=open("cheat/XX.txt", "r")

    for line in f.readlines():
        result=line.split(",")
        media=Media(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
        MEDIA.append(media)
        print(MEDIA)

    f.close()

def write_to_database():
    f=open("cheat/XX.txt", "w")
    for media in MEDIA:
        f.write(str(media.name)+ ","+ str(media.director)+ ","+ str(media.imdb_score)+ ","+ str(media.url)+ ","+ str(media.duration)+ ","+ str(media.cast)+ ","+ str(media.productionyear)+ "\n")
    
    print("your data sucessfylly saved")
    f.close()

def show_menu():
    print("1- add")
    print("2- remove")
    print('3- edit')
    print("4- search")
    print("5- advanced search")
    print("6- show list")
    print("7- show info")
    print("8- download")
    print("9- exit")
    print()

def add():
    name=input("enter film name: ")
    director=input("enter film director: ")
    imdb_score=input("enter imdb score: ")
    url=input("enter film url: ")
    duration= input("enter film duration: ")
    casts=input(" enter film casts: ")
    productionyear= input("enter production year of media: ")

    new_media= Media(name, director, imdb_score, url, duration, casts, productionyear)
    MEDIA.append(new_media)
    new_media.showInfo()
    
def remove():
    name= input("enter film name: ")
    for media in MEDIA:
        if media.name==name:
            MEDIA.remove(media)
            print("media was successfully removed")
            break

        else:
            print("not found!")


def edit():
    
    field_choice=int(input("enter which field you want toedit(1-7)?"))
    for media in MEDIA:
        if field_choice==1:
            new=input("enter new name: ")
            media.name=new
            media.showInfo()
            print("successfully edited")
            break
        elif field_choice==2:
            new=input("enter new director:")
            media.director=new
            media.showInfo()
            print("successfully edited")
            break
        elif field_choice==3:
            new=input("enter new imdb_score:")
            media.imdb_score=new
            media.showInfo()
            print("successfully edited")
            break
        elif field_choice==4:
            new=input("enter new url: ")
            media.url=new
            media.showInfo()
            print("successfully edited")
            break
        elif field_choice==5:
            new=input("enter new duration: ")
            media.duration=new
            media.showInfo()
            print("successfully edited")
            break
        elif field_choice==6:
            new=int(input("enter new cast:"))
            media.casts=new
            media.showInfo()
            print("successfully edited")
            break
        elif field_choice==7:
            new=int(input("enter film production's year:"))
            media.productionyear=new
            media.showInfo()
            print("successfully edited")
            break
    else:
        print("media not found!")

def search():
    user_input=input("enter keyword(movie name or director):")
    for media in MEDIA:
        if media.name==user_input or media.director== user_input:
            print(media.name, "\t" , media.director, "\t" , media.imdb_score, "\t" , media.url, "\t" , media.cast, "\t" , media.productionyear)
            break
    else:
        print("not found!")


def advanced_search():
    i=int(input("enter minimum time in minute: "))
    e=int(input("enter maximum time in minute:"))
    n=0
    for media in MEDIA:
        if media.duration.isnumeric() and i<=int(media.duration)<=e: 
            media.showInfo()
            n+=1
        if n==0:
            print("media duration between", i, "and", e, "was not found!")


def show_list():
    print("name \t director \t imdbscore \t url \t duration \t casts of film")
    for media in MEDIA:
        print(media.name, "\t", media.director, "\t", media.imdb_score, "\t", media.url, "\t", media.duration, "\t", media.cast )


print("welcome to my media management program")
print(" please wait, loading...")
read_from_database()
print("data loaded")

while True:
    
    show_menu()

    choice=int(input("enter your choice: "))
    if choice==1:
        add()
    elif choice==2:
        remove()
    elif choice==3:
        edit()
    elif choice==4:
        search()
    elif choice==5:
        advanced_search()
    elif choice==6:
        show_list()
    elif choice==7:
        name=input("enter media's name: ")
        for media in MEDIA:
            if media.name==name:
                media.showInfo()
                break
        else:
            print("media not found!")

    elif choice==8:
        name=input("enter media's name: ")
        for media in MEDIA:
            if media.name==name:
                media.downloads()
                break
        else:
            print("media not found!")

    elif choice==9:
        write_to_database()
        exit(0)

    else:
        print("incorrect input!")