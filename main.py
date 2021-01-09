import numpy as np


class Life:
    DEAD = 0
    ALIVE = 255

    def __init__(self, board_heigth: int, board_width: int):
        self.board_heigth = board_heigth
        self.board_width = board_width
        self.curr_board = np.zeros(shape=(board_heigth, board_width), dtype=np.int8)
        self.next_board = np.zeros(shape=(board_heigth, board_width), dtype=np.int8)

    def __is_alive(self, x: int, y: int):
        if self.curr_board[x][y] == self.ALIVE:
            return True

    def __is_dead(self, x: int, y: int):
        if self.curr_board[x][y] == self.DEAD:
            return False

    def __count_live_neighbours(self, x: int, y: int):
        count = 0
        neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x = x + i
                new_y = y + j

                if new_x < 0 or new_y < 0:
                    continue
                if new_x >= self.board_heigth or new_y >= self.board_width:
                    continue
                if new_x == x and new_y == y:
                    continue
                neighbours += 1
                if self.__is_alive(new_x, new_y):
                    count += 1
        return count

    def __evolve_tile(self, x: int, y: int):
        live_neighbours = self.__count_live_neighbours(x, y)
        if self.__is_alive and (live_neighbours < 2 or live_neighbours > 3):
            self.next_board[x][y] = self.DEAD
        elif self.__is_dead(x, y) and live_neighbours == 3:
            self.next_board[x][y] = self.ALIVE

    def next_generation(self):
        for row in range(0, self.board_heigth):
            for column in range(0, self.board_width):
                self.__evolve_tile(row, column)
        self.curr_board, self.next_board = self.next_board, self.curr_board


def main():
    life = Life(10, 10)
    life.next_generation()


if __name__ == '__main__':
    main()
