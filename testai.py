# Pasiimti anksčiau sukurtą programos kodą (4 paskaita "Funkcijos")
# • Funkcijas perdaryti taip, kad jos gražintų duomenis
# • Sukurti UNIT testą visoms funkcijoms
# • Kiekvienai funkcijai turi būti mažiausiai 3 patikrinimai
# • Maksimaliai patobulinti kodą, nuolatos leidžiant sukurtą UNIT testą
# 1. Gražinti trijų paduotų skaičių sumą.
def skaiciu_suma(sk1, sk2, sk3):
    return sk1 + sk2 + sk3
#print(skaiciu_suma(45, 5, 6))
# 2. Gražintų paduoto sąrašo iš skaičių, sumą.
def saraso_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius
    return suma
sarasas = [4, 5, 78, 8]
#print(saraso_suma(sarasas))
# 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
def didziausias_skaicius(*args):
    return max(args)
#print(didziausias_skaicius(5, 8, 789, 94, 78))

#output
Process finished with exit code 0
