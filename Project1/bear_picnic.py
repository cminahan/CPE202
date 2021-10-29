# Project1
# Name: Claire Minahan
# Section: CPE202-03

''' the bear game module '''

def bears(num_bears):
    """ A True return value means that it is possible
        to win the bear game by starting with n bears.
        A False return value means that it is not possible
        to win the bear game by starting with n bears.
        Args:
            num_bears(int): the number of bears the player starts with
        Returns:
            boolean: True or False on whether it is possible to win the game with n bears
    """
    if num_bears == 42:
        return True
    if num_bears < 42:
        return False
    even = num_bears%2 == 0
    three_four = (num_bears%3 == 0) or (num_bears%4 == 0)
    five = num_bears%5 == 0
    if even:
        new_bears = num_bears//2
        if bears(new_bears):
            return even
    if five:
        new_bears = num_bears - 42
        if bears(new_bears):
            return five
    if three_four:
        string_bears = str(num_bears)
        length = len(string_bears)
        mult1 = int(string_bears[length-2])
        mult2 = int(string_bears[length-1])
        minus = mult1 * mult2
        if minus == 0:
            return False
        new_bears = num_bears - minus
        if bears(new_bears):
            return three_four
    return False
