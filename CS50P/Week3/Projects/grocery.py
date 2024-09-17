
grocery_list = {}

while True:
    try:
        item = input().upper()
        if item not in grocery_list:
            grocery_list[item] = 1
        elif item in grocery_list:
            grocery_list[item] += 1

    except EOFError:
        print()
        for item in sorted(grocery_list):
            print (grocery_list[item], item)
        break


