# Terminal Snake Game

# Inverted coordinate values for moving based on 2D Arrays
# indexing for position

class Snake:
    def __init__(self, init_body, init_direction) -> None:
        self._body = init_body
        self._direction = init_direction

    def take_step(self, position):
        self._body = self._body[1:1].append(position)
    
    def set_direction(self, direction):
        self._direction = direction

    def head(self):
        return self._body[-1]

class Apple:
    pass

class Game:
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    
    EMPTY = 0
    BODY = 1
    HEAD = 2
    APPLE = 3

    GRID_SYMBOLS = {
        EMPTY: " ",
        BODY: "O",
        HEAD: "X",
        APPLE: "*",
    }

    def play():
        pass

    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width
        self._snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], self.UP)

    def _board_matrix(self):
        matrix = [[self.EMPTY for _ in range(self.height)] for _ in range(self.width)]
        for co in self._snake._body:
            matrix[co[0]][co[1]] = self.BODY

        head = self._snake.head()
        matrix[head[0]][head[1]] = self.HEAD
        print(matrix)
        return matrix

    def _render(self):
        matrix = self._board_matrix()

        top_and_bottom_border = "+" + "-" * self.width + "+"

        print(top_and_bottom_border)
        for y in range(0, self.height):
            line = "|"
            for x in range(0, self.width):
                cell_val = matrix[x][self.height-1-y]
                line += self.GRID_SYMBOLS[cell_val]
            line += "|"
            print(line)
        print(top_and_bottom_border)


game = Game(10, 8)
game._render()