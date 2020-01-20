from pygame import draw
from pygame import rect

class Snake(object):

    __body = []


    def __contains__(self, rect):
        return self.__body[0].colliderect(rect)


    def __init__(self, surface, size = 10, color = (0, 255, 0)):

        self.__surface = surface
        self.__size = size
        self.__color = color

        self.__DOWN = (0, size)
        self.__UP = (0, -size)
        self.__LEFT = (-size, 0)
        self.__RIGHT = (size, 0)
        self.__direction = self.__DOWN


    def clear(self):
        """
        Método para apagar a cobra.
        """
        self.__body.clear()


    def collided(self):
        """
        Método para verificar se a cobra colidiu nela mesma.
        """

        head = self.__body[0]

        for rect in self.__body[1:]:
            if head.colliderect(rect): 
                return True
        return False


    def draw(self):
        """
        Método para desenhar a cobra.
        """
        for rect in self.__body:
            draw.rect(self.__surface, self.__color, rect)


    def increase(self, callback = lambda:None):
        """
        Método para crescer o corpo da cobra.
        """

        if not self.__body:
            width , height = self.__surface.get_size()
            x , y = width / 2 - self.__size / 2 , height / 2 - self.__size / 2       
        else:
            x , y = self.__body[-1].x , self.__body[-1].y

        self.__body.append(rect.Rect(x, y, self.__size, self.__size))
        callback()


    def move(self):
        """
        Método para mover a cobra.
        """

        # Obtém a largura e altura da janela.
        width , height = self.__surface.get_size()

        # Verifica se a cobra ultrapassou os limites da janela no eixo X.
        if self.__body[0].x < 0:
            self.__body[0].x = width

        elif self.__body[0].x + self.__size > width:
            self.__body[0].x = 0

        # Verifica se a cobra ultrapassou os limites da janela no eixo Y.
        if self.__body[0].y < 0:
            self.__body[0].y = height

        elif self.__body[0].y + self.__size > height:
            self.__body[0].y = 0

        # Move a cabeça da cobra primeiro.
        last_pos = (self.__body[0].x , self.__body[0].y)
        self.__body[0].x += self.__direction[0]
        self.__body[0].y += self.__direction[1]

        # Verifica se além da cabeça a cobra possui um corpo.
        if len(self.__body) < 2: return

        # Move cada parte do corpo para a posição do bloco anterior.
        for rect in self.__body[1:]:
            current = (rect.x , rect.y)
            rect.x = last_pos[0]
            rect.y = last_pos[1]
            last_pos = current


    def up(self):
        """
        Move a cobra para cima.
        """

        if not self.__direction == self.__DOWN:
            self.__direction = self.__UP


    def down(self):
        """
        Move a cobra para baixo.
        """

        if not self.__direction == self.__UP:
            self.__direction = self.__DOWN


    def left(self):
        """
        Move a cobra para esquerda.
        """

        if not self.__direction == self.__RIGHT:
            self.__direction = self.__LEFT


    def right(self):
        """
        Move a cobra para direita.
        """

        if not self.__direction == self.__LEFT:
            self.__direction = self.__RIGHT




