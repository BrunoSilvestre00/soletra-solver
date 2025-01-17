MIN_SIZE = 5
MAX_SIZE = 8
LETTERS = "CUDOPIM"
MAIN_LETTER = "O"


def pt_words():
    pt_words = None
    with open('dicionario.txt', encoding='utf-8') as file:
        pt_words = file.readlines()
        pt_words = [w.replace('\n', '').upper() for w in pt_words]
    return pt_words

def verify_soletra(word):
    for c in word:
        if c not in LETTERS:
            return False
    size = len(word)
    return (MIN_SIZE <= size <= MAX_SIZE) and (MAIN_LETTER in word)

def aditional_check(word):
    return True

def main():
    words = sorted(pt_words(), key=lambda x: (len(x), x))
    for w in words:
        if verify_soletra(w) and aditional_check(w):
            print(len(w), w)
    
main()