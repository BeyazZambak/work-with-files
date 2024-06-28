def create_cook_book(recipes_file):
    cook_book = {}
    with open(recipes_file, "r") as file:
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
    return print(cook_book)

create_cook_book("recipes.txt")