# A simple program to average two exam scores.
# Illustrates the use of mulitple inputs.
def main():
    print("This program computes the average of two exam scores:")
    
    input_str = input("Enter two scores separated by a comma: ")
    
    # split the input string at the comma to get separate score strings.
    score1, score2 = input_str.split(',') # Cada vez que el programa lee una coma o cualquier simbolo, los separa a dos valores distintos.
    
    score1 = float(score1)
    score2 = float(score2)
    
    #Calcultate de average
    average = (score1 / score2) / 2.0
    
    print(f"The average of the score is: {average}")
    

main()