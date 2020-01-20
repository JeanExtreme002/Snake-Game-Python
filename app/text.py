from pygame import font

class Text(object):

    def __init__(self, surface, text_font, size):

        self.__surface = surface
        self.__font = font.Font(text_font, size)


    def draw(self, x, y, text, color, outline = None):
        """
        Método para desenhar o texto.
        """
        surface = self.__font.render(str(text),0,color)

        if outline:
            outline_surface = self.__font.render(str(text),0,(0,0,0))
            self.__surface.blit(outline_surface, [x - outline,y])
            self.__surface.blit(outline_surface, [x + outline,y])
            self.__surface.blit(outline_surface, [x,y - outline])
            self.__surface.blit(outline_surface, [x,y + outline])

        self.__surface.blit(surface, [x,y])


    def size(self, text):
        """
        Método para obter o tamanho de um texto.
        """
        return self.__font.size(str(text))
