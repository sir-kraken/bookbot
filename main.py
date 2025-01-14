def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    lowered_text = book.lower()
    lowered_text = list(lowered_text)
    charactercount = {}
    for i in range(0, len(lowered_text) - 1):
        if lowered_text[i] in charactercount:
            charactercount[lowered_text[i]] += 1
        elif lowered_text[i] not in charactercount:
            charactercount[lowered_text[i]] = 1
        
    return charactercount

def convert_to_list_of_dics(dict):
    list_from_dict = []
    for x, y in dict.items():
        if x.isalpha() == True:
            dic = {
                "character": x,
                "count": y
            }
            list_from_dict.append(dic)

    return list_from_dict

def sort_on(argument):
    return argument["count"]

def print_character_count(characterlist):
    for dic in characterlist:
        character = dic["character"]
        count = dic["count"]
        print(f"The {character} was found {count} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    wordcount = count_words(file_contents)
    charactercount = count_characters(file_contents)
    characterlist = convert_to_list_of_dics(charactercount)


    characterlist.sort(reverse=True, key=sort_on)

    #print(wordcount)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document", end="\n\n")
    print_character_count(characterlist)
    print("--- End report ---")



main()