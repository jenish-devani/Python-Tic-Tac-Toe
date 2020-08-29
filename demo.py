


from IPython.display import clear_output
import random

def choosefirst():

    flip=random.randint(0,1)

    if flip==0:
        return 'Player 1';
    else:
        return 'Player 2';

def spaceckeck(bord,position):

    if bord[position]==' ':
        return True;
    else:
        return False;

def fullboardcheck(bord):

    for i in range(1,10):
        if spaceckeck(bord,i):
            return False;

    return True;

def playerchoice(bord):

    position=0;

    while position not in [1,2,3,4,5,6,7,8,9] or spaceckeck(bord,position):

        position=int(input(turn+" Enter the Position in (1-9): "))

        return position;


def playerinput():
    mark=''

    while mark!='X' and mark!='O':
        mark=input("Player 1 enter your mark 'O' or 'X': ").upper()

    if(mark=='X'):
        return ('X','O')
    else:
        return ('O','X')

def placemark(bord,mark,position):

    bord[position]=mark

def wincheck(bord,mark):

    if(bord[1] == bord[2] == bord[3] == mark or
    bord[4] == bord[5] == bord[6] == mark or
    bord[7] == bord[8] == bord[9] == mark or
    bord[1] == bord[4] == bord[7] == mark or
    bord[2] == bord[5] == bord[8] == mark or
    bord[3] == bord[6] == bord[8] == mark or
    bord[1] == bord[5] == bord[9] == mark or
    bord[3] == bord[5] == bord[7] == mark ):
        return True;


def replay():

    ans=str(input("Want to play again? Y or N").upper())

    if ans=='Y':
        return True;
    else:
        return False;


def printbord(bord):

    clear_output()
    for i in range(1,10,3):
        print(str(bord[i])+" | "+str(bord[i+1])+" | "+str(bord[i+2]))



print("***** Welcome to Tic TAC Toi Game *****")

while True:

    bord = [' ']*10
    p1_mark, p2_mark = playerinput()
    turn=choosefirst()
    print(turn+" plays first")

    playgame=input("Ready to play? Y or N").upper()

    if playgame=='Y':
        game_on=True;
    else:
        game_on=False;

    while game_on:

        if turn=='Player 1':
            printbord(bord)
            position=playerchoice(bord)
            placemark(bord,p1_mark,position)

            if(wincheck(bord,p1_mark)):
                printbord(bord)
                print("Player 1 Win !!")
                game_on=False;
            else:
                if fullboardcheck(bord):
                    printbord(bord)
                    print("Game Tie !!")
                    game_on=False;
                else:
                    turn='Player 2'
        else:
            printbord(bord)
            position = playerchoice(bord)
            placemark(bord, p2_mark, position)

            if (wincheck(bord, p2_mark)):
                printbord(bord)
                print("Player 2 Win !!")
                game_on = False;
            else:
                if fullboardcheck(bord):
                    printbord(bord)
                    print("Game Tie !!")
                    game_on = False;
                else:
                    turn = 'Player 1'


    if not replay():
        break;