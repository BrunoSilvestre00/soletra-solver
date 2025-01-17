from main import SoletraConfig

letters = sorted(list(SoletraConfig.LETTERS))

def get_anagrams(size: int) -> list:
    if size <= 1:
        return list(letters)
    anagrams = get_anagrams(size-1)
    return [f'{l}{a}' for l in letters for a in anagrams] + anagrams

def generate_anagrams() -> list:
    anagrams = list(set(get_anagrams(SoletraConfig.MAX_SIZE)))
    anagrams = sorted(anagrams, key=lambda x: (len(x), x))
    return list(filter(
        lambda a: len(a) >= SoletraConfig.MIN_SIZE and SoletraConfig.MAIN_LETTER in a,
        anagrams
    ))

def generate_anagrams_file():
    with open(SoletraConfig.ANAGRAMS_FILE, 'w', encoding='utf-8') as file:
        for anagram in generate_anagrams():
            file.write(f'{anagram}\n')
