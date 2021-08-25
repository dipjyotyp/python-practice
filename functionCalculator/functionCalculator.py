def calculate(left_operand, operator, right_operand):
    if operator == '+':
        return left_operand + right_operand
    if operator == '-':
        return left_operand - right_operand
    if operator == '*':
        return left_operand * right_operand
    if operator == '//':
        return left_operand // right_operand

def zero(param = ''):
    if param == '':
        return 0
    return calculate(0, param[0], param[1])

def one(param = ''):
    if param == '':
        return 1
    return calculate(1, param[0], param[1])

def two(param = ''):
    if param == '':
        return 2
    return calculate(2, param[0], param[1])
    
def three(param = ''):
    if param == '':
        return 3
    return calculate(3, param[0], param[1])

def four(param = ''):
    if param == '':
        return 4
    return calculate(4, param[0], param[1])

def five(param = ''):
    if param == '':
        return 5
    return calculate(5, param[0], param[1])

def six(param = ''):
    if param == '':
        return 6
    return calculate(6, param[0], param[1])

def seven(param = ''):
    if param == '':
        return 7
    return calculate(7, param[0], param[1])

def eight(param = ''):
    if param == '':
        return 8
    return calculate(8, param[0], param[1])

def nine(param = ''):
    if param == '':
        return 9
    return calculate(9, param[0], param[1])

def plus(ro):
    return '+', ro
def minus(ro):
    return '-', ro
    
def times(ro):
    return '*', ro
    
def divided_by(ro):
    return '//', ro
    

print(six(divided_by(two())))
print(seven(times(five())))
print(eight(minus(three())))