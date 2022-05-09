import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def initialize_firestore():
    '''Create database connection'''   

    cred = credentials.Certificate("Cloud-Databases/filipino-food-8d8cf-firebase-adminsdk-vhdjo-e67cc374b7.json")
    firebase_admin.initialize_app(cred, {
        'projectId': 'filipino-food-8d8cf',
    })
    
    # Get reference to database
    db = firestore.client()
    return db

def add_new_dish(db):
    '''Prompt the user to add a Filipino dish into the dish database.
    The dish must be unique.'''
    
    name = input('Dish Name: ')
    location = input('Best City To Get It: ')
    popular = input("Is it popular (Y/N): ") in ['Y','y']
    price = int(input('Price: '))
    calories = int(input('Calories: '))
    
    # Hold the contents in a built dictionary 
    data = {'location':location,
            'popular':popular,
            'price':price,
            'calories':calories}
    db.collection('dish').document(name).set(data)
    
    
def search_dish(db):
    '''Search the dish database'''
    
    results = db.collection('dish').get()
    
    # Display results
    print('Search Results:')
    print(f"{'Name':<20} {'Location':<10} {'Popular':<10} {'Price':<10} {'Calories':<10}")
    for result in results:
        data = result.to_dict()
        print(f"{result.id:<20} {data['location']:<10} {'yes':<10} {data['price']:<10} {data['calories']:<10}")
    print()
    
def main():
    db = initialize_firestore()
    choice = None
    while choice != '0':
        print()
        print('0) Exit')
        print('1) Add New Dish')
        print('2) Search Dish')
        
        if choice == '1':
            add_new_dish(db)
        elif choice == '2':
            search_dish(db)
        
if __name__ == '__main__':
    main()