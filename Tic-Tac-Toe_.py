board= [' ' for _ in range(9)]

def show_board():
    print()
    print(f"\t{board[0]} | {board[1]} | {board[2]}")
    print("\t--|---|--")
    print(f"\t{board[3]} | {board[4]} | {board[5]}")
    print("\t--|---|--")
    print(f"\t{board[6]} | {board[7]} | {board[8]}")
    print()
    
def win_check():
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] != ' ':
            return True
    return False
    
def main():
    turn ='X'
    for _ in range(9):
        show_board()
        try:
            move =int(input(f"\nPlayer {turn} enter your move(1-9): "))
        except ValueError:
            move=int(input("\nInvalid move! Please try again. Enter your Move(1-9): "))
        
        if move < 1 or move > 9 or board[move-1] in ['X', 'O']:
            print("\nInvalid move! Please try again.\n")
            continue
        board[move-1]= turn;
        if(win_check()):
            show_board()
            print(f"\nPlayer {turn} wins!")
            return
        if (turn=='X'):
            turn= 'O'
        else:
            turn ='X'
    show_board()
    print("\nIt's Draw!\n") 
    
    
if __name__ =="__main__":
    main()           