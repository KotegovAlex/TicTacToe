from pathlib import Path

GAME_TITLE = 'Tic-Tac-Toe Game'

RULES_TITLE = 'Правила игры'

RULES_CONTENT = '''    Игроки по очереди ставят на свободные клетки
поля 3×3 знаки (один всегда крестики, другой 
всегда нолики). 
    
    Первый, выстроивший в ряд 3 своих фигуры по 
вертикали, горизонтали или диагонали, выигрывает. 
    
    Первый ход делает игрок, ставящий крестики.
    '''

START_BTN_TEXT = 'Начало игры'

EXIT_BTN_TEXT = 'Выход'

REFRESH_BTN_TEXT = 'Заново'

CROSS_WIN = 'Победил КРЕСТИК!'

ZERO_WIN = 'Победил НОЛИК!'

NO_ONE = 'Игра окончена, НИЧЬЯ!'

WINDOW_WIDTH = 550

WINDOW_HEIGHT = 550

BACK_IMG_PATH = Path(r"content\tic_tac_back.png")
