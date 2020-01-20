from app.apple import Apple 
from app.snake import Snake
from app.text import Text 
import pygame


class App(object):

    FPS = 20
    FONT = "font/Autumn.ttf"
    WINDOW_GEOMETRY = [400, 400]
    WINDOW_TITLE = "Snake Game"


    def __init__(self):

        pygame.init()
        pygame.display.set_mode(self.WINDOW_GEOMETRY)
        pygame.display.set_caption(self.WINDOW_TITLE)

        self.__window = pygame.display.get_surface()
        self.__snake = Snake(self.__window, size = 10)
        self.__apple = Apple(self.__window, size = 12)
        self.__clock = pygame.time.Clock()

        self.CONTROLS = {
            pygame.K_UP: self.__snake.up,
            pygame.K_DOWN: self.__snake.down,
            pygame.K_LEFT: self.__snake.left,
            pygame.K_RIGHT: self.__snake.right,
            pygame.K_RETURN: self.__playGame
        }


    def __captureEvents(self):
        """
        Captura eventos e realiza ações com base neles.
        """

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.__stop = True

            elif event.type == pygame.KEYDOWN:

                if event.key in self.CONTROLS:
                    self.CONTROLS[event.key]()


    def __gameOver(self):
        """
        Desenha uma tela de fim de jogo.
        """

        # Cria os textos.
        game_over_text = Text(self.__window, self.FONT , 60)
        game_over_text_size = game_over_text.size("GAME OVER")

        score_text = Text(self.__window, self.FONT, 100)
        score_text_size = score_text.size(self.__score)

        self.__play = False

        # Permanece na tela de fim de jogo enquanto o usuário não pedir
        # para sair ou para iniciar um novo jogo.
        while not self.__stop and not self.__play:

            self.draw()

            h_width = self.WINDOW_GEOMETRY[0] // 2
            h_height = self.WINDOW_GEOMETRY[1] // 2

            # Desenha os textos na tela.
            game_over_text.draw(h_width - game_over_text_size[0] // 2, 10, "GAME OVER", (255, 0, 0), outline = 1)

            score_text.draw(
                h_width - score_text_size[0] // 2, h_height - score_text_size[1] // 2,
                self.__score, (255,255,0), outline = 2
                )
            
            self.update()

        # Verifica se o jogador pediu para sair.
        if not self.close():
            self.start()


    def __playGame(self):
        """
        Método de evento para jogar o jogo novamente.
        """
        self.__play = True


    def __reset(self):
        """
        Método para resetar o jogo.
        """

        self.__snake.clear()
        self.eat()
        self.__stop = False
        self.__score = 0


    def close(self):
        """
        Método para fechar o jogo caso o usuário tenha pedido.
        """

        if self.__stop:
            pygame.quit()
            return True
        return False


    def draw(self):
        """
        Método para atualizar os desenhos do jogo.
        """

        self.__window.fill((0,0,0))
        self.__snake.draw()
        self.__apple.draw()


    def eat(self):
        """
        Verifica se a cobra comeu a maçã.
        """
        self.__snake.increase(self.__apple.createNewApple)


    def start(self):
        """
        Método para iniciar o jogo.
        """

        self.__reset()

        while not self.__stop:

            # Move a cobra e verifica se colidiu.
            self.__snake.move()
            if self.__snake.collided(): break

            # Verifica se a cobra comeu a maçã.
            if self.__apple.rect in self.__snake:
                self.__score += 1
                self.eat()

            self.draw()
            self.update()

        # Verifica se o usuário pediu para sair.
        if not self.close():
            self.__gameOver()
            

    def update(self):
        """
        Método para atualizar o jogo.
        """

        pygame.display.flip()
        self.__captureEvents()
        self.__clock.tick(self.FPS)
