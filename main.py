class SoletraConfig(object):
    WORDS_PT_FILE   = "files/words.pt_br.txt"
    ANAGRAMS_FILE   = "files/anagrams.out"
    SOLVED_FILE     = "files/solved.out"
    SOLETRA_FILE    = "files/soletra.out"
    
    MIN_SIZE    = 5
    MAX_SIZE    = 8
    LETTERS     = "CUDOPIM"
    MAIN_LETTER = "O"


def soletra():
    from soletra.soletra_words import generate_soletra_file
    from soletra.soletra_anagrams import generate_anagrams_file
    
    generate_soletra_file()
    generate_anagrams_file()


def solve():
    from soletra.soletra_solver import generate_solved_file
    
    TARGET_SIZE = 6
    TARGET_BEFORE = "A"
    TARGET_AFTER = "Z"
    
    def adicional_check(word: str) -> bool:
        return True
    
    generate_solved_file(
        TARGET_SIZE, TARGET_BEFORE, TARGET_AFTER, adicional_check
    )


def main():
    soletra()


if __name__ == "__main__":
    main()
