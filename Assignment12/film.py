                              # CLASS FILM ( CHILD CLASS )

from media import Media

class Film ( Media ) :

    def __init__ ( self , type , name , director , imbd , url , duration , casts , genre ) :
        super().__init__ ( type , name , director , imbd , url , duration , casts )
        self.gener = genre