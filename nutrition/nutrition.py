import pandas as pd


def main():

    # url = 'https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/raw-fruits-poster-text-version-accessible-version'
    # tables = pd.read_html(url)
    # df = tables [0]
    # df[df.columns[0]] = df[df.columns[0]].str.split().str[0]
    # nutrition_dict = df.set_index(df.columns[0])[df.columns[1]].to_dict()
    # nutrition_dict['Honeydew Melon'] = nutrition_dict['Honeydew']
    # nutrition_dict['Sweet Cherries'] = nutrition_dict['Sweet']
    nutrition_dict = {'Apple': 130, 'Avocado': 50, 'Banana': 110,
    'Cantaloupe': 50, 'Grapefruit': 60, 'Grapes': 90, 'Honeydew': 50,
    'Kiwifruit': 90, 'Lemon': 15, 'Lime': 20, 'Nectarine': 60, 'Orange': 80,
    'Peach': 60, 'Pear': 100, 'Pineapple': 50, 'Plums': 70,
    'Strawberries': 50, 'Sweet': 100, 'Tangerine': 50,
    'Watermelon': 80, 'Honeydew Melon': 50,
    'Sweet Cherries': 100
    }
   # while True:
    fruit = input('Item: ').title()
    if fruit in nutrition_dict:
        print(f'Calories: {nutrition_dict[fruit]}')


main()

