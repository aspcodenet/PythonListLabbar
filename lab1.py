#Skapa ett program där användaren får upp fyra frågor om att mata in ett tal. Spara
#alla talen i en lista. Loopa igenom lista och ta fram det tal som är störst. Skriv
#tillbaka resultatet på skärmen för användaren

talLista = []

for i in range(4):
    tal = int(input(f"Mata in tal {i+1}"))
    talLista.append(tal)

largestSoFar = 0
for i in talLista:
    if i > largestSoFar:
        largestSoFar = i



# for index in range(len(talLista)):
#     talet = talLista[index]

print(f"Största = {largestSoFar}")
