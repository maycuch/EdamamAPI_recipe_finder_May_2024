# Edamam_recipe_finder

### What does this project do
- this is python code that extracts recipes from Edamam API
- it extracts up to 20 recipes based on user defined main ingredient (eg. 'raspberry', 'beans') and type of meal (breakfast, dinner, lunch, snack, teatime). It also offers a choice of random recipes.

### How to use this 
- you need to have [Python](https://www.python.org/downloads/) software installed
- you also need an editor where you can write and/or run the code, eg. [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)
- in order to run a code you will need to go register and create an account on [Edamam](https://www.edamam.com/). These are steps:
  - go to main page header menu and click on `Products`
  -  and within a drop down menu you click on `Recipe Search API`.
  -  It should show you a table where you click inside the column 'Developer' on `Get started`. Now you will need to sign up using your email address.
  -  Once registered and logged in, click on `Accounts` in top right header and then click on `Go to dashboard` \ `Applications` and then finally within a box 'Recipe Search API' click on `View`.
  -  Here you can find your Application ID and Application Keys which you should copy and paste into `main.py` into rows 6 and 7 inbtween `''`:
    <img width="589" alt="image" src="https://github.com/user-attachments/assets/025ccfd5-32e7-4b2e-a231-6eda0591df2d">

    
### How to run a python code
- before you run the code you need to install following modules:
  - requests
  - csv
  - pprint
  
- once you run Python code in your editor it will ask you for ingredient(s) you want to search recipes for, you also have a choice of inputting 'r' for random recipe
- it will also asks you for what type fo meal you are looking for, you can select from 5 options: breakfast, dinner, lunch, snack, teatime
 <img width="728" alt="image" src="https://github.com/maycuch/CFG-Assignments/assets/104008913/c756f6da-2ea0-46ed-bb3b-78a6859858ac">
 
- the program then runs and extracts up to 20 recipes into *recipe_results.csv* and it also prints your results into Python console with a url to access it
- at the bottom of console it shows number of recipes found
- it displays number of calories and name of the recipe with the highest number of calories within your search results
- lastly it prints main domains that all search result recipes are from, each domain only once
  ![Screenshot of results](https://github.com/maycuch/CFG-Assignments/assets/104008913/d969041b-31ef-4b16-a7f4-ce84f479694d)
