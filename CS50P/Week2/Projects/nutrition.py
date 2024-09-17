#input type of fruit.. .lower()
fruit = input("Fruit: ").lower()

#dictionary of fruits
fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "50",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangarine": "50",
    "water melon": "80"
}

#print response
if fruit in fruits:
    print("Calories:", fruits[fruit])
else:
    print()