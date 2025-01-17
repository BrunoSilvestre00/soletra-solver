from main import SoletraConfig

def get_words_pt() -> list:
    with open(SoletraConfig.WORDS_PT_FILE, encoding='utf-8') as file:
        return map(
            lambda w: w.replace('\n', '').upper(),
            file.readlines()
        )

def verify_soletra(word: str) -> bool:
    for letter in word:
        if letter not in SoletraConfig.LETTERS:
            return False
    size = len(word)
    return (
        SoletraConfig.MIN_SIZE <= size <= SoletraConfig.MAX_SIZE
    ) and (
        SoletraConfig.MAIN_LETTER in word
    )

def get_soletra_words() -> list:
    return list(filter(verify_soletra, get_words_pt()))

def generate_soletra_file():
    with open(SoletraConfig.SOLETRA_FILE, 'w', encoding='utf-8') as file:
        for word in get_soletra_words():
            file.write(f'{len(word)} - {word}\n')
