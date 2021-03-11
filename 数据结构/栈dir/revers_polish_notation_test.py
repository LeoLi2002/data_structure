import stack

def ReverePolishNotationTest(algebratic_expression):
    stack_ = stack.Stack()
    #遍历表达式，将表达式中字符存入栈中
    for i in algebratic_expression:
        if i in "/*-+":
            num1 = stack_.pop().val
            num2 = stack_.pop().val
            result = eval("{0}{1}{2}".format(num2, i, num1))
            stack_.push(result)
        #向栈中进行压栈
        else:
            stack_.push(i)


    return stack_.head.next.val
        #如果在压入一个数后，下一个待压入栈中的任然是数，那么连续从栈中弹出两个字符，将计算结果压入栈中

algebratic_expression = ["3","17","15","-","*","18","6","/","+"]
print(ReverePolishNotationTest(algebratic_expression))