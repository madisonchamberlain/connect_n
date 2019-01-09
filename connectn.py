#Make empty board
def make_board(num_rows: int, num_cols: int, blank_char: str) -> list:
    board = []
    for row_number in range(num_rows):
        row = [blank_char] * num_cols
        board.append(row)
    return board

def display_game_state(board: list) -> None:
    print(end=' ')
    for col_num in range(len(board[0])):
        print(col_num, end=' ' * 3)
    print()
    for row_num, row in reversed(list(enumerate(board))):
        print(row_num, end=' ')
        row_image = (' '.join(row))
        print(row_image)
    #return row_image

def display_game_state_two(board: list) -> str :
    for row_num, row in reversed(list(enumerate(board))):
        row_image = ('   '.join(row))
        return row_image

def fill(board: list) -> int:
    for row_num, row in enumerate(board):
        row_number = row_num

def row_win(iterable,n, blank_char: str) -> bool:
    matches = 0

    for element in iterable:
        for char in element:
            if char != blank_char and char != ' ':
                if char == iterable[iterable.index(char)]:
                    index = iterable.index(element) + 1
                    while char == iterable[index]:
                        matches +=1
                        index += 1
                        if matches == n:
                            return True
                        else:
                            return False
        return

def column_win(num_rows: int, num_cols: int, blank_char: str, n: int,col_check: int) -> bool:
    col_check -= 1
    board = make_board(num_rows, num_cols, blank_char)
    col_string = []
    row = board[0]
    for row in board:
        for index in row:
            char = row[col_check]
        col_string.append(char)

    if row_win(col_string, n, blank_char):
        return True


def right_diag_win(num_rows: int, num_cols: int, blank_char: str, n: int) -> bool:
    board = make_board(num_rows, num_cols, blank_char)
    diag_list = []
    index = 0
    if num_rows != num_cols:
        return False
    else:
        for pos, row in enumerate(board):
            diag_char = board[pos][index]
            diag_list.append(diag_char)
            index += 1
    if row_win(diag_list,n, blank_char):
        return True
    else:
        return False

def get_player_attributes():
    while True:
        row = is_valid_board_input('Enter the number of rows: ')
        row = int(row)
        cols = is_valid_board_input('Enter the number of columns: ')
        cols = int(cols)
        n = is_valid_board_input('Enter the number of pieces in a row to win: ')
        n = int(n)
        return (row, cols, n)

def is_valid_board_input(prompt):
   inp = input(prompt).strip()
   while (not inp.isdigit()) or (inp.isdigit() and inp == 0):
       inp = input(prompt).strip()
   if inp.isdigit() and inp != 0:
       inp = inp
   return inp

def make_board(num_rows: int, num_cols: int, blank_char: str) -> list:
    board = []
    for row_number in range(num_rows):
        row = [blank_char] * num_cols
        board.append(row)
    return board

def display_game_state(board: list) -> None:
    print(end='  ')
    for col_num in range(len(board[0])):
        print(col_num, end=' ' * 3)
    print()
    for row_num, row in reversed(list(enumerate(board))):
        print(row_num, end=' ')
        row_image = ('   '.join(row))
        print(row_image)

def is_valid_move(col_choice, amount_of_cols_specified,  amount_of_rows_specified, board):
    if col_choice.isdigit():
        if int(col_choice) >= 0 and int(col_choice) < amount_of_cols_specified:
            if not board[int(amount_of_rows_specified)-1][int(col_choice)] != '*':
                return True
    else:
        return False

def get_player_move(cols,rows, board, blank_char):
    player_move = input('Enter the column you want to play in: ').strip()
    while not is_valid_move(player_move, cols, rows, board):
        player_move = input('Enter the column you want to play in: ').strip()
    move = int(player_move)
    for i in range(rows):
        if board[i][move] == blank_char:
            #update_game_state()
            row_to_return = i
            return [row_to_return,move]

def tie_game_check(board):
    star_count = 0
    for row in board:
        for col in row:
            if board[board.index(row)][row.index(col)] == "*":
                star_count += 1
    if star_count == 0:
        display_game_state(board)
        print("Tie Game")
        return True
    else:
        return False


def row_win(row, col, n, board):
      sum_left = 0
      sum_right = 0
      player = board[row][col]
      for currCol in range(col+1, len(board)):
          if board[row][currCol] == player:
              sum_right += 1
          else:
              break
      for currCol in range(col-1, 0, -1):
          if board[row][currCol] == player:
              sum_right += 1
          else:
              break
      if sum_left + sum_right + 1 >= n:
          if player == "X":
            display_game_state(board)
            print('Player 1 won!')
          else:
            display_game_state(board)
            print('Player 2 won!')
          return True
      return False


def col_win(row, col, n, board):
    sum_left = 0
    sum_right = 0
    player = board[row][col]
    for currRow in range(row + 1, len(board)):
        if board[currRow][col] == player:
            sum_right += 1
        else:
            break
    for currRow in range(row - 1, 0, -1):
        if board[currRow][col] == player:
            sum_right += 1
        else:
            break
    if sum_left + sum_right + 1 >= n:
        if player == "X":
            display_game_state(board)
            print('Player 1 won!')
        else:
            display_game_state(board)
            print('Player 2 won!')
        return True
    return False

def change_turn(turn: int):
    if turn == 0:
        return 1
    elif turn == 1:
        return 0

def update_game_state(piece: str, rows, cols, board) -> list:
   board[rows][cols] = piece
   return board

def play_game():
    player_attributes = get_player_attributes()
    rows = player_attributes[0]
    cols = player_attributes[1]
    n = player_attributes[2]
    board = make_board(rows, cols, "*")
    blank_char = '*'
    player_turn = 0

    while True:
        display_game_state(board)
        everything_to_return = get_player_move(cols, rows, board,blank_char)
        row_to_return = everything_to_return[0]
        column_to_return = everything_to_return[1]
        pieces = 'XO'
        update_game_state(pieces[player_turn], row_to_return, column_to_return, board)
        if tie_game_check(board):
            return False
        if row_win(row_to_return, column_to_return, n, board):
            return False
        if col_win(row_to_return, column_to_return, n, board):
            return False
        player_turn = change_turn(player_turn)

def main():
    play_game()

main()
