from tic_tac_toe_graphics import *
import time

def BoardClicked(col_index, row_index):
        
        global count
        global markedSquares
        if count >= 10:
                return
        print('BoardClicked col_index:', col_index, 'row_index:', row_index)          
        if count % 2 != 0:           
                #new list containing the inner list
                innerList = markedSquares[col_index]
                #checking to ensure this cell is empty
                if (innerList[row_index]):              
                        i = innerList[row_index]
                        if row_index == 0  and i != 'x' and i != 'o':
                                board.mark_square(col_index, row_index, 'x')
                                innerList[row_index] = 'x'
                                markedSquares[col_index] = innerList
                                board.display_message("It's Player O turn.")
                                count += 1
                                #checking to see if player won: all vertical possibilities checked (x)
                                if markedSquares[0][0] == 'x' and markedSquares[0][1] == 'x' and markedSquares[0][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[1][0] == 'x' and markedSquares[1][1] == 'x' and markedSquares[1][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[2][0] == 'x' and markedSquares[2][1] == 'x' and markedSquares[2][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                #checking to see if player won: all horizontal possibilities checked (x)
                                if markedSquares[0][0] == 'x' and markedSquares[1][0] == 'x' and markedSquares[2][0] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[0][1] == 'x' and markedSquares[1][1] == 'x' and markedSquares[2][1] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[0][2] == 'x' and markedSquares[1][2] == 'x' and markedSquares[2][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                #checking to see if player won: all diagonal possibilities checked (x)
                                if markedSquares[0][0] == 'x' and markedSquares[1][1] == 'x' and markedSquares[2][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[0][2] == 'x' and markedSquares[1][1] == 'x' and markedSquares[2][0] == 'x':
                                        board.display_message("Player X won")
                                        return
                                #checking to see if there is a draw based on the count
                                if count >= 10:
                                        board.display_message("It's a draw :(")
                                        return
                                return
                        elif row_index == 1  and i != 'x' and i != 'o':
                                board.mark_square(col_index, row_index, 'x')
                                innerList[row_index] = 'x'
                                markedSquares[col_index] = innerList
                                board.display_message("It's Player O turn.")
                                count += 1
                                #checking to see if player won: all vertical possibilities checked (x)
                                if markedSquares[0][0] == 'x' and markedSquares[0][1] == 'x' and markedSquares[0][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[1][0] == 'x' and markedSquares[1][1] == 'x' and markedSquares[1][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[2][0] == 'x' and markedSquares[2][1] == 'x' and markedSquares[2][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                #checking to see if player won: all horizontal possibilities checked (x)
                                if markedSquares[0][0] == 'x' and markedSquares[1][0] == 'x' and markedSquares[2][0] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[0][1] == 'x' and markedSquares[1][1] == 'x' and markedSquares[2][1] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[0][2] == 'x' and markedSquares[1][2] == 'x' and markedSquares[2][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                #checking to see if player won: all diagonal possibilities checked (x)
                                if markedSquares[0][0] == 'x' and markedSquares[1][1] == 'x' and markedSquares[2][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[0][2] == 'x' and markedSquares[1][1] == 'x' and markedSquares[2][0] == 'x':
                                        board.display_message("Player X won")
                                        return
                                #checking to see if there is a draw based on the count
                                if count >= 10:
                                        board.display_message("It's a draw :(")                           
                                return
                        elif row_index == 2  and i != 'x' and i != 'o':
                                board.mark_square(col_index, row_index, 'x')
                                innerList[row_index] = 'x'
                                markedSquares[col_index] = innerList
                                board.display_message("It's Player O turn.")
                                count += 1
                                #checking to see if player won: all vertical possibilities checked (x)
                                if markedSquares[0][0] == 'x' and markedSquares[0][1] == 'x' and markedSquares[0][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[1][0] == 'x' and markedSquares[1][1] == 'x' and markedSquares[1][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[2][0] == 'x' and markedSquares[2][1] == 'x' and markedSquares[2][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                #checking to see if player won: all horizontal possibilities checked (x)
                                if markedSquares[0][0] == 'x' and markedSquares[1][0] == 'x' and markedSquares[2][0] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[0][1] == 'x' and markedSquares[1][1] == 'x' and markedSquares[2][1] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[0][2] == 'x' and markedSquares[1][2] == 'x' and markedSquares[2][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                #checking to see if player won: all diagonal possibilities checked (x)
                                if markedSquares[0][0] == 'x' and markedSquares[1][1] == 'x' and markedSquares[2][2] == 'x':
                                        board.display_message("Player X won")
                                        return
                                elif markedSquares[0][2] == 'x' and markedSquares[1][1] == 'x' and markedSquares[2][0] == 'x':
                                        board.display_message("Player X won")
                                        return
                                #checking to see if there is a draw based on the count
                                if count >= 10:
                                        board.display_message("It's a draw :(")  
                                return
                        
                        board.display_message("Player X Click again.")
                                

                        
                        
                
        else:
                #new list containing the inner list
                innerList = markedSquares[col_index]
                if (innerList[row_index]):              
                        i = innerList[row_index]
                        if row_index == 0 and i != 'x' and i != 'o':
                                board.mark_square(col_index, row_index, 'o')
                                innerList[row_index] = 'o'
                                markedSquares[col_index] = innerList
                                board.display_message("It's Player X turn.")
                                count += 1
                                #checking to see if player won: all vertical possibilities checked (o)
                                if markedSquares[0][0] == 'o' and markedSquares[0][1] == 'o' and markedSquares[0][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[1][0] == 'o' and markedSquares[1][1] == 'o' and markedSquares[1][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[2][0] == 'o' and markedSquares[2][1] == 'o' and markedSquares[2][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                #checking to see if player won: all horizontal possibilities checked (o)
                                if markedSquares[0][0] == 'o' and markedSquares[1][0] == 'o' and markedSquares[2][0] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[0][1] == 'o' and markedSquares[1][1] == 'o' and markedSquares[2][1] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[0][2] == 'o' and markedSquares[1][2] == 'o' and markedSquares[2][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                #checking to see if player won: all diagonal possibilities checked (o)
                                if markedSquares[0][0] == 'o' and markedSquares[1][1] == 'o' and markedSquares[2][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[0][2] == 'o' and markedSquares[1][1] == 'o' and markedSquares[2][0] == 'o':
                                        board.display_message("Player O won")
                                        return
                                #checking to see if there is a draw based on the count
                                if count >= 10:
                                        board.display_message("It's a draw :(")  
                                return
                        elif row_index == 1  and i != 'x' and i != 'o':
                                board.mark_square(col_index, row_index, 'o')
                                innerList[row_index] = 'o'
                                markedSquares[col_index] = innerList
                                board.display_message("It's Player X turn.")
                                #checking to see if player won: all vertical possibilities checked (o)
                                if markedSquares[0][0] == 'o' and markedSquares[0][1] == 'o' and markedSquares[0][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[1][0] == 'o' and markedSquares[1][1] == 'o' and markedSquares[1][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[2][0] == 'o' and markedSquares[2][1] == 'o' and markedSquares[2][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                #checking to see if player won: all horizontal possibilities checked (o)
                                if markedSquares[0][0] == 'o' and markedSquares[1][0] == 'o' and markedSquares[2][0] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[0][1] == 'o' and markedSquares[1][1] == 'o' and markedSquares[2][1] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[0][2] == 'o' and markedSquares[1][2] == 'o' and markedSquares[2][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                #checking to see if player won: all diagonal possibilities checked (o)
                                if markedSquares[0][0] == 'o' and markedSquares[1][1] == 'o' and markedSquares[2][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[0][2] == 'o' and markedSquares[1][1] == 'o' and markedSquares[2][0] == 'o':
                                        board.display_message("Player O won")
                                        return
                                #checking to see if there is a draw based on the count
                                if count >= 10:
                                        board.display_message("It's a draw :(")  
                                count += 1
                                return
                        elif row_index == 2  and i != 'x' and i != 'o':
                                board.mark_square(col_index, row_index, 'o')
                                innerList[row_index] = 'o'
                                markedSquares[col_index] = innerList
                                board.display_message("It's Player X turn.")
                                count += 1
                                #checking to see if player won: all vertical possibilities checked (o)
                                if markedSquares[0][0] == 'o' and markedSquares[0][1] == 'o' and markedSquares[0][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[1][0] == 'o' and markedSquares[1][1] == 'o' and markedSquares[1][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[2][0] == 'o' and markedSquares[2][1] == 'o' and markedSquares[2][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                #checking to see if player won: all horizontal possibilities checked (o)
                                if markedSquares[0][0] == 'o' and markedSquares[1][0] == 'o' and markedSquares[2][0] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[0][1] == 'o' and markedSquares[1][1] == 'o' and markedSquares[2][1] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[0][2] == 'o' and markedSquares[1][2] == 'o' and markedSquares[2][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                #checking to see if player won: all diagonal possibilities checked (o)
                                if markedSquares[0][0] == 'o' and markedSquares[1][1] == 'o' and markedSquares[2][2] == 'o':
                                        board.display_message("Player O won")
                                        return
                                elif markedSquares[0][2] == 'o' and markedSquares[1][1] == 'o' and markedSquares[2][0] == 'o':
                                        board.display_message("Player O won")
                                        return
                                #checking to see if there is a draw based on the count 
                                if count >= 10:
                                        board.display_message("It's a draw :(")  
                                return
                        board.display_message("Player O Click again.")
                   
board = TicTacToeBoard(3, 3, BoardClicked)


board.display_message("Player X click to get started.")
global count
count = 1

global markedSquares
markedSquares = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

                


# Make sure mainloop() is the last line of code in this program!
mainloop()



