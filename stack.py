values = []
n= len(values)
def push(x):
    values.append(x)
def pop():
    return values.pop()
def display():
    print(values[-1])

print("welcome to stack operations")
while True:
    choice = int(input("enter your choice (1 for push, 2 for pop, 3 for display, 4 for exit) : "))
    if choice == 1:
        item = int(input("enter an element to push"))
        push(item)
    elif choice == 2:
        if not values:
            print("stack is empty")
        else:
            print("poped element is ", pop())
    elif choice == 3:
        if not values:
            print("stack is empty")
        else:
            display()
    else:
        break
    

