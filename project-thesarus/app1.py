from asyncio import open_unix_connection
import json
from difflib import SequenceMatcher, get_close_matches


# load json file to python dictionary

data = json.load(open('data.json'))


def find_word(word):
    w = word.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif(len(get_close_matches(w, data.keys(), n=3, cutoff=0.8)) > 0):
        yn = input("Did you mean %s instead? , Enter Y if yes, or N if No: " %
                   get_close_matches(w, data.keys(), n=3, cutoff=0.8)[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower == 'y':
            return "The word does not exist, Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "The word does not exist, Please double check it"


word = input('Enter word: ')

output = find_word(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
