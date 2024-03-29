# Terminal Snake Game

import random
import time

class Snake(object):
    def __init__(self, init_body=[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], 
                 init_direction=(1, 0)) -> None:
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
    def __init__(self, location) -> None:
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

    def __init__(self, width=15, height=10) -> None:
        self.height = height
        self.width = width
        self.snake = Snake()

    def play(self):
        self.score = 0
        self.total_apples = 0
        self._generate_apple()
        self._render()

        while True:
            direction = input().upper()
            match direction:
                case self.INPUT_UP:
                    self.snake.set_direction(self.UP)
                case self.INPUT_DOWN:
                    self.snake.set_direction(self.DOWN)
                case self.INPUT_LEFT:
                    self.snake.set_direction(self.LEFT)
                case self.INPUT_RIGHT:
                    self.snake.set_direction(self.RIGHT)

            next_position = self._next_position(self.snake.head(), self.snake._direction)
            if next_position in self.snake._body:
                print("You crashed into yourself!")
                break

            if next_position == self.current_apple._location:
                self.snake.extend_body(next_position)
                self.total_apples += 1
                self.score += (10 * self.total_apples) // 5
                self._generate_apple()
            else:
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

        apple = self.current_apple._location
        matrix[apple[0]][apple[1]] = self.APPLE
        
        return matrix

    def _generate_apple(self):
        while True:
            apple_location = (
                random.randint(0, self.width - 1),
                random.randint(0, self.height - 1)
            )
            if apple_location not in self.snake._body:
                break
        self.current_apple = Apple(apple_location)

    def _render(self):
        matrix = self._board_matrix()

        top_and_bottom_border = "+" + "-" * self.width + "+"

        print("SCORE:", self.score)
        print(top_and_bottom_border)
        for y in range(0, self.height):
            line = "|"
            for x in range(0, self.width):
                cell_val = matrix[x][self.height-1-y]
                line += self.GRID_SYMBOLS[cell_val]
            line += "|"
            print(line)
        print(top_and_bottom_border)

if __name__ == "__main__":
    game = Game()
    game.play()