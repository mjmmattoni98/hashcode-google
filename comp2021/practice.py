from typing import *
import sys


def file_reader(filename: str):
    def add_pizza(pizza: int, ingredients: set):
        # Best combinations for two_teams
        best_combinations_two, size_combinations_two = best_pizzas_combinations[2]
        # i: int = 0
        for option in best_combinations_two:
            # option is a list which contains two tuples with the index of the pizzas with their ingredients
            # and the score of the combination
            # option = [(p1, ing1), (p2, ing2), score]
            if option[-1] == -1:
                # If we are in the last best option and it is not completed
                option[1] = (pizza, ingredients)
                option[2] = len(ingredients.union(option[0][1]))
            else:
                # If we have two pizzas in the option

                # Score between the first pizza and the current pizza
                score1 = len(ingredients.union(option[0][1]))

                # Score between the second pizza and the current pizza
                score2 = len(ingredients.union(option[1][1]))

                # Update the option if we have a better score
                if score1 > score2 and score1 > option[2]:
                    option[-1] = score1
                    option[1] = (pizza, ingredients)
                elif score2 > option[-1]:
                    option[-1] = score2
                    option[0] = (pizza, ingredients)

        if size_combinations_two < two_teams + two_teams // 2:
            best_combinations_two.append([(pizza, ingredients), (), -1])
            best_pizzas_combinations[2] = (best_combinations_two, size_combinations_two + 1)

        # Best combinations for three_teams
        best_combinations_three, size_combinations_three = best_pizzas_combinations[3]
        # i: int = 0
        for option in best_combinations_three:
            # option is a list which contains three tuples with the index of the pizzas with their ingredients
            # and the score of the combination
            # option = [(p1, ing1), (p2, ing2), (p3, ing3), score]
            if option[-1] == -1:
                # If we are in the last best option and it is not completed
                if len(option[1]) == 0:
                    option[1] = (pizza, ingredients)
                else:
                    option[2] = (pizza, ingredients)
                    option[-1] = len(ingredients.union(option[0][1], option[1][1]))
            else:
                # If we have three pizzas in the option

                # Score between the second pizza and the current pizza
                score1 = len(ingredients.union(option[0][1]))

                # Score between the second pizza and the current pizza
                score2 = len(ingredients.union(option[1][1]))

                # Score between the second pizza and the current pizza
                score3 = len(ingredients.union(option[2][1]))

                # Update the option if we have a better score
                if score1 > score2 and score1 > option[-1]:
                    option[-1] = score1
                    option[1] = (pizza, ingredients)
                elif score2 > option[-1]:
                    option[-1] = score2
                    option[0] = (pizza, ingredients)
                elif score3 > option[-1]:
                    option[-1] = score2
                    option[0] = (pizza, ingredients)

        if size_combinations_three < three_teams + three_teams // 2:
            best_combinations_three.append([(pizza, ingredients), (), -1])
            best_pizzas_combinations[3] = (best_combinations_three, size_combinations_three + 1)

        # Best combinations for four_teams
        best_combinations_four, size_combinations_four = best_pizzas_combinations[4]
        # i: int = 0
        for option in best_combinations_four:
            # option is a list which contains two tuples with the index of the pizzas with their ingredients
            # and the score of the combination
            # option = [(p1, ing1), (p2, ing2), (p3, ing3), (p4, ing4), score]
            if option[-1] == -1:
                # If we are in the last best option and it is not completed
                option[1] = (pizza, ingredients)
                option[2] = len(ingredients.union(option[0][1]))
            else:
                # If we have two pizzas in the option

                # Score between the second pizza and the current pizza
                score1 = len(ingredients.union(option[0][1]))

                # Score between the second pizza and the current pizza
                score2 = len(ingredients.union(option[1][1]))

                # Update the option if we have a better score
                if score1 > score2 and score1 > option[2]:
                    option[2] = score1
                    option[1] = (pizza, ingredients)
                elif score2 > option[2]:
                    option[2] = score2
                    option[0] = (pizza, ingredients)

        if size_combinations_four < four_teams + four_teams // 2:
            best_combinations_four.append([(pizza, ingredients), (), -1])
            best_pizzas_combinations[4] = (best_combinations_four, size_combinations_four + 1)




    f_input = open(filename, "r")

    aux_line = f_input.readline().strip().split()
    pizzas: int = int(aux_line[0])
    two_teams: int = int(aux_line[1])
    three_teams: int = int(aux_line[2])
    four_teams: int = int(aux_line[3])
    best_pizzas_combinations: dict = {i: ([], 0) for i in range(2, 5)}

    pizzas_ingredients: dict = {}
    # ingredients: set = set()
    i: int = 0
    for line in f_input:
        pizza_ing = set(line.strip().split()[1:])
        pizzas_ingredients[i] = pizza_ing
        # ingredients.update(pizza_ing)
        add_pizza(i, pizza_ing)
        i += 1

    f_input.close()

    different_ingredients: dict = {}
    # for pizza, ingredients_pizza in pizzas_ingredients.items():
    #     ingredients_not_in_pizza: set = ingredients.difference(ingredients_pizza)
    #     if ingredients_not_in_pizza in different_ingredients:
    #         different_ingredients[ingredients_not_in_pizza].add(pizza)
    #     else:
    #         different_ingredients[ingredients_not_in_pizza] = set(pizza)

    # indexes_pizzas = sorted(range(pizzas), key= lambda i: len(different_ingredients[ingredients.difference(pizzas_ingredients[i])]))

    return pizzas, two_teams, three_teams, four_teams, pizzas_ingredients, different_ingredients


def delivery_solver(pizzas: int, two_teams: int, three_teams: int, four_teams: int,
                    pizzas_ingredients: dict, different_ingredients: dict):
    for pizza in pizzas_ingredients:
        if pizzas <= 0 or (two_teams <= 0 and three_teams <= 0 and four_teams <= 0):
            break
        if two_teams >= 2 and pizzas >= 2:
            ingredients = pizzas_ingredients[pizza]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ERROR: Parametros pasados al programa = {}   Esperado 1 parametro".format(len(sys.argv) - 1))
        exit(-1)

    # pizzas --> number of pizzas that has the pizzeria
    # two_teams --> number of two-people teams
    # three_teams --> number of three-people teams
    # four_teams --> number of three-people teams
    # pizza_ingredients --> dictionary with the ingredients for each pizza

    filename: str = sys.argv[1]

    pizzas, two_teams, three_teams, four_teams, pizzas_ingredients, different_ingredients = file_reader(filename)
    deliveries = delivery_solver(pizzas, two_teams, three_teams, four_teams, pizzas_ingredients, different_ingredients)

    f_output = open("submit_b.txt", "w", encoding="UTF-8")
    f_output.write("{}\n".format(len(deliveries)))
    for type_team in deliveries:
        f_output.write("{}".format(type_team))
        for index_pizza in indexes_pizzas:
            f_output.write(" {}".format(index_pizza))
        f_output.write("\n")

    f_output.close()
