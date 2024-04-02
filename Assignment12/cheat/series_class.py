
from media_class import Media

class Series(Media):
    def __init__(self, casts):
        super().__init__()
        self.casts=casts