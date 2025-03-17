import string
class Unit:
    """
    Базовый класс для шахматных фигур.

    Атрибуты:
        SYMBOLS (dict): Словарь, сопоставляющий символы фигур с их Unicode-представлениями.
        color (str): Цвет фигуры ('W' для белых, 'B' для чёрных).
        name (str): Название фигуры (например, 'P' для пешки).
        symbol (str): Символ фигуры, зависящий от её цвета.
    """
    SYMBOLS = {'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'S': '♜', 'W': '♞', 'M': '♝'}

    def __init__(self, color, name):
        """
        Конструктор для инициализации фигуры.

        Аргументы:
            color (str): Цвет фигуры ('W' или 'B').
            name (str): Название фигуры (например, 'P' для пешки).
        """
        self.color = color
        self.name = name
        self.symbol = self.SYMBOLS[name] if color == 'W' else self.SYMBOLS[name].lower()

    def is_valid_move(self, start, end, board):
        """
        Проверяет, является ли ход корректным для фигуры.

        Аргументы:
            start (tuple): Начальная позиция фигуры (строка, столбец).
            end (tuple): Конечная позиция фигуры (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        return False  

    def is_path_clear(self, start, end, board):
        """
        Проверяет, свободен ли путь между начальной и конечной позициями.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если путь свободен, иначе False.
        """
        start_row, start_col = start
        end_row, end_col = end
        row_step = 1 if end_row > start_row else -1 if end_row < start_row else 0
        col_step = 1 if end_col > start_col else -1 if end_col < start_col else 0
        row, col = start_row + row_step, start_col + col_step
        while (row, col) != (end_row, end_col):
            if board[row][col] is not None:
                return False
            row += row_step
            col += col_step
        return True

class Pawn(Unit):
    """
    Класс, представляющий пешку.

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации пешки.

        Аргументы:
            color (str): Цвет пешки ('W' или 'B').
        """
        super().__init__(color, 'P')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для пешки.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        direction = -1 if self.color == 'W' else 1
        start_row, start_col = start
        end_row, end_col = end
        if start_col == end_col and end_row == start_row + direction and board[end_row][end_col] is None:
            return True
        if start_col == end_col and start_row == (6 if self.color == 'W' else 1) and end_row == start_row + 2 * direction and board[end_row][end_col] is None and board[start_row + direction][end_col] is None:
            return True
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            return board[end_row][end_col] is not None and board[end_row][end_col].color != self.color
        return False

class Rook(Unit):
    """
    Класс, представляющий ладью.

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации ладьи.

        Аргументы:
            color (str): Цвет ладьи ('W' или 'B').
        """
        super().__init__(color, 'R')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для ладьи.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        if (start[0] == end[0] or start[1] == end[1]) and self.is_path_clear(start, end, board):
            return board[end[0]][end[1]] is None or board[end[0]][end[1]].color != self.color
        return False

class Knight(Unit):
    """
    Класс, представляющий коня.

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации коня.

        Аргументы:
            color (str): Цвет коня ('W' или 'B').
        """
        super().__init__(color, 'N')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для коня.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        row_diff, col_diff = abs(start[0] - end[0]), abs(start[1] - end[1])
        return (row_diff, col_diff) in [(2, 1), (1, 2)] and (board[end[0]][end[1]] is None or board[end[0]][end[1]].color != self.color)

class Bishop(Unit):
    """
    Класс, представляющий слона.

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации слона.

        Аргументы:
            color (str): Цвет слона ('W' или 'B').
        """
        super().__init__(color, 'B')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для слона.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        if abs(start[0] - end[0]) == abs(start[1] - end[1]) and self.is_path_clear(start, end, board):
            return board[end[0]][end[1]] is None or board[end[0]][end[1]].color != self.color
        return False

class Queen(Unit):
    """
    Класс, представляющий ферзя.

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации ферзя.

        Аргументы:
            color (str): Цвет ферзя ('W' или 'B').
        """
        super().__init__(color, 'Q')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для ферзя.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        if (start[0] == end[0] or start[1] == end[1] or abs(start[0] - end[0]) == abs(start[1] - end[1])) and self.is_path_clear(start, end, board):
            return board[end[0]][end[1]] is None or board[end[0]][end[1]].color != self.color
        return False

class King(Unit):
    """
    Класс, представляющий короля.

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации короля.

        Аргументы:
            color (str): Цвет короля ('W' или 'B').
        """
        super().__init__(color, 'K')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для короля.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        if max(abs(start[0] - end[0]), abs(start[1] - end[1])) == 1:
            return board[end[0]][end[1]] is None or board[end[0]][end[1]].color != self.color
        return False

class Spider(Unit):
    """
    Класс, представляющий паука (новая фигура).

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации паука.

        Аргументы:
            color (str): Цвет паука ('W' или 'B').
        """
        super().__init__(color, 'S')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для паука.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        return abs(start[0] - end[0]) <= 2 and abs(start[1] - end[1]) <= 2  # Двигается в радиусе 2 клеток

class Wizard(Unit):
    """
    Класс, представляющий волшебника (новая фигура).

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации волшебника.

        Аргументы:
            color (str): Цвет волшебника ('W' или 'B').
        """
        super().__init__(color, 'W')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для волшебника.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        return (start[0] + start[1]) % 2 == (end[0] + end[1]) % 2  # Может перемещаться только по клеткам одного цвета

class Minotaur(Unit):
    """
    Класс, представляющий минотавра (новая фигура).

    Наследует атрибуты и методы от класса Piece.
    """
    def __init__(self, color):
        """
        Конструктор для инициализации минотавра.

        Аргументы:
            color (str): Цвет минотавра ('W' или 'B').
        """
        super().__init__(color, 'M')

    def is_valid_move(self, start, end, board):
        """
        Проверяет корректность хода для минотавра.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).
            board (list): Шахматная доска (двумерный список).

        Возвращает:
            bool: True, если ход корректен, иначе False.
        """
        return start[0] == end[0] or start[1] == end[1] or abs(start[0] - end[0]) == abs(start[1] - end[1])  # Как ферзь, но через 1 клетку

class Board:
    """
    Класс, представляющий шахматную доску.

    Атрибуты:
        grid (list): Двумерный список, представляющий шахматную доску.
        move_history (list): История ходов.
    """
    def __init__(self):
        """
        Конструктор для инициализации доски и расстановки фигур.
        """
        self.grid = [[None] * 8 for _ in range(8)]
        self.move_history = []
        self.setup_pieces()

    def setup_pieces(self):
        """
        Расставляет фигуры на доске в начальной позиции.
        """
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i in range(8):
            self.grid[1][i] = Pawn('B')
            self.grid[6][i] = Pawn('W')
        for i, piece in enumerate(piece_order):
            self.grid[0][i] = piece('B')
            self.grid[7][i] = piece('W')
        self.grid[0][2] = Spider('B') 
        self.grid[7][2] = Spider('W')
        self.grid[0][5] = Wizard('B')
        self.grid[7][5] = Wizard('W')
        self.grid[3][3] = Minotaur('B')
        self.grid[4][4] = Minotaur('W')

    def display(self, move_count, highlight_moves=None):
        """
        Отображает текущее состояние доски.

        Аргументы:
            move_count (int): Номер текущего хода.
            highlight_moves (list): Список позиций для подсветки доступных ходов.
        """
        print(f"Ход: {move_count}")
        print("  " + " ".join(string.ascii_lowercase[:8]))
        print("  - - - - - - - - ")
        for i in range(8):
            row_display = f"{8 - i}|"
            for j in range(8):
                if highlight_moves and (i, j) in highlight_moves:
                    row_display += "* "  # Подсветка доступных ходов
                else:
                    piece = self.grid[i][j]
                    row_display += (piece.symbol if piece else '. ') + ''  
            print(row_display + f"|{8 - i}")
        print("  - - - - - - - - ")
        print("  " + " ".join(string.ascii_lowercase[:8]))

    def move_piece(self, start, end):
        """
        Перемещает фигуру на доске, если ход корректен.

        Аргументы:
            start (tuple): Начальная позиция (строка, столбец).
            end (tuple): Конечная позиция (строка, столбец).

        Возвращает:
            bool: True, если ход выполнен успешно, иначе False.
        """
        piece = self.grid[start[0]][start[1]]
        if piece and piece.is_valid_move(start, end, self.grid):
            self.move_history.append((start, end, self.grid[end[0]][end[1]])) 
            self.grid[end[0]][end[1]] = piece
            self.grid[start[0]][start[1]] = None
            return True
        return False

    def undo_move(self):
        """
        Отменяет последний ход.

        Возвращает:
            bool: True, если отмена выполнена успешно, иначе False.
        """
        if self.move_history:
            last_move = self.move_history.pop()
            start, end, captured = last_move
            self.grid[start[0]][start[1]] = self.grid[end[0]][end[1]]
            self.grid[end[0]][end[1]] = captured
            return True
        return False

    def get_valid_moves(self, position):
        """
        Возвращает список доступных ходов для фигуры в указанной позиции.

        Аргументы:
            position (tuple): Позиция фигуры (строка, столбец).

        Возвращает:
            list: Список доступных ходов.
        """
        piece = self.grid[position[0]][position[1]]
        if not piece:
            return []
        valid_moves = []
        for r in range(8):
            for c in range(8):
                if piece.is_valid_move(position, (r, c), self.grid):
                    valid_moves.append((r, c))
        return valid_moves

class Game:
    """
    Класс, управляющий шахматной игрой.

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
            move (str): Ввод пользователя (например, 'e2e4' или 'undo').

        Возвращает:
            tuple: Начальная и конечная позиции в виде кортежей (строка, столбец).
        """
        if move == "undo":
            return "undo", None
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
            move = input(f"Ход {'белых' if self.current_turn == 'W' else 'чёрных'} (например, e2-e4 или 'undo'): ")
            move = move.replace("-", "")
            if move == "undo":
                if self.board.undo_move():
                    self.move_count -= 1
                    self.current_turn = 'B' if self.current_turn == 'W' else 'W'
                else:
                    print("Откат невозможен!")
                continue
            start, end = self.parse_input(move)
            if start and end:
                valid_moves = self.board.get_valid_moves(start)
                self.board.display(self.move_count, valid_moves)  # Подсветка ходов
                if self.board.move_piece(start, end):
                    self.move_count += 1
                    self.current_turn = 'B' if self.current_turn == 'W' else 'W'
                else:
                    print("Неверный ход, попробуйте снова.")

if __name__ == "__main__":
    game = Game()
    game.play()
