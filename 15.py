import random

class P15:
    def __init__(self):
        """
        инициализация поля
        """
        self.size = 4   # размер поля
        self.board = [  # массив
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.empty = (3, 3)   # расположение пустой клетки
        self.initialize()

    def initialize(self):
        """
        инициализация цифрами
        """
        numbers = list(range(1, 16)) # создаем и перемешиваем цифры
        random.shuffle(numbers)

        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if count < len(numbers):
                    self.board[i][j] = numbers[count]
                    count += 1
                else:
                    self.board[i][j] = 0  # пустая клетка

    def print_board(self):
        """
        вывод поля
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0: # пустая клетка
                    print("   ", end=" ")
                else:
                    print(f"{self.board[i][j]:2}", end=" ")
            print()

    def can_move(self, row, col):
        er, ec = self.empty # соседняя пустая клетка
        return (abs(row - er) == 1 and col == ec) or (abs(col - ec) == 1 and row == er)

    def move(self, row, col):
        """
        перемещение
        """
        if self.can_move(row, col): # меняем местами с пустой клеткой
            er, ec = self.empty
            self.board[er][ec] = self.board[row][col]
            self.board[row][col] = 0
            self.empty = (row, col)
            return True
        return False

    def is_solved(self):
        """
        проверка результата
        """
        num = 1
        for i in range(4):
            for j in range(4):
                if i == 3 and j == 3:
                    if self.board[i][j] != 0:
                        return False
                else:
                    if self.board[i][j] != num:
                        return False
                    num += 1
        return True


def main():
    game = P15()

    print("Игра - головоломка '15'")
    print("Перемещайте плитки, чтобы расставить числа по порядку")
    print("Используйте: w(вверх), s(вниз), a(влево), d(вправо), q(выход)")

    while True:
        game.print_board()

        if game.is_solved():
            print("\nГоловоломка решена")
            break

        move = input("\nХод(wasd/q): ").lower()

        if move == 'q':
            print("Выход из игры")
            break

        er, ec = game.empty #определяем возможно ли перемещение
        if move == 'w' and er < 3:
            game.move(er + 1, ec)
        elif move == 's' and er > 0:
            game.move(er - 1, ec)
        elif move == 'a' and ec < 3:
            game.move(er, ec + 1)
        elif move == 'd' and ec > 0:
            game.move(er, ec - 1)
        else:
            print("\nХод невозможен\n")


if __name__ == "__main__":

    main()
