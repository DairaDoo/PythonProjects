#scope
enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
# print(potion_strength)


#Globaal Scope

# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
        
#     drink_potion()
    
# game()


# game_level = 3

# Example if an if a variable is declared inside a function, then it is a local scope, it belongs only to the function, if it is declared in a while loop or if statement, its not considered local, it is global.
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemies = enemies[0]
# print(new_enemies)

# Modifying Global Scope

# enemies = "Skeleton" # Global variable.

# def increase_enemies():
#     enemies = "Zombie" # local scope variable, it belongs to the function.
#     print(f"Enemies inside function: {enemies}")
    
# increase_enemies()
# print(f"Enemies inside function: {enemies}")




enemies = 1

# def increase_enemies():
#     """primera forma de hacerlo menos eficiente."""
#     global enemies
#     enemies += 1
#     print(f"Enemies inside function 1: {enemies}")
# increase_enemies()
# print(f"Enemies inside function 1: {enemies}")


def increase_enemies2():
    """"Manera más eficiente de hacerlo"""
    print(f"Enemies inside function 2: {enemies}")
    return enemies + 1
enemies = increase_enemies2() # increase_enemies se convierte en dos, ya que enemies es global, la podemos llamar desde la funcion.
print(f"Enemies inside function 2: {enemies}")
    