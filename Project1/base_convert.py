# Project1
# Name: Claire Minahan
# Section: CPE202-03

''' the base converter module '''

def convert(number, base):
    ''' Recursive function that returns a string representing number in the base.
    Args:
        number(int): base 10 number
        base(int): base that number is being converted to
    Returns:
        int: number with the input base
    '''
    remainder = number % base
    num = number // base
    if num == 0:
        return str(remainder)
    list1 = []
    for ascii_num in range(65, 91):
        list1.append(chr(ascii_num))
    if remainder >= 10:
        remainder = list1[remainder - 10]
    string1 = ''
    string1 += str(convert(num, base))
    string1 += str(remainder)
    return string1
