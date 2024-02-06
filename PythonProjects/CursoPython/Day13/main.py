############DEBUGGING#####################

# Describe Problem
# Si el ultimo valor del range se queda en 20, ejecuta hasta el 19 y por lo tanto, nunca se cumple la condición, se resuelve cambiando el 20 a 21.
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# El original era randint(1,6), cambie los dos valores ya que el rango incluye ambos, el valor izquierdo y derecho, y la lista comienza en 0, teniendo 5 elementos de 0 a 5.
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
def mutate( a_list ) :
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append( new_item )
  print(b_list)

mutate([1,2,3,5,8,13])