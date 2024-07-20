print("welcome to TIC-TAC-TOE game!")
board=["-","-","-","-","-","-","-","-","-"]

current_player="X"
game_winner= None
game_running=True
#printing the game board
def print_board(board):
    print(board[0]  + " | " +  board[1] + " | " +  board[2])
    print("--|---|--")
    print(board[3]  + " | " +  board[4] + " | " +  board[5])
    print("--|---|--")
    print(board[6]  + " | " +  board[7] + " | " +  board[8])

def player_input(board):
   val=int(input("enter any value from 0-9: "))
   if val>=1 and val<=9 and board[val-1]=="-":
      board[val-1]=current_player
   else:
      print("oops! That place is already occupied!")

def chck_horizontal(board):
   global winner
   if board[0]==board[1]==board[2] and board[1]!="-":
      winner=board[0]
      return True
   elif (board[3]==board[4]==board[5] and board[4]!="-"):
      winner=board[3]
      return True
   elif (board[6]==board[7]==board[8] and board[7]!="-"):
      winner=board[6]   
      return True

def chck_row(board):
   global winner
   if board[0]==board[3]==board[6] and board[3]!="-":
      winner=board[0]
      return True
   elif board[1]==board[4]==board[7] and board[4]!="-":
      winner=board[1]
      return True
   elif board[2]==board[5]==board[8] and board[5]!="-":  
      winner=board[2]
      return True
def chck_diagonal(board):
   global winner
   if board[0]==board[4]==board[8] and board[4]!="-":
      winner=board[0]
      return True
   elif board[2]==board[4]==board[6] and board[4]!="-":
      winner=board[2]
      return True
#to check its a tie!
def chck_tie(baord):
   global game_running
   if "-" not in board:
      print_board
      print("its a tie!!")
      game_running=False

#to check who wins the game!
def chck_win():
   global game_running
   if chck_horizontal(board) or chck_row(board) or chck_diagonal(board):
      print(f"the winner is {winner}")
      print_board(board)
      game_running=False
#to switch player!
def switch_player():
   global current_player
   if current_player=="X":
      current_player="O"
   else:
      current_player="X"

while game_running:
   print_board(board)
   player_input(board)
   chck_win()
   chck_tie(board)
   switch_player()
   
print("___GAME OVER___")
   



      