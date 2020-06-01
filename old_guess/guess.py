import random
NB_ESSAIS_MAX = 5
bottom = 0
top = 100
secret = random.randint(bottom,top)
print("Essayez de deviner le nombre secret !")
count = 0
win = 0
for i in range(NB_ESSAIS_MAX):
    if count < NB_ESSAIS_MAX and win < 1:
        count +=1
        x = int(input("Entrez un nombre entre {} et {}: ".format(bottom,top)))
        if x == secret:
            win += 1
            print("Gagné en",count,"essais !")
        elif x < secret:
            if count == NB_ESSAIS_MAX:
                print("Perdu ! Le nombre secret était", secret)
            else:
                print("Trop petit ! ")
                print("Il vous reste",NB_ESSAIS_MAX-i-1,"essais")
                bottom = x
        elif x > secret:
            if count == NB_ESSAIS_MAX:
                print("Perdu ! Le nombre secret était", secret)
            else:
                print("Trop grand ! ")
                print("Il vous reste",NB_ESSAIS_MAX-i-1,"essais")
                top = x

fin = input()
