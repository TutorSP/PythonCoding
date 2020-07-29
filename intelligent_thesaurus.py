def return_meaning(word):
    word = word.lower()
    if word in data:                # common match
        return data[word]
    elif word.title() in data:      # proper nouns
        return data[word.title()]
    elif word.upper() in data:      # acronyms
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0:
        new_word = get_close_matches(word, data.keys(), cutoff = 0.8)[0]
        print("Did you mean",new_word,"? Type Y for YES or N for NO")
        yn = input()
        if yn == 'Y':
            return data[new_word]
        elif yn == 'N':
            return "Word does not exist in dictionary"          
        else:
            return "Please check your input. It is incorrect"          
    else:
        return "Word does not exist in dictionary"

w = input("Enter a word whose meaning you want to find : ")
meanings = return_meaning(w)
if type(meanings) == list:
    index = 1
    for meaning in meanings:
        print("Meaning",index,":",meaning)
        index += 1
else:
    print(meanings)
