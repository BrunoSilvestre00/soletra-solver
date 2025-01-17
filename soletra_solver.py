from main import SoletraConfig

def get_anagrams() -> list:
    with open(SoletraConfig.ANAGRAMS_FILE, encoding='utf-8') as file:
        return [a.replace('\n', '') for a in file.readlines()]

def solve(target_size: int, target_before: str, target_after: str, adicional_check) -> list:
    return list(filter(
        lambda a: (
            (len(a) == target_size) and 
            (target_before <= a <= target_after) and 
            adicional_check(a)
        ),
        get_anagrams()
    ))
    
def generate_solved_file(target_size: int, target_before: str, target_after: str, adicional_check):
    with open(SoletraConfig.SOLVED_FILE, 'w', encoding='utf-8') as file:
        for word in solve(target_size, target_before, target_after, adicional_check):
            file.write(f'{word}\n')
