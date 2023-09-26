valore1 = input("Inserisci il primo valore: ")
valore2 = input("Inserisci il secondo valore: ")

if valore1.isnumeric() and valore2.isnumeric():
    risultato = int(valore1) * int(valore2)
    print("Il risultato della moltiplicazione è:", risultato)
elif valore1.isalpha() and valore2.isalpha():
    risultato = valore1 + valore2
    print("La concatenazione delle stringhe è:", risultato)
else:
    print("PESTO MISTO")
