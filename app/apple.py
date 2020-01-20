from pygame import draw
from pygame import rect
import random


class Apple(object):

    def __init__(self, surface, size = 10, color = (255,0,0) , margin = [50,50]):

        self.__surface = surface
        self.__size = size
        self.__color = color
        self.__margin = margin


    def createNewApple(self):
        """
        Método para criar uma nova maçã.
        """

        width, height = self.__surface.get_size()

        x = random.randint(self.__size + self.__margin[0] , width - self.__size - self.__margin[0])
        y = random.randint(self.__size + self.__margin[1] , height - self.__size - self.__margin[1])

        self.__rect = rect.Rect(x, y, self.__size, self.__size)


    def draw(self):
        """
        Método para desenhar a maçã.
        """
        draw.rect(self.__surface, self.__color, self.__rect)


    @property
    def rect(self):
        return self.__rect