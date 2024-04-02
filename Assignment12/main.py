from media import Media
from series import Series
from film import Film
from documentary import Documentary
from clip import Clip
from actors import Actor

OBJECTS = []
ACTORS = []

class Database :

    def read ( self ) :
        f = open ( "database.txt" , "r" )
        for line in f :
            text = line.split("\n")
            obj = text[0]
            result = obj.split (",")
            if result[0] == "film" :
                my_object = Film ( result[0] , result[1] , result[2] , result[3] , result[4] , result[5] , result[6] , result[7] )
            
            elif result[0] == "series" :
                my_object = Series ( result[0] , result[1] , result[2] , result[3] , result[4] , result[5] , result[6] , result[7] , result[8] )

            elif result[0] == "documentary" :
                my_object = Documentary ( result[0] , result[1] , result[2] , result[3] , result[4] , result[5] , result[6] )

            elif result[0] == "clip" :
                my_object = Clip ( result[0] , result[1] , result[2] , result[3] , result[4] , result[5] , result[6] , result[7] )

            OBJECTS.append ( my_object )
        f.close ()

    def write ( self ) :
        f = open ( "database.txt" , "w" )
        for obj in OBJECTS :
            if obj.type == "series" :
                text = obj.type + "," + obj.name + "," + obj.director + "," + obj.IMBD_score + "," + obj.url + "," + obj.duration + "," + obj.casts + "," + obj.episode + "," + obj.genre + "\n"           
                print ("added to series")
                f.write ( text )

            elif obj.type == "documentary" :
                text = obj.type + "," + obj.name + "," + obj.director + "," + obj.IMBD_score + "," + obj.url + "," + obj.duration + "," + obj.casts + "\n"
                print ("added to documentary")
                f.write ( text )

            else :
                text = obj.type + "," + obj.name + "," + obj.director + "," + obj.IMBD_score + "," + obj.url + "," + obj.duration + "," + obj.casts + "," + obj.genre + "\n"
                print ("added to film/clip")
                f.write ( text )

        f.close ()


class Store :
    @staticmethod
    def show_menu() :
        print ()
        print (" Enter 1 to Add ")
        print (" Enter 2 to Edit ")
        print (" Enter 3 to Remove ")
        print (" Enter 4 to Search media ")
        print (" Enter 5 to Advanced Search ")
        print (" Enter 6 to Show the list ")
        print (" Enter 7 to Show the info ")
        print (" Enter 8 to download ")
        print (" Enter 9 to see the list of actors ")
        print (" Enter 10 to Exit ")
        print ()

    @staticmethod
    def add () :
        type = input (" Please enter type of media you want to add ( choose between series , film , documentary , clip) : ")
        if type == "series" or type == "film" or type == "clip" or type == "documentary" :
            name = input (" Please enter the name : ")
            director = input (" Please enter the director : ")
            imbd = input (" Please enter IMBD score : ")
            url = input (" Please enter the URL : ")
            duration = input (" Pleae enter the duration : ")
            casts = input (" Please enter the actors ( split them with '-') : ")
            if type == "series" :
                episod = input (" Please enter the number of episodes : ")
                genre = input (" Please enter the genre : ")
                obj = Series ( type , name , director , imbd , url , duration , casts , episod , genre )
                OBJECTS.append ( obj )
            
            elif type == "documentary" :
                obj = Documentary ( type , name , director , imbd , url , duration , casts )
                OBJECTS.append ( obj )
            
            elif type == "film" or type == "clip" :
                gener = input (" Please enter the genre : ")
                obj = Film ( type , name , director , imbd , url , duration , casts , genre )
                OBJECTS.append ( obj )
            
            print (" done ")

        else :
            print (" ❌❌ Wrong type of input ❌❌ ")
        

    @staticmethod
    def edit () :
        obj = Store.search ()
        if obj != " No " :
            print (" Remember that documentary doesn't have episode and genre , also film and clip don't have genre 😊")
            user_change = input (" Which part of this media you want to change ? ( name , director , IMBD_score , url , duration , casts , genre , episode ) : ")
            if user_change == "name" :
                obj.name = input (" Please enter new information : ")
                print (" done ")

            elif user_change == "director" :
                obj.director = input (" Please enter new information : ")
                print (" done ")

            elif user_change == "IMBD_score" :
                obj.IMBD_score = input (" Please enter new information : ")
                print (" done ")

            elif user_change == "url" :
                obj.url = input (" Please enter new information : ")
                print (" done ")

            elif user_change == "duration" :
                obj.duration = input (" Please enter new information : ")
                print (" done ")

            elif user_change == "casts" :
                obj.casts = input (" Please enter new information : ")
                print (" done ")

            elif user_change == "genre" :
                if obj.type == "documentary" :
                    print (" ❌❌ Wrong input ❌❌ ")
                    print (" Documentaries don't have genre")
                else :
                    obj.genre = input (" Please enter new information : ")
                    print (" done ")

            elif user_change == "episode" :
                if obj.type == "series" :
                    obj.episode = input (" Please enter new information : ")
                    print (" done ")
                
                else :
                    print (" ❌❌ Wrong input ❌❌ ")
                    print (" only series have episode ")

            else :
                print (" ❌❌ Wrong input ❌❌ ")


    @staticmethod
    def remove () :
        obj = Store.search ()
        if obj != " No " :
            OBJECTS.remove ( obj )
            print (" done ")
        

    @staticmethod
    def search () :
        user_input = input (" Please enter the name of media you are looking for : ")
        for obj in OBJECTS :
            if obj.name == user_input :
                print (" The media found ✅✅ ")
                return obj
        
        else :
            print (" Sorry😞 This media doesn't exist ")
            return (" No ")
        

    @staticmethod
    def advanced_search () :
        low = int ( input (" Please enter the lower range of duration : "))
        high = int ( input (" Please enter the higher range of duration : "))
        for obj in OBJECTS :
            lenght = int ( obj.duration )
            if low <= lenght <= high :
                print ( obj.name + " , " + obj.duration + " min" )

    
    @staticmethod
    def media_list () :
        for obj in OBJECTS :
            print ( obj.type + " , " + obj.name + " , " + obj.casts )


    @staticmethod
    def show_information () :
        obj = Store.search ()
        if obj != " No " :
            obj.showInfo ()


    @staticmethod
    def download () :
        obj = Store.search ()
        if obj != " No " :
            obj.download ()
    
    
    @staticmethod
    def actors () :
        obj = Store.search ()
        if obj != " No " :
            result = obj.casts.split ( "-" )
            
        for x in result :
            person = Actor ( x )
            ACTORS.append ( person )
        
        for x in ACTORS :
            print ( x.name )
            

print (" Hello😊! Welcom to DI$H MEDIA.")
print (" Please waite✋! Loading... ")
data = Database ()
data.read ()
print (" Data loaded👍 Thaks for your patience ")


while True :
    Store.show_menu ()
    user_choice = input (" Please enter your choice : ")
    if user_choice == "1" :
        Store.add ()
    
    elif user_choice == "2" :
        Store.edit ()
    
    elif user_choice == "3" :
        Store.remove ()

    elif user_choice == "4" :
        Store.search ()

    elif user_choice == "5" :
        Store.advanced_search ()

    elif user_choice == "6" :
        Store.media_list ()

    elif user_choice == "7" :
        Store.show_information ()
    
    elif user_choice == "8" :
        Store.download ()

    elif user_choice == "9" :
        Store.actors ()
    
    elif user_choice == "10" :
        data.write ()
        exit (0)
    
    else :
        print (" ❌❌ Your entered input is wrong ... ❌❌ ")
        print (" Please enter right inputs ... 🧐 ")