import math

# Funktion zur Berechnung des Durchmessers eines Kreises
def diameter_circle(r):
    return 2 * r

# Funktion zur Berechnung des Umfangs eines Kreises
def circumference_circle(r):
    return 2 * r * math.pi

# Funktion zur Berechnung der Fläche eines Kreises
def area_circle(r):
    return r**2 * math.pi

# Funktion zur Berechnung der Oberfläche
def surface_area_sphere(r):
    return 4 * math.pi * r**2

# Funktion zur Berechnung des Volumens
def volume_sphere(r):
    return (4/3) * math.pi * r**3

# Benutzereingabe für den Radius des Kreises
r = float(input('Radius des Kreises in cm: '))

# Berechnungen für den Kreis
d = diameter_circle(r)
u = circumference_circle(r)
a = area_circle(r)

# Berechnungen für die Kugel
sa = surface_area_sphere(r)
v = volume_sphere(r)

# Ausgabe der Ergebnisse
print('\nDer Durchmesser des Kreises beträgt:', d, 'cm')
print('Der Umfang des Kreises beträgt:', u, 'cm')
print('Die Fläche des Kreises beträgt:', a, 'cm²')
print('Die Oberfläche der Kugel beträgt:', sa, 'cm²')
print('Das Volumen der Kugel beträgt:', v, 'cm³')
