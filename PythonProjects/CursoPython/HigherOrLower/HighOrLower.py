from gameData import data, logo, vs
import random # usamos el random para elegir elementos aleatorios a la hora de comparar.


def HighOrLowerGame():
    # variable para matener el juego activo usando un while.
    stillAlive = True

    # Mantenemos un conteo de las correctas del usuario.
    score = 0

    # variable para almacenar la primera opción a comparar.
    option1 = random.choice(data)

    print(logo)

    while stillAlive:
        # variable para almacenar la segunda opción a comparar.
        option2 = random.choice(data)
        # valor a escoger por el usuario
        print(f"Compare A: {option1['name']}, a {option1['description']}, from {option1['country']}. \n{vs}")

        # variable para almacenar la opción de la comparación que entrará el usuario.
        userChoice = input(f"Against B: {option2['name']}, a {option2['description']}, from {option2['country']}.\nWho has more followers? Type 'A' or 'B': ").upper()

        if option1 == option2: # If para prevenir errores, en caso de que ambas opciones sean iguales.
            option2 = random.choice(data)
            continue

        elif option1['follower_count'] < option2['follower_count'] and userChoice == 'a': # si la opcion 1 es menor
            print(f"Sorry that's wrong. Final score {score}.")
            return

        elif option2['follower_count'] < option1['follower_count']:  # si la opcion 2 es menor
            print(f"Sorry that's wrong. Final score {score}.")
            return

        elif option1['follower_count'] > option2['follower_count']: # si la opcion 1 es mayor
            score += 1
            print(logo)
            print(f"You're right! Current Score: {score}.")
            option2 = option1
            continue

        elif option2['follower_count'] > option1['follower_count']: # si la opcion 2 es mayor
            score += 1
            print(logo)
            option1 = option2
            print(f"You're right! Current Score: {score}.")
            continue
        else: # acepta cualquier valor distinto a A o B.
            print(f"Sorry that's wrong. Final Score {score}")


HighOrLowerGame() # LLamamos al juego, ya que este lo pusimos adentro de una función.








