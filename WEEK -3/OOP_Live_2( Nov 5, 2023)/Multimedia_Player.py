'''
code link:

https://gist.github.com/romjanxr/327d28a7b8a991c8345b9b5b085769fd

uml diagram:
https://ibb.co/XpynvfK

'''

from abc import ABC,abstractmethod

class Description:
    def __init__(self,description):
        self.__description = description


    def get_description(self):
        return self.__description


class Media(ABC):
    def __init__(self,title,duration):
        self.title = title
        self.duration = duration

    @abstractmethod
    def play(self):
        raise NotImplementedError


class Music(Media,Description):
    def __init__(self,title,duration,description):
        Description.__init__(self,description)
        Media.__init__(self,title,duration)

    def play(self):
        print(f"Playing music: {self.title}")

    def info(self):
        print(f"Music name: {self.title}, Description: {self.get_description()}, Duration: {self.duration}")



class Video(Media,Description):
    def __init__(self,title,duration,description):
        Description.__init__(self,description)
        Media.__init__(self,title,duration)

    def play(self):
        print(f"Playing video: {self.title}")

    def info(self):
        print(f"Video name: {self.title}, Description: {self.get_description()}, Duration: {self.duration}")

class Audiobook(Media,Description):
    def __init__(self,title,duration,description):
        Description.__init__(self,description)
        Media.__init__(self,title,duration)

    def play(self):
        print(f"Playing audiobook: {self.title}")

    def info(self):
        print(f"Audiobook name: {self.title}, Description: {self.get_description()}, Duration: {self.duration}")


class Library:
    def __init__(self):
        self.__media_items = []
        self.__media_by_genre = {}
        self.__genre = ""

    def get_media_by_genre(self):
        return self.__media_by_genre

    def add_media(self,media):
        # self.__media_items.append(media)
        if isinstance(media,Music):
            self.__genre = "Music"
        elif isinstance(media,Video):
            self.__genre = 'Video'
        elif isinstance(media,Audiobook):
            self.__genre = 'Audiobook'


        if self.__genre in self.__media_by_genre:
            self.__media_by_genre[self.__genre].append(media)

        else:
            self.__media_by_genre[self.__genre] = [media]


    def get_media_items(self):
        return self.__media_items


class Media_Player:
    def play_media(self,media):
        media.play()



class User(ABC):
    def __init__(self,name):
        self.__name = name

    @abstractmethod
    def play_media(self):
        raise NotImplementedError

class FreeUser(User):
    def __init__(self,name):
        super().__init__(name)

    def play_media(self,library):
        for media in library.get_media_items():
            print(media.info())


class PremiumUser(User):
    def __init__(self,name):
        super().__init__(name)
        self.__favourite_genre = None

    def play_media(self,library):
        # for media in library.get_media_items():
        #     if isinstance(media,Music) and self.__favourite_genre.lower() == 'music':
        #         media.info()
        #     elif isinstance(media,Video) and self.__favourite_genre.lower() == 'video':
        #         media.info()
        #     elif isinstance(media,Audiobook) and self.__favourite_genre.lower() == 'audiobook':
        #         media.info()
        if self.__favourite_genre in library.get_media_by_genre():
            for media in library.get_media_by_genre()[self.__favourite_genre]:
                media.info()






    def set_favourite_genre(self,genre):
        self.__favourite_genre = genre

    def get_favourite_genre(self):
        return self.__favourite_genre




# add media to the library

music = Music('Faded',3.5, 'song by Alan Walker')
music_2 = Music('Oniket prantor',15.6,'best song')
video = Video('Shutter Island',2.35,'De Caprio Movie')
audiobook = Audiobook('Physics audio book',5.6,'audion book on physics')

library = Library()
library.add_media(music)
library.add_media(video)
library.add_media(audiobook)
library.add_media(music_2)

premium_user = PremiumUser('Sakib Al Hasan')
premium_user.set_favourite_genre('Music')
premium_user.play_media(library)


# free_user = FreeUser('Moshiur')
# free_user.play_media(library)


# player = Media_Player()
# player.play_media(audiobook)
