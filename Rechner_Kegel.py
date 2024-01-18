import math

# Funktion zur Berechnung des Kegelvolumens
def kegel_volumen(radius, hoehe):
    return (1/3) * math.pi * radius**2 * hoehe

# Funktion zur Berechnung der Mantellinie des Kegels
def kegel_mantellinie(radius, hoehe):
    return math.sqrt(hoehe**2 + radius**2)

# Funktion zur Berechnung des Umfangs der Grundfläche des Kegels
def kegel_umfang(radius):
    return 2 * math.pi * radius

# Funktion zur Berechnung der Grundfläche des Kegels
def kegel_grundflaeche(radius):
    return math.pi * radius**2

# Funktion zur Berechnung der Mantelfläche des Kegels
def kegel_mantelflaeche(radius, mantellinie):
    return math.pi * radius * mantellinie

# Funktion zur Berechnung der Oberfläche des Kegels
def kegel_oberflaeche(radius, mantellinie):
    return kegel_grundflaeche(radius) + kegel_mantelflaeche(radius, mantellinie)

def main():
    # Benutzereingabe für den Radius und die Höhe des Kegels
    radius = float(input("Radius des Kegels in cm: "))
    hoehe = float(input("Höhe des Kegels in cm: "))

    # Berechnung verschiedener Eigenschaften
    volumen = kegel_volumen(radius, hoehe)
    mantellinie = kegel_mantellinie(radius, hoehe)
    umfang = kegel_umfang(radius)
    grundflaeche = kegel_grundflaeche(radius)
    mantelflaeche = kegel_mantelflaeche(radius, mantellinie)
    oberflaeche = kegel_oberflaeche(radius, mantellinie)

    # Ausgabe der Werte
    print(f"Volumen des Kegels: {volumen} cm³")
    print(f"Mantellinie des Kegels: {mantellinie} cm")
    print(f"Umfang der Grundfläche: {umfang} cm")
    print(f"Grundfläche des Kegels: {grundflaeche} cm²")
    print(f"Mantelfläche des Kegels: {mantelflaeche} cm²")
    print(f"Oberfläche des Kegels: {oberflaeche} cm²")

if __name__ == "__main__":
    main()
