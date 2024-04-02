from media import Media
class Documentary(Media):
    def __init__(self, name, director, imdbScore, url, duration, casts, yearReleased):
        super().__init__(name, director, imdbScore, url, duration, casts, yearReleased)