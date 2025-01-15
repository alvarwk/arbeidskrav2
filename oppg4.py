
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

land = input("Skriv inn et land: ").title()

info = data.get(land)
hovedstad, befolkning = info
print(f'{info[0]} er hovedstaden i {land} og det er {befolkning} mill. innbyggere i {hovedstad}')

nytt_land = input("Skriv inn et nytt land: ").title()
hovedstad = input(f"Hva er hovedstaden til {nytt_land}? ").title()
innbyggere = input(f'Hvor mange innbyggere er det i {hovedstad} i millioner? ').title()

data.update({nytt_land: [hovedstad, innbyggere]})
print(data)