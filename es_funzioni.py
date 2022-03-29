# ESERCIZI
# REVERSE
# Scrivi una funzione che ha come argomento una parola.
# Verifica e stampa la stessa parola ma al contrario.
# es. 'abcd' -> 'dbca'


def reverse(word):
    str = ""
    for i in word:
        str = i + str
    print(str)
    # se voglio che mi ritorni un oggetto devo usare return
    # print me la stampa e basta
    return str


parola = input("Scrivi una parola: ")

reverse(parola)

# CUSTOM LEN
# Scrivi una funzione che ha come argomento una parola.
# Verifica e stampa la lunghezza esatta di quella parola.


def custom_len(word):
    len = 0
    for i in word:
        len += 1
    print(f"La tua parola è lunga {len} caratteri")


parola2 = input("Scrivi una seconda parola: ")

custom_len(parola2)

# PALINDROMO
# Scrivi una funzione che ha come argomento una parola.
# Verifica e stampa se la parola è palindroma o oppure no.


def palindromo(word):
    if word == reverse(word):
        print("La tua parola è palindroma")
    else:
        print("La tua parola non è palindroma")


parola3 = input("Scrivi una terza parola: ")

palindromo(parola3)

# ALTERNATIVA CON CICLO FOR
def palindrome(word):
    notPalindrome = False
    for i in range(len(word)):
        if word[i] != word[-i - 1]:
            notPalindrome = True
    if notPalindrome:
        word += " non"

    print(f"La parola {word} è palindroma.")


palindrome(input("Inserisci una parola: "))
