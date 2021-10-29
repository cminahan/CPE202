# Project 2
# Name: Claire Minahan
# Section: CPE202-03

from stack_array import*

def postfix_eval(input_str):
    ''' Evaluates a postfix expression
    Args:
        input_str(str): input expression to be evaluated
    Returns:
        int: the evaluation of the postfix expression
    '''
    stack = StackArray()
    for item in input_str:
        if item == ' ':
            continue
        item_ascii = ord(item)
        if 48 <= item_ascii <= 57:
            item = int(item)
            stack.push(item)
        elif 42 <= item_ascii <= 43 or item_ascii == 45 or item_ascii == 47\
                or item == '^':
            num1 = stack.pop()
            num2 = stack.pop()
            if item_ascii == 42:
                result = num1*num2
            elif item_ascii == 43:
                result = num1 + num2
            elif item_ascii == 45:
                result = num2 - num1
            elif item_ascii == 47:
                if num2 == 0:
                    raise ValueError
                result = num1/num2
            elif item == '^':
                result = num2**num1
            stack.push(result)
    return stack.pop()

def infix_to_postfix(input_str):
    ''' converts infix expression to postfix expression
    Args:
         input_str(str): infix expression
    Returns:
        str: postfix expression
    '''
    stack = StackArray()
    rpn = ''
    for item in input_str:
        if item == ' ':
            continue
        item_ascii = ord(item)
        if 48 <= item_ascii <= 57:
            rpn += item
            rpn += ' '
        else:
            if item == '(' or stack.num_items == 0 or item == '^':
                stack.push(item)
            elif item == ')':
                index = stack.num_items - 1
                while stack.arr[index] != '(':
                    rpn += str(stack.pop())
                    rpn += ' '
                    index -= 1
                stack.pop()
            elif item == '*' or item == '/':
                if stack.peek() == '^' or stack.peek() == '*' or stack.peek() == '/':
                    rpn += str(stack.pop())
                    rpn += ' '
                stack.push(item)
            elif item == '+' or item == '-':
                if stack.peek() != '(':
                    rpn += str(stack.pop())
                    rpn += ' '
                stack.push(item)
    while stack.num_items != 0:
        rpn += str(stack.pop())
        rpn += ' '
    return rpn

def prefix_to_postfix(input_str):
    ''' Converts a prefix expression to postfix
    Args:
         input_str(string): prefix expression
    Returns:
        str: postfix expression
    '''
    stack = StackArray()
    list_exp = input_str.split()
    list_exp.reverse()
    new_expression = ''.join(list_exp)
    for item in new_expression:
        item_ascii = ord(item)
        if item == ' ':
            continue
        if 48 <= item_ascii <= 57:
            stack.push(item)
        else:
             op1 = stack.pop()
             op2 = stack.pop()
             string = op1 + ' ' + op2 + ' ' + item
             stack.push(string)
    return stack.peek()
