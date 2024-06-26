from bs4 import BeautifulSoup
import requests

def scrapeRestaurants(location, cuisine):
    url = f"https://www.yelp.com/search?find_desc=Restaurants&find_loc=New+York%2C+NY"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.content, "html.parser")
   
    restaurants = []
   
    for item in soup.findAll("h4", class_="css-1l5lt1i"):
        name = item.text.strip()
        restaurants.append(name)
    print('Found restaurants:', restaurants)
    return restaurants

def filterByPrice(restaurants, priceRange):
    filteredRestaurants = []
    for restaurant in restaurants:
        if priceRange == '$':
            if '$' in restaurant:
                filteredRestaurants.append(restaurant)
        elif priceRange == '$$':
            if '$$' in restaurant:
                filteredRestaurants.append(restaurant)
        elif priceRange == '$$$':
            if '$$$' in restaurant:
                filteredRestaurants.append(restaurant)
    return filteredRestaurants
def getUserPreferences():
    cuisine = input('What type of cuisine are you in the mood for? (Japanese, Chinese, American, Filipino, Mediterranean, Korean):\n>>>').strip().title()
    location = input('What are would you like to dine at? (Midtown East, SoHo, Chelsea, Koreatown, Hell\'s Kitchen):\n>>>').strip().title()
    budget = input('What is your budget? ($, $$, $$$): \n>>>').strip().upper()
    return cuisine, location, budget

def main():
    print('Welcome to the Restaurant Finder!!!')
    cuisine, location, budget = getUserPreferences()
    restaurants = scrapeRestaurants(location, cuisine)
    filteredRestaurants = filterByPrice(restaurants, budget)
   
    if len(filteredRestaurants) == 0:
        print('Sorry, there are no restaurants that match your desired criteria.')
    else:
        print('Here are the restaurants that match your desired criteria:')
        for restaurant in filteredRestaurants:
            print('-', restaurant)
if __name__ == '__main__':
    main()
