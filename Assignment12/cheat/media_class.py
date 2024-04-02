import pytube

class Media():
    def __init__(self, name, director, imdbscore, url, duration, cast, productionyear):
        self.name = name
        self.director = director
        self.imdb_score = imdbscore
        self.url = url
        self.duration = duration
        self.cast = cast
        self.productionyear = productionyear
        

    def showInfo(self):
        print(self.name, "\t", self.director, "\t", self.imdb_score, "\t", self.url, "\t", self.duration, "\t", self.cast, "\t", self.productionyear )

    def downloads(self):
        user_choice=input("enter media name to download: ")
        if user_choice==self.name:
            first_streams= pytube.YouTube(self.url).streams.first()
            first_streams.download(output_path="XX.txt", filename="")

    
