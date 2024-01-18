import math

# Funktion zur Berechnung des Umfangs
def umfang_kreis(r):
    return 2 * r * math.pi

# Funktion zur Berechnung der Mantelfläche
def mantelflaeche_zylinder(r, h):
    return umfang_kreis(r) * h

# Funktion zur Berechnung der Oberfläche
def oberflaeche_zylinder(r, h):
    return 2 * math.pi * r * (r + h)

# Funktion zur Berechnung des Volumens
def volumen_zylinder(r, h):
    return math.pi * r**2 * h

# Eingabe des Radius und Höhe
r = float(input('Radius des Zylinders in cm: '))
h = float(input('Höhe des Zylinders in cm: '))

# Anzeigen des Ergebnisses
print('\nDie Oberfläche des Zylinders beträgt:', oberflaeche_zylinder(r, h), 'cm²')
print('Die Mantelfläche beträgt:', mantelflaeche_zylinder(r, h), 'cm²')
print('Das Volumen des Zylinders beträgt:', volumen_zylinder(r, h), 'cm³')
