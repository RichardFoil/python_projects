def hello():
    print(f"Hello, from inside a file")

hello()

def pack(a,b,c):
    return [a,b,c]

print(pack(1,2,3))

def eat_lunch(my_list):
    if len(my_list) == 0:
        print(f"my lunch box is empty")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"first i eat {my_list[0]}")
            else:
                print(f"Next i eat {my_list[i]}")


eat_lunch([])
eat_lunch(["sandwhich"])
eat_lunch(["banana","crackers","juice box"])