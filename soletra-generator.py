MIN_SIZE = 4 
MAX_SIZE = 8
LETTERS = "AVESRLP"
MAIN_LETTER = "S"

letters = sorted(list(LETTERS))

def get_anagrams(size: int) -> list:
    if size <= 1:
        return list(letters)
    anagrams = get_anagrams(size-1)
    return [f'{l}{a}' for l in letters for a in anagrams] + anagrams

def main():
    anagrams = list(set(get_anagrams(MAX_SIZE)))
    anagrams = sorted(anagrams, key=lambda x: (len(x), x))
    for a in anagrams:
        if len(a) >= MIN_SIZE and MAIN_LETTER in a:
            print(a)

main()