"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
    (Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

    (Optional) A sign character (either '+' or '-').
One of the following formats:
    At least one digit, followed by a dot '.'.
    At least one digit, followed by a dot '.', followed by at least one digit.
    A dot '.', followed by at least one digit.

An integer can be split up into these components (in order):
    (Optional) A sign character (either '+' or '-').
    At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.


"""
def isNumber(s:str) -> bool:
    s = s.lower()
    if s.isdecimal():
        return True
    sign_count = 0
    dot_count = 0
    digit_count = 0
    scientific_count = 0
    valid_scientific = True
    for ch in s:
        if ch == '+' or ch == '-':
            sign_count += 1
            if digit_count > 0 or dot_count > 0 or scientific_count > 0:
                return
        elif ch == '.':
            dot_count += 1
            if scientific_count >= 1:
                return False
        elif ch == 'e':
            scientific_count += 1
            valid_scientific = False
            if digit_count == 0:
                return False
        elif ch.isdigit():
            digit_count += 1
            valid_scientific = True
        else:
            return False
            
    if sign_count > 1 or dot_count > 1 or scientific_count > 1 or not valid_scientific:
        return False
    if dot_count == len(s) or digit_count == 0:
        return False
    return True   

if __name__ == "__main__":
    print(isNumber("inf"))
