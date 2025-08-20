import sys
from stats import get_num_words, get_char_count, sorted_list_of_dict

def get_book_text(filepath:str) -> str:
    with open(filepath, 'r') as f:
        file_content = f.read()
        return file_content

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_content = get_book_text("./" + path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_content)} total words")
    print("--------- Character Count -------")
    char_count:dict = get_char_count(file_content)
    sorted_counts:list = sorted_list_of_dict(char_count)
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()