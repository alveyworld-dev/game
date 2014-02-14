import pygame

class Sound():

    """
    Represents a sound effect
    """

    def __init__(self, filename):
        self.sound = pygame.mixer.Sound(filename)

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()


class Music():

    """
    Represents a song
    """

    def __init__(self, filename):
        pygame.mixer.music.load(filename)

    def play(self, loops=0):
        pygame.mixer.music.play(loops)

    def stop(self):
        pygame.mixer.music.stop()