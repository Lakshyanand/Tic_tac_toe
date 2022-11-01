import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])

p1s='X'
p2s='O'

def play():
    for turn in range(9):
        if(turn%2==0):
            print("X's turn")
            place(p1s)
            if(win(p1s)==True):
                break
        else:
            print("O's turn")
            place(p2s)
            if(win(p2s)==True):
                break
    if not(win(p1s)) and not(win(p2s)):
        print("DRAW")
    
def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("enter row 1,2 or 3"))
        col=int(input("enter col 1,2 or 3"))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            break
        else:
            print("invalid input,please re-enter..")
    board[row-1][col-1]=symbol

def win(symbol):
    return check_row(symbol) or check_col(symbol) or check_diagonal(symbol)

def check_row(symbol):
    for row in range(3):
        count=0
        for col in range(3):
            if(board[row][col]==symbol):
                count=count+1
        if(count==3):
            print(symbol,"won")
            return True

def check_col(symbol):
    for col in range(3):
        count=0
        for row in range(3):
            if(board[row][col]==symbol):
                count=count+1
        if(count==3):
            print(symbol,"won")
            return True

def check_diagonal(symbol):
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol):
        print(symbol,"won")
        return True
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol):
        print(symbol,"won")
        return True

play()