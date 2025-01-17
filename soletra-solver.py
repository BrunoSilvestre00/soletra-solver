TARGET_SIZE = 5
TARGET_BEFORE = 'SELVA'
TARGET_AFTER = 'SERRA'
CHK_PT=False

def check_pt_br(word: str) -> bool:
    pt_words = None
    with open('dicionario.txt', encoding='utf-8') as file:
        pt_words = file.readlines()
        pt_words = [w.replace('\n', '').upper() for w in pt_words]
    return word in pt_words

def adicional_check(word):
    return (
        word[-1] in 'AERLS'
        and not 'VV' in word
        and not 'VP' in word
        and not 'PS' in word
        and not 'VS' in word
        and not 'VR' in word
        and not 'PR' in word
        and not 'PV' in word
        and not 'LL' in word
        and not 'PP' in word
    )

def main():
    anagrams = None
    with open('soletra.out') as file:
        anagrams = file.readlines()
        anagrams = [a.replace('\n', '') for a in anagrams]
    
    for a in anagrams:
        if len(a) == TARGET_SIZE and TARGET_BEFORE <= a <= TARGET_AFTER and adicional_check(a):
            if not CHK_PT or check_pt_br(a):
                print(a)
    
main()