from stack import Stack

def precedence(char):
    if char == '^':
        return 3
    elif char == '/' or char == '*':
        return 2
    elif char == '+' or char == '-':
        return 1
    else:
        return 0

def isOperand(char):
    return (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z')) or (ord(char) >= ord('0') and ord(char) <= ord('9'))

def infixToPostfix(s, st): 
    postFix = []
    for i in range(len(s)):
        if isOperand(s[i]):
            postFix.append(s[i])
        elif s[i] == '(':
            st.push(s[i])
        elif s[i] == ')':
            while (not st.isEmpty()) and st.peek() != '(':
                postFix.append(st.peek())
                st.pop()
            if not st.isEmpty() and st.peek() == '(':
                st.pop()  
        else:
            while (not st.isEmpty()) and (precedence(s[i]) <= precedence(st.peek())):
                postFix.append(st.peek())
                st.pop()
            st.push(s[i])

    while not st.isEmpty():
        postFix.append(st.peek())
        st.pop()

    return ' '.join(postFix)


infix_expression = input("Enter the infix expression: ")
stack = Stack()
postfix_expression = infixToPostfix(infix_expression, stack)
print(postfix_expression)