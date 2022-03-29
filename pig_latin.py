def prima_vocale(word):
    vocali = ['a','e','i','o','u']
    index_vocale = 0
    
    for chr in word:
        if chr in vocali:
            break
        index_vocale += 1
    
    return index_vocale
    
def pig_latin(word):
    new_str=''
    vocali=['a','e','i','o','u']
    
    if word[0] in vocali:
        new_str=word+'way'
    else:
        id=prima_vocale(word)
        new_str=word[id:]+word[0:id]+'ey'
    
    return new_str

word=input('Scrivi una parola: ')        
print(pig_latin(word))