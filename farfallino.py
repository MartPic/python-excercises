def farfallino(word):
    new_str = ""
    vocali = ["a", "e", "i", "o", "u"]

    for chr in word:
        if chr in vocali:
            new_str += chr + "f" + chr
        else:
            new_str += chr
    print(new_str)


parola = input("Scrivi qualcosa: ")

farfallino(parola)
