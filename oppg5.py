import numpy as np

def halvsirkel_omkrets(a):
    return np.pi * (a / 2)

def omkrets_rettvinklet_trekant(katet_a, katet_b):
    hypotenus = np.sqrt(katet_a ** 2 + katet_b ** 2)
    # Skal ikke ha med katet A pga halvsirkelen
    return  katet_b + hypotenus


def halvsirkel_areal(a):
    return (np.pi * a ** 2) / 8

def trekant_areal(a, b):
    return (a * b) / 2


def beregn_areal_figur(a, b):
    areal = trekant_areal(a, b) + halvsirkel_areal(a)
    return f"Areal av figuren er {areal:.2f}"

def beregn_omkrets_figur(a, b):
    omkrets = omkrets_rettvinklet_trekant(a, b) + halvsirkel_omkrets(a)
    return f"'Ytre omkrets' av figuren er {omkrets:.2f}"

a = float(input("Skriv inn lengden a: "))
b = float(input("Skriv inn lengden b: "))

areal_resultat = beregn_areal_figur(a, b)
omkrets_resultat = beregn_omkrets_figur(a, b)

print(areal_resultat)
print(omkrets_resultat)