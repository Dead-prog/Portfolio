
import random

with open("mots_pendu.txt", "r") as f:
    mots = f.read().splitlines()


word = random.choice(mots)

display = ""

lucky = 6

word_found = []

print("Bienvenue dans mon jeux du pendu: vous disposerez de 6 vie si votre score de vie attein zero \n vous avez perdue vous pourez proposer un mot toute les 3 lettre trouver \n s'il est faux vous perdrez 2 vie sinon c'est gagner.")
print("Les accents ne sont pas comptée. \n")

while lucky > 0:
    
    letter = str(input("Entrer une lettre: "))

    if letter not in word:
        lucky -= 1
        print(f'il vous reste {lucky} chance')
    else:
        for i in word:
            if i == letter:
                if i in word_found:
                    pass
                else:
                    word_found.append(i)
            else:
                continue

    for a in word:
        if a in word_found:
            display += a
        else:
            display += "_"

    print(display)

    if display == word:
        print("Vous avez gagné ! Le mot était :", word)
        break


    display = ""

    if len(word_found) == 3 or len(word_found) == 6 or len(word_found) == 9:

        suggested_word = str(input("Voulez vous proposez un mot(repondez par oui ou par non): "))

        if suggested_word == "oui":
            word2 = str(input("Quel mot: "))
            if word2 == word:
                print("Vous avez gagnez: ")
                break
            else:
                print("Faux")
                lucky -= 2
                print(f'il vous reste {lucky} chance')
                continue
        else:
            continue


if lucky == 0:
    print("Vous avez perdus")