import string
class Unit:
    """
    Базовый класс для шашек.

    Атрибуты:
        SYMBOLS (dict): Словарь, сопоставляющий символы шашек с их Unicode-представлениями.
        color (str): Цвет шашки ('W' для белых, 'B' для чёрных).
        name (str): Тип шашки ('C' для обычной шашки, 'D' для дамки).
        symbol (str): Символ шашки, зависящий от её цвета.
    """
    SYMBOLS = {'C': '⛀', 'D': '⛁'}  # C - обычная шашка, D - дамка

    def __init__(self, color, name):
        """
        Конструктор для инициализации шашки.

        Аргументы:
            color (str): Цвет шашки ('W' или 'B').
            name (str): Тип шашки ('C' или 'D').
        """
        self.color = color
        self.name = name
        self.symbol = self.SYMBOLS[name] if color == 'W' else self.SYMBOLS[name].lower()

    def is_valid_move(self, start, end, board):
        """
        Проверяет, является ли ход корректным для шашки.

        Аргументы:
            start (tuple): Начальная позиция шашки (строка, столбец).
            end (tuple): Конечная позиция шашки (строка, столбец).
            board (list): Игровая доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        return False

    def get_possible_moves(self, start, board):
        """
        Возвращает список возможных ходов для шашки.

        Аргументы:
            start (tuple): Текущая позиция шашки (строка, столбец).
            board (list): Игровая доска (двумерный список).

        Возвращает:
            list: Список возможных ходов.
        """
        return []

class Checker(Unit):
    """
    Класс, представляющий обычную шашку.

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации обычной шашки.

        Аргументы:
            color (str): Цвет шашки ('W' или 'B').
        """
        super().__init__(color, 'C')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для обычной шашки.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Игровая доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        direction = -1 if self.color == 'W' else 1
        start_row, start_col = start
        end_row, end_col = end

        # Обычный ход
        if abs(start_col - end_col) == 1 and end_row == start_row + direction and board[end_row][end_col] is None:
            return True

        # Ход с взятием
        if abs(start_col - end_col) == 2 and abs(start_row - end_row) == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            if board[mid_row][mid_col] and board[mid_row][mid_col].color != self.color:
                return True

        return False

    def get_possible_moves(self, start, board):
        """
        Возвращает список возможных ходов для обычной шашки.

        Аргументы:
            start (tuple): Текущая позиция шашки (строка, столбец).
            board (list): Игровая доска (двумерный список).

        Возвращает:
            list: Список возможных ходов.
        """
        moves = []
        for drow, dcol in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            end = (start[0] + drow, start[1] + dcol)
            if 0 <= end[0] < 8 and 0 <= end[1] < 8 and self.is_valid_move(start, end, board):
                moves.append(end)
        return moves

class Board:
    """
    Класс, представляющий игровую доску.

    Атрибуты:
        grid (list): Двумерный список, представляющий игровую доску.
    """
    def __init__(self):
        """
        Конструктор для инициализации доски и расстановки шашек.
        """
        self.grid = [[None] * 8 for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        """
        Расставляет шашки на доске в начальной позиции.
        """
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Checker('B')

        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Checker('W')

    def display(self, move_count):
        """
        Отображает текущее состояние доски.

        Аргументы:
            move_count (int): Номер текущего хода.
        """
        print(f"Ход: {move_count}")
        print("  a b c d e f g h")
        print("  ----------------")
        for row in range(8):
            print(8 - row, end="| ")
            for col in range(8):
                if self.grid[row][col]:
                    print(self.grid[row][col].symbol, end=' ')
                else:
                    print('.', end=' ')
            print(f"| {8 - row}")
        print("  ----------------")
        print("  a b c d e f g h")

    def move_piece(self, start, end):
        """
        Перемещает шашку на доске, если ход корректен.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).

        Возвращает:
            bool: True, если ход выполнен успешно, иначе False.
        """
        piece = self.grid[start[0]][start[1]]
        if piece and piece.is_valid_move(start, end, self.grid):
            mid_row = (start[0] + end[0]) // 2
            mid_col = (start[1] + end[1]) // 2
            if abs(start[0] - end[0]) == 2:
                self.grid[mid_row][mid_col] = None  # Убираем побитую шашку
            self.grid[end[0]][end[1]] = piece
            self.grid[start[0]][start[1]] = None
            if (piece.color == 'W' and end[0] == 0) or (piece.color == 'B' and end[0] == 7):
                self.grid[end[0]][end[1]] = Piece(piece.color, 'D')  # Превращение в дамку
            return True
        return False

class Game:
    """
    Класс, управляющий игрой в шашки.

    Атрибуты:
        board (Board): Объект доски.
        current_turn (str): Текущий ход ('W' для белых, 'B' для чёрных).
        move_count (int): Счётчик ходов.
    """
    def __init__(self):
        """
        Конструктор для инициализации игры.
        """
        self.board = Board()
        self.current_turn = 'W'
        self.move_count = 0

    def parse_input(self, move):
        """
        Парсит ввод пользователя в координаты на доске.

        Аргументы:
            move (str): Ввод пользователя (например, 'e3d4').

        Возвращает:
            tuple: Начальная и конечная позиции в виде кортежей (строка, столбец).
        """
        if len(move) != 4 or move[0] not in string.ascii_lowercase[:8] or move[2] not in string.ascii_lowercase[:8]:
            return None, None
        try:
            start = (8 - int(move[1]), string.ascii_lowercase.index(move[0]))
            end = (8 - int(move[3]), string.ascii_lowercase.index(move[2]))
            return start, end
        except ValueError:
            return None, None

    def play(self):
        """
        Основной цикл игры.
        """
        while True:
            self.board.display(self.move_count)
            move = input(f"Ход {'белых' if self.current_turn == 'W' else 'чёрных'} (например, e3-d4): ")
            move = move.replace("-", "")
            start, end = self.parse_input(move)
            if start and end and self.board.move_piece(start, end):
                self.move_count += 1
                self.current_turn = 'B' if self.current_turn == 'W' else 'W'
            else:
                print("Неверный ход, попробуйте снова.")

if __name__ == "__main__":
    game = Game()
    game.play()
