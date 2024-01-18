# Funktion zur Berechnung der Oberfläche eines Würfels
def oberflaeche_wuerfel(a, b, h):
    return 2 * (a*b + b*h + a*h)

# Funktion zur Berechnung des Volumens eines Würfels
def volumen_wuerfel(a, b, h):
    return a * b * h

# Benutzereingabe für die Abmessungen des Würfels
a = float(input('Seitenlänge des Würfels in cm: '))
b = float(input('Breite des Würfels in cm: '))
h = float(input('Höhe des Würfels in cm: '))

# Ausgabe der Ergebnisse ohne Rundung
print('\nDie Oberfläche des Würfels beträgt:', oberflaeche_wuerfel(a, b, h), 'cm²')
print('Das Volumen des Würfels beträgt:', volumen_wuerfel(a, b, h), 'cm³')
