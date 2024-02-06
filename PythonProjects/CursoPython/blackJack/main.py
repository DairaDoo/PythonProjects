from art import logo
import random
# List of cards.
cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]

def startingCardsChooser( tempList ):
    global cards
    """This function takes two strating cards for the user cards and computer cards."""
    for i in range( 2 ):
        tempList.append( random.choice( cards ) )
    return tempList
    
def currentScore( someList ):
    """Count all the values from a recieved list and return the total."""
    score = 0
    for value in someList:
        score += value
    return score    

wantToPlay = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")

#conditon for the while loop.
keepPlaying = True

if wantToPlay == 'n':
    keepPlaying = False


userCards = []
computerCards = []

#Add starting cards to computer
startingCardsChooser( userCards )
startingCardsChooser( computerCards )

def start_again():
    """This function starts the game again from zero or ends it."""
    global wantToPlay, userCards, computerCards
    
    wantToPlay = input("\n\nDo you want to play a game of BlackJack? Type 'y' or 'n': ")
    
    if wantToPlay == 'y':
        
        userCards = []
        computerCards = []
        
        startingCardsChooser( userCards )
        startingCardsChooser( computerCards )
        
        return blackJack()
    else:
        print("\nThanks for playing!\n\n")


def blackJack():
    """"Function that contains the game."""
    print( logo )
    global wantToPlay, keepPlaying
    # condition for while loop inside blackjack function.

    
    while keepPlaying:



        #Show starting cards.
        print(f"Your cards: {userCards}, current score: {currentScore(userCards)}")
        print(f"Computer first card: {computerCards[0]}")
        
        

        while currentScore(computerCards) < 17:
            computerCards.append(random.choice(cards))
            
                        
        if currentScore(computerCards) == 21 and currentScore(userCards) < 21:
                print(f"You're final hand: {userCards}, final score: {currentScore(userCards)}")
                print(f"Computer's final hand: {computerCards}, final score: {currentScore(computerCards)}")   
                print("Computer had a blackJack, you lose! :(")
                
        otherCard = input("Type 'y' to get another card, type 'n' to pass: ")

        if otherCard == 'y':
            userCards.append( random.choice( cards ) )
            
            if 11 in userCards and currentScore(userCards) > 21:
                userCards.remove(11)
                userCards.append(1)
            
            elif currentScore( userCards ) > 21:
                print(f"You're final hand: {userCards}, final score: {currentScore(userCards)}")
                print(f"Computer's final hand: {computerCards}, final score: {currentScore(computerCards)}")   
                print("You went over. You lose :(")
                keepPlaying = False
                
        elif otherCard == 'n':
                
            print(f"You're final hand: {userCards}, final score: {currentScore( userCards )}")
            print(f"Computer's final hand: {computerCards}, final score: {currentScore( computerCards )}") 
            
            if currentScore( computerCards ) > 21:
                print("Computer went over. You Win! :)")
                keepPlaying = False  
            
            elif currentScore( userCards ) == currentScore( computerCards ):
                print("It's a draw!")  
                keepPlaying = False
            elif currentScore( userCards ) > currentScore( computerCards ):
                print("You win! :) ")
                keepPlaying = False
            elif currentScore( userCards ) < currentScore( computerCards ):
                print("You lose! Computer wins :( ")
                keepPlaying = False
    start_again()
                 
        
blackJack()
    

