def word_count(text):
    words_list=text.split()
    return len(words_list)

def letter_count(text):
    letter_dict = {}
    lower_text=text.lower()
    for letter in lower_text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter]=1
    return letter_dict

def report(dict_letter):
    letters=[]
    for letter in dict_letter:
        dict = {"letter":letter, "num":dict_letter[letter]}
        letters.append(dict)
    def sort_on(dict_items):
        return dict_items["num"]
    letters.sort(reverse=True, key=sort_on)
    return letters
    