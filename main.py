import requests
from pprint import pprint as pp
import csv

## storing the ID & KEY  in variables (generated upon subscription)
app_id = ''
app_key = ''

print('\nWelcome in recipe finder app!')
main_ingredient = input('\nPlease provide an ingredient you want to search recipes for or type \'r\' for random selection of recipes: ')
mealType = input('Please choose type of meal: \nAvailable options: breakfast, dinner, lunch, snack, teatime: ')

#Set up the request URL
url = 'https://api.edamam.com/api/recipes/v2'

#setting up parameters, 3 required ones: app_id, app_key, q (in case of random search this can be emitted)
if main_ingredient == 'r':
        para = {'app_id':app_id,
                'app_key':app_key,
                'type':'any',
                'random': True,
                'mealType':mealType
                }
else:
        para = {'app_id': app_id,
                'app_key': app_key,
                'type': 'any',
                'q': main_ingredient,
                'mealType': mealType
                }

#creating 'response' variable where we store all content from API's URL
response = requests.get(url,params=para)
print(f'\nResponse code: {response.status_code}\n') #checking whether we are connected

#storing all data as a dictionary in variable 'data'
data = response.json()
pp(data)


#printing search results in terminal and creating csv file
field_names = ['name','calories','cuisineType','url']
results = []

#creating flatten fucnction as cuisineType is extracting as a dictionary, eg. [american] instead of simple string 'american'
def flatten(list):
        flat_list = []
        for row in list:
                flat_list.extend(row)
        return flat_list

with open('recipe_results.csv','w') as csv_file:

        counter = 0
        for i in data['hits']:
                counter +=1
                #extracting values for csv file
                name = (i['recipe'])['label']
                cuisineType = (i['recipe'])['cuisineType']#extracting from Edamam as a list [] instead of string
                calories = round((i['recipe'])['calories'])#rounding to 0 decimal points
                url = (i['recipe'])['url']
                uri = (i['recipe'])['uri']#this seems like a unique identifier

                #creating a dictionary that will be appended into a list results
                dict = {}
                dict['name'] = name
                dict['calories'] = calories
                dict['cuisineType']="".join(flatten(cuisineType))#using function flatten to remove list [] from this extraction and joining all letters together to create a simple string eg. 'american'
                dict['url'] = url
                results.append(dict)

                print(f"{counter}. {name} \nCalories: {calories:,} \nLink: {url}\n")


        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(results)

#number of recipes found
count = 0
with open('recipe_results.csv','r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
            count +=1
print(f'Number of recipes matching your search criteria: {count}')

# Finding a recipe with highest number of calories

# finding the highest number of calories within search results
def max_calories(list):
        max = 0
        for index in list:
                if int(index['calories']) > max:
                        max = int(index['calories'])
        return max

#finding a name of recipe with highest number of calories
for i in results:
        if i['calories'] == max_calories(results):
                max_name = (i['name'])


max_cal = max_calories(results)
print(f'\n{max_name} is the recipe with the most calories: {max_cal:,} kcal.')


#example for string slicing: find websites that all search result recipes come from and print each only once
print('\nMain domains that all search result recipes are from: \n')
domains =[]
for i in results:
        individual_domain = i['url'].split('/')[2:3]
        domains.append("".join(flatten(individual_domain)))

# print(domains)
unique_domains = set(domains)
for i in unique_domains:
        print(i)