cook_book = {}

with open("recipes.txt", "r") as file:
    for line in file:
        dish_name = line.strip()
        ingredient_count = file.readline()
        cook_book[dish_name] = []
        for i in range(int(ingredient_count)):
            ingredient_info = file.readline()
            ingredient_name, quantity, measure = ingredient_info.split(" | ")
            ingredient_dict = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
            cook_book[dish_name].append(ingredient_dict)
        file.readline()
print(cook_book)