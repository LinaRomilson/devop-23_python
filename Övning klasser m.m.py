import math
from datetime import datetime

class Person:
    def __init__(self, namn, ålder, adress):
        self.namn = namn
        self.ålder = ålder
        self.adress = adress

    def beskrivning(self):
        return f"{self.namn} är {self.ålder} år gammal och bor på {self.adress}"


class Circle:
    def __init__(self, radie):
        self.radie = radie

    def omkrets(self):
        return f"Cirkeln omkrets är {round((self.radie * 2 * math.pi), 4)}"


class BankAccount:
    def __init__(self, kontonummer, saldo):
        self.kontonummer = kontonummer
        self.saldo = saldo

    def insättningar(self, belopp):
        if belopp > 0:
            self.saldo += belopp
            return f"Ditt saldo är {self.saldo} kr"
        else:
            return "Ogiltigt belopp angivet."

    def uttag(self, belopp):
        if belopp > 0 and belopp <= self.saldo:
            self.saldo -= belopp
            return f"Ditt saldo är {self.saldo} kr"

class Employee:
    def __init__(self, namn, löneinformation, anställningsdatum):
        self.namn = namn
        self.löneinformation = löneinformation
        self.anställningsdatum = anställningsdatum

    def år_i_arbete(self):
        idag = datetime.now()
        anställningsår = self.anställningsdatum.year
        nu_år = idag.year
        antal_år = nu_år - anställningsår
        return antal_år

class Student:
    def __init__(self, namn):
        self.namn = namn
        self.betygspoäng = []

    def lägg_till_betyg(self,betygspoäng):
        self.betygspoäng.append(betygspoäng)

    def genomsnittsbetyg(self):
        if len(self.betygspoäng) == 0:
            return 0
        else:
            total = sum(self.betygspoäng)
            antal_betyg = len(self.betygspoäng)
            return total / antal_betyg
# Personbeskrivning
print("----personbeskrivning----".center(25))
person = Person("Lina", 19, "Maltesholmsvägen 154D")
beskrivning_person = person.beskrivning()
print(beskrivning_person)

# Cirkelns omkrets
print("----Cirkelns omkrets----".center(25))
cirkel = Circle(2)
beskrivning_omkrets = cirkel.omkrets()
print(beskrivning_omkrets)

# Insättning av pengar / Uttag av pengar
print("----Bankkonto----".center(25))
konto = BankAccount("12893456", 1000)
print(konto.insättningar(345))
print(konto.uttag(123))

#Anställningstid

anställd   = Employee("Lina", 5000, datetime(2021,12,15))

år_i_arbete = anställd.år_i_arbete()
print(f"{anställd.namn} har varit på företaget i {år_i_arbete} år")

# Genomsnittsbetyg
student = Student("Lina")

student.lägg_till_betyg(82)
student.lägg_till_betyg(98)
student.lägg_till_betyg(100)

genomsnitt = student.genomsnittsbetyg()
print(f"{student.namn}s genomsnittsbetyg: {round(genomsnitt,2)}")