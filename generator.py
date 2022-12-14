import random

lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&_-()=%*:/!?+."

combination = lower_letters + upper_letters + numbers + symbols
length = int(input('¿De cuántos caracteres quieres que sea tu contraseña? \n > '))
password = "".join(random.sample(combination, length))

print("Tu contraseña será:", password)
