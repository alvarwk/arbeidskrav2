import math

antall_elever = int(input('Skriv inn antall elever:' ))
antall_pizzaer = math.ceil(antall_elever / 4)

print(f'Det må handles inn {antall_pizzaer} pizzaer til festen')

