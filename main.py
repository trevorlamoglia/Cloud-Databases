from unittest import result
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def initialize_firestore():
    '''Create database connection'''   

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = "filipino-food-8d8cf-firebase-adminsdk-vhdjo-e67cc374b7.json"

    cred = credentials.Certificate("Cloud-Databases/filipino-food-8d8cf-firebase-adminsdk-vhdjo-e67cc374b7.json")
    firebase_admin.initialize_app(cred, {
        'projectId': 'filipino-food-8d8cf',
    })
    
    # Get reference to database
    db = firestore.client()
    return db

def add_dish(db):
    '''Prompt the user to add a Filipino dish into the dish database.
    The dish must be unique.'''
    
    name = input('Dish Name: ')
    location = input('Best City To Get It: ')
    popular = input("Is it popular (Y/N): ") in ['Y','y']
    price = float(input('Price: '))
    calories = int(input('Calories: '))
    
    # Hold the contents in a built dictionary 
    data = {'location':location,
            'popular':popular,
            'price':price,
            'calories':calories}
    db.collection('dish').document(name).set(data)
    
    
def search_dish(db):
    '''Display Filipino dishes in the dish database'''
    
    print('Select Option:')
    print('1) Display All Dishes')
    print('2) Display Expensive Dishes')
    print('3) Display Cheap Dishes')
    option = input('> ')
    
    # Build and execute the option made
    if option == '1':
        results = db.collection('dish').get()
    elif option == '2':
        results = db.collection('dish').where('price', '>=', 5).get()
    elif option == '3':
        results = db.collection('dish').where('price', '<=', 4).get()
    else:
        print('Invalid Input')
        return
    
    # Display results
    print('Search Results:')
    print(f"{'Name':<15} {'Location':<15} {'Popular':<10} {'Price':<10} {'Calories':<10}")
    for result in results:
        data = result.to_dict()
        print(f"{result.id:<15} {data['location']:<15} {'yes':<10} {data['price']:<10} {data['calories']:<10}")
    print()

    
def remove_dish(db):
    '''Prompt user to delete a Filipino dish from the dish database'''
    name = input('Dish Name: ')
    
    result = db.collection('dish').document(name).set(data)
    if not result.exists:
        print('Dish does not exist')
        return
    
    data = result.to_dict()
    
    data['name'] == name
    db.collection('dish').document(name).delete(data)
    

def update_dish(db):
    '''Prompt the user to update a Filipino dish's price or calorie in the dish database.'''
    
    # Update adobo price from 15.9 to 3.91
    name = input('Dish Name: ')
    
    # Check for existing item by the same name.
    result = db.collection('dish').document(name).get()
    if not result.exists:
        print('Dish does not exist')
        return
    
    print('Select Option')
    print('1) Update Price')
    print('2) Update Calories')
    print('3) Update Price and Calories')
    option = input('> ')
    
    if option == '1':
        update_price = float(input('New Price: '))
    elif option == '2':
        update_calories = int(input('New Calories: '))
    elif option == '3':
        update_price = float(input('New Price: '))
        update_calories = int(input('New Calories: '))
    else:
        print('Invalid Input')
        return

    # Convert data read from the firestore document to a dictionary
    data = result.to_dict()
    
    data['price'] == update_price
    data['calories'] == update_calories
    db.collection('dish').document(name).set(data)

    
def main():
    db = initialize_firestore()
    choice = None
    while choice != '0':
        print()
        print('0) Exit')
        print('1) Add New Dish')
        print('2) Search Dish')
        print('3) Delete Dish')
        print('4) Update Dish Information')
        choice = input("> ")
        
        if choice == '1':
            add_dish(db)
        elif choice == '2':
            search_dish(db)
        elif choice == '3':
            remove_dish(db)
        elif choice == '4':
            update_dish(db)
        
if __name__ == '__main__':
    main()