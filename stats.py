from collections import Counter
def get_num_words(text:str) -> int:
    return len(text.split())

def get_char_count(text:str) -> dict:
    return dict(Counter(text.lower()))

def sorted_list_of_dict(input: dict) -> list:
    output = [ {'char': key, 'num': value}for key, value in input.items() if key.isalpha()]
    output.sort(reverse=True, key=lambda x: x['num'])

    return output