def check_win(a):
  if((a[0][0]==a[1][1]==a[2][2]) and (a[0][0]=='X' or a[0][0]=='O')):
       return 1
  elif((a[0][0]==a[1][0]==a[2][0]) and (a[0][0]=='X' or a[0][0]=='O')):
       return 1
  elif ((a[0][1]==a[1][1]==a[2][1]) and (a[0][1]=='X' or a[0][1]=='O')):
        return 1
  elif ((a[0][2]==a[1][2]==a[2][2]) and (a[0][2]=='X' or a[0][2]=='O')):
       return 1
  elif((a[0][0]==a[0][1]==a[0][2]) and (a[0][0]=='X' or a[0][0]=='O')):
       return 1
  elif ((a[1][0]==a[1][1]==a[1][2]) and (a[1][0]=='X' or a[1][0]=='O')):
       return 1
  elif ((a[2][0]==a[2][1]==a[2][2]) and (a[2][0]=='X' or a[2][0]=='O')):
       return 1
  elif((a[0][2]==a[1][1]==a[2][0]) and (a[0][2]=='X' or a[0][2]=='O')):
       return 1
  else:
      return 0
def check_draw(a):
    draw=True
    for i in [0,1,2]:
        for j in [0,1,2]:
            if(a[i][j]==' '):
                draw=False
    return draw
def print_rows(array_2D):
    for i in range(0, len(array_2D)):
        for j in range(0, 3):
            print(array_2D[i][j], end="     ")
        print("\n")

from IPython.display import clear_output
re_game=True
while(re_game):
 print("Welcome, Let's Play Tic Tac Toe")
 array_2D = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
 game_on = True
 dict={}
 name_1=input("Enter Player 1 name: ")
 name_2=input("Enter Player 2 name: ")
 dict[1]=name_1
 dict[2]=name_2
 a = 1
 while (game_on):
     row,column = input(f"Enter Input, {dict[a]}  : ").split()
     clear_output()
     row = int(row)
     column = int(column)
     row -= 1
     column -= 1
     if(array_2D[row][column]=='X' or array_2D[row][column]=='O'):
         print("You cannot enter value here")
         continue
     if a == 1:
         array_2D[row][column] = 'X'
     else:
         array_2D[row][column] = 'O'
     print_rows(array_2D)
     victory = check_win(array_2D)
     if victory==1:
         print(f"{dict[a]} has won \n")
         play_again=input("Do you want to play again? Yes or No ").upper().startswith('YES')
         if play_again:
             break
         else:
             game_on = False
             re_game = False
     draw= check_draw(array_2D)
     if draw==True:
         print("It is a draw \n")
         play_again = input("Do you want to play again? Yes or No ").upper().startswith('YES')
         if play_again:
             break
         else:
             game_on = False
             re_game = False
     a = 3 - a

