import math

# Welcome message
print("Willkommen beim TIP-Löser für quadratische Gleichungen")

int_a = float(input("Gib einen Wert für a ein: "))
int_b = float(input("Gib einen Wert für b ein: "))
int_c = float(input("Gib einen Wert für c ein: "))
int_Diskr = (int_b**2) - (4 * int_a * int_c) # Berechnung der Diskriminanten
int_x1 = round((-int_b - math.sqrt((int_b**2) - (4*int_a*int_c))) / (2 * int_a), 2) # Berechnung von x1
int_x2 = round((-int_b + math.sqrt((int_b**2) - (4*int_a*int_c))) / (2 * int_a), 2)# Berechnung von x2
# Zeigt die Eingaben nochmals:
print("\n")
print("=================================")
print("Deine Eingaben:\n" + "a = " + str(int_a) + ", " + "b = " + str(int_b) + ", " + "c = " + str(int_c))
# Zeigt die Lösungen:
print("\n")
print("=================================")
print("Daraus ergeben sich folgende Lösungen: ")
print("Diskriminante D = " + str(int_Diskr))
print("Lösung x_1 = " + str(int_x1))
print("Lösung x_2 = " + str(int_x2))
# Goodbye message
print("\n")
print("=================================")
print("Das wars, bis bald!")