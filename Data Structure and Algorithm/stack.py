# How to implement stack in python

#lets create a list

def create_stack():
    stack=[]
    print('empty stack is created')
    return stack

#check if stack is empty
def check_empty(stack):
    if len(stack)>=1:
        length_of_stack=f'length of stack is:{ len(stack)}'
        return length_of_stack
    else:
        return 'stack is empty'

# display stack
def display_stack(stack):
    stack_rev=stack[::-1]
    for every in stack_rev:
        print(f'{every}\n__')

# add element
def push_element(stack,item):
    stack.append(str(item))
    print(f'element {item} has been added to the stack')

#remove element
def remove_top(stack):
    if len(stack)>=1:
        return stack.pop()
    else:
        return 'stack is empty'