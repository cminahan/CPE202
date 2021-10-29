# Project1
# Name: Claire Minahan
# Section: CPE202-03

'''the permutation module'''

def perm_gen_lex(string1):
    """ Generates all permutations of the characters in a string
    Args:
        string1(string): input string with characters already sorted
    Returns:
        list: list of all permutations of the characters in the input string in lexicographic order
    """
    length = len(string1)
    if length <= 1:
        return string1.split()
    if len(string1) == 2:
        string2 = string1
        string2 += ' ' + string1[1] + string1[0]
        return string2.split()
    perm_list = []
    for char in string1:
        index = string1.find(char)
        string2 = string1[0:index] + string1[index + 1:length]
        og_string = char + string2
        perm_list.append(og_string)
        temp_list = perm_gen_lex(string2)
        if isinstance(temp_list, list):
            for item in temp_list:
                new_item = char + item
                perm_list.append(new_item)
        length_list = len(perm_list)
        for index in range(length_list - 2):
            current_string = perm_list[index]
            if current_string == perm_list[index+1]:
                perm_list.remove(perm_list[index+1])
                length_list -= 1
    return perm_list
