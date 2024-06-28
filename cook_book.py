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
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book("recipes.txt")
    dict_by_dishes = {}
    for dish in dishes:
        ingredients_list = cook_book.get(dish, "Такого рецепта нет")
        for ingredient in ingredients_list:
            if dict_by_dishes.get(ingredient['ingredient_name'], False) == False:
                dict_by_dishes[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
            else:
                ingredient_name = dict_by_dishes[ingredient['ingredient_name']]
                quantity = ingredient_name.pop('quantity', None)
                dict_by_dishes[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(quantity) + int(ingredient['quantity']) * person_count}
    return print(dict_by_dishes)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2) 