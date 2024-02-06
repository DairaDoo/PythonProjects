# convert.py
# A program to convert Celsius to Fahrenheit.

def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = (9.0 / 5.0) * celsius + 32
    print(f"The temperature is {fahrenheit} degrees Fahrenheit.")


main()
