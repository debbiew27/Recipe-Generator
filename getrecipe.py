import random

'''
def get_recipes(table):
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=#no;'
                        'Database=Recipes;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Recipes.dbo.' + table)

    for row in cursor:
        print(row)
'''

def get_recipes_txt(category):
    file_name = category + ".txt"
    recipe_file = open(file_name)
    list_of_recipes = recipe_file.readlines()
    index = random.randrange(len(list_of_recipes))
    recipe_string = list_of_recipes[index]
    return parse_string(recipe_string)

def parse_string(recipe_string):
    tokens = recipe_string.split(" ")
    url = tokens[0]
    name = ""
    for index in range(1, len(tokens)):
        name += tokens[index] + " "
    result = [url, name]
    return result