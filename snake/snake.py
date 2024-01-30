# Terminal Snake Game

# Inverted coordinate values for moving based on 2D Arrays
# indexing for position

class Snake(object):
    def __init__(self, init_body, init_direction) -> None:
        self._body = init_body
        self._direction = init_direction

    def take_step(self, position):
        self._body = self._body[1:] + [position]
    
    def set_direction(self, direction):
        self._direction = direction

    def extend_body(self, position):
        self._body.append(position)

    def head(self):
        return self._body[-1]

class Apple(object):
    def __init__(self, location):
        self._location = location

class Game(object):
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

    INPUT_UP = "W"
    INPUT_DOWN = "S"
    INPUT_LEFT = "A"
    INPUT_RIGHT = "D"

    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], self.UP)

    def play(self):
        self._render()

        while True:
            direction = input().upper()
            if direction == self.INPUT_UP:
                self.snake.set_direction(self.UP)
            elif direction == self.INPUT_DOWN:
                self.snake.set_direction(self.DOWN)
            elif direction == self.INPUT_LEFT:
                self.snake.set_direction(self.LEFT)
            elif direction == self.INPUT_RIGHT:
                self.snake.set_direction(self.RIGHT)
            next_position = self._next_position(self.snake.head(), self.snake._direction)
            self.snake.take_step(next_position)
            self._render()

    def _next_position(self, position, direction):
        return (
            (position[0] + direction[0]) % self.width,
            (position[1] + direction[1]) % self.height
        )

    def _board_matrix(self):
        matrix = [[self.EMPTY for _ in range(self.height)] for _ in range(self.width)]
        for co in self.snake._body:
            matrix[co[0]][co[1]] = self.BODY

        head = self.snake.head()
        matrix[head[0]][head[1]] = self.HEAD
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
game.play()