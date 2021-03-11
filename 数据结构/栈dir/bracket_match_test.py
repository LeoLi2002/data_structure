import stack

def BracketMatchTest(string):
    stack_ = stack.Stack()
    for i in string:
        if i == "(":
            stack_.push("(")
        if i == ")":
            try:
                stack_.pop()
            except:
                return False
    if stack_.length != 0:
        return False
    return True

string1 = "()()())"
string2 = "()()()()"
print(BracketMatchTest(string1))
print(BracketMatchTest(string2))