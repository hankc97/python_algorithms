# Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. 
# Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. 
# For example ‘([])’ is balanced but ‘([)]’ is not.
# You can assume the input string has no spaces.

def balance_check(string):
    stack = [string[0]]
    opposites = { '(' : ')', '[' : ']', '{' : '}', ')' : '(', ']' : '[', '}' : '{' }
    for symbol in string[1:]:
        if (len(stack) != 0) and stack[-1] == opposites[symbol]:
            stack.pop()
        else:
            stack.append(symbol)
    return len(stack) == 0


if __name__ == '__main__':
    print(
        balance_check('[]'), #true
        balance_check('[](){([[[]]])}'), #true
        balance_check('()(){]}') #false
    )

