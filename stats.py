# count the words from the previous obtained text
def count_words(text):
    words = text.split()
    counted_words = len(words)
    return counted_words

# count the characters in the text and put them in a dictionary str--> int
def count_chars(text):
    # create empty dict
    chars_dict = {}
    # go over every char in text and convert to lowercase
    for char in text:
        char = char.lower()
        # check if char is already in dict and count up if is
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] +=1
    return chars_dict

# sort the dictionary from count_chars
def chars_dict_to_sorted_list(dict):
    #create empty list
    sorted_dict = []
    # convert each char and count in a dict and add to the list
    for char, count in dict.items():
        sorted_dict.append({"char": char, "num": count})
    # helper function for sorting       
    def sort_on(dict):
        return dict["num"]
    # sort list in desc order (greatest to least) 
    sorted_dict.sort(reverse=True, key=sort_on)

    return sorted_dict

    