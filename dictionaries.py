#Dictionaries in Python are defined using curly braces {} and consist of key-value pairs.
#Each key  has to be unique and immutable (like strings, numbers, or tuples), 
# while values can be of any data type.
#Dictionaries maintain insertion order starting in Python 3.7 and later versions. 
#They are also mutable, meaning you can change their content after creation.

# Example of a Python dictionary
from turtle import title


my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

#In this example, the dictionary my_dict contains three key🔑-value pairs. 
# The keys are 'name', 'age', and 'city', and their respective values are 'Alice', 25, 
# and 'New York'.

#You can access the values in a dictionary by using their corresponding keys:
#If the key 'name' is present in the dictionary, the value associated with it will be printed.

# Accessing values by key
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict['name'])  # Output: Alice

#Here we're accessing the data stored at the key name, 
# which in this case is a string containing the name Alice.

#Accessing key elements in a Python Dictionary
kitchen = {
    "Spoons":"Top Drawer",
    "Plates":"Middle Shelf",
    "Cups":"Top Shelf",
    "Blender":"Counter"
}

location_of_spoons = kitchen["Spoons"]
print(location_of_spoons)  # Output: Top Drawer

#If you try to access a key that doesn't exist in the dictionary, Python will raise a key error.
#To avoid this, you can use the get() method, which returs None (or a specified default value)
# if the key is not found.
#The get() method is particularly useful when you're unsure if a key exists in the dictionary.

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict.get('age'))  # Output: 25
print(my_dict.get('address', 'Not Available'))  # Output: Not Available

#Handling missing Keys
kitchen = {
    "Spoons":"Top Drawer",
    "Plates":"Middle Shelf",
    "Cups":"Top Shelf",
    "Blender":"Counter"
}

location_of_toaster = kitchen.get("Toaster", "Not Found")
print(location_of_toaster)  # Output: Not Found

#Adding, Modifying, and Removing Elements
#Dictionaries are dynamic, meaning you can add, modify, or remove elements at any time. 
#Adding elements is as simple as assigning a value to a new key.

my_dict['profession'] = 'Engineer'
#Adding and Updating Elements
community_center = {
    "Yoga": "8 AM", 
    "Art": "10 AM",
}
community_center["Cooking"] = "1 PM"  # Adding a new class
print(community_center)
# Output: {'Yoga': '8 AM', 'Art': '10 AM', 'Cooking': '1 PM'}

#Modifying an existing value, assign a new value to an existing key.
my_dict['age'] = 26

#The Art of Updating
community_center = {
    "Yoga": "8 AM", 
    "Art": "10 AM",
}

community_center["Yoga"] = "7:30 AM"  # Updating the time for Yoga class
print(community_center)
# Output: {'Yoga': '7:30 AM', 'Art': '10 AM'}

#Removing Elements: Use the del or the .pop() method to remove elements from a dictionary.
del my_dict['city']
#The del statement removes the key 'city' and its associated value from my_dict.
#If you do not need to use the value being removed, del is a straightforward choice.
#The del Keyword:
book_shelf = {"Fiction":10, "Non-Fiction":7, "Mystery":5}
del book_shelf["Non-Fiction"]
print(book_shelf) # Output: {'Fiction': 10, 'Mystery': 5}

#Pop Method: Allows you to remove an item and also return its value, which can be useful 
# if you need to use the removed value.
#The .pop() Method:
inventory = {"Apples": 30, "Oranges": 20, "Bananas": 15}
removed_item = inventory.pop("Oranges")
print(removed_item)  # Output: 20
print(inventory)    # Output: {'Apples': 30, 'Bananas': 15}

#Dictionary Methods: .keys() returns a view object that displays a list of all the keys in the 
# dictionary. It can be converted to a list if needed.
print(list(my_dict.keys()))  # Output: ['name', 'age']
#The keys() Method:
user_profile = {"name": "Alice", "age": 30, "email": "alice@example.com"}
for key in user_profile.keys():
    print(key)
    
#.values() returns a view object of all the keys in the directory.
print(list(my_dict.values()))  # Output: ['Alice', 26]

#.items() returns a view object that displays a list of dictionary's key-value tuple pairs.
print(list(my_dict.items()))  # Output: [('name', 'Alice'), ('age', 26)]

#The items() Method:
book_ratings = {"1984": 4.5, "To Kill a Mockingbird": 4.8, "Brave New World": 4.3}
for book, rating in book_ratings.items():
    print(f"{book} has a rating of {rating}")

#These methods are helpful for iterating through dictionary. 
for key, value in my_dict.items():
    print(f"{key}: {value}")

book = {
    'title': '1984',
    'author': 'George Orwell',
    'year': 1949,
    'genre': 'Dystopian'
}

book['publisher'] = 'Secker & Warburg'

book['year'] = 1950
print(f"{book}: {title}")

#Looping through keys only - You can loop through keys using a for loop and this is useful 
# when you only need to access the keys of the dictionary.
for key in my_dict:
    print(key)
# Output: name, age

#Looping through values only - You can use the .values() method to loop through values.
# This is useful when you only need to access the values of the dictionary.
for value in my_dict.values():
    print(value)
# Output: Alice, 26

#Looping through key-value pairs - You can use the .items() method to loop through both keys
# and values. This is useful when you need to access both the key and its corresponding value.
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output: name: Alice, age: 26

#Looping through a Dictionary keys in a Particular Order
colors_count = {"red": 3, "blue": 4, "green": 1}
for color in sorted(colors_count.keys()):
    print(f"{color}: {colors_count[color]}")

#Nested Dictionaries: Nesting them within other dictionaries allows you to create complex data
# structures that can represent real-world entities more accurately.
#A nested dictionary is simply a dictionary where one or more values are also dictionaries.
# Creating a dictionary of users, where each user has their own dictionary of details
users = {
    'user1': {
        'name': 'Alice',
        'age': 25,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'zipcode': '10001'
        }
    },
    'user2': {
        'name': 'Bob',
        'age': 30,
        'address': {
            'street': '456 Elm St',
            'city': 'San Francisco',
            'zipcode': '94107'
        }
    }
}

# In this example, each user has a dictionary containing their 'name', 'age',
# and an 'address' dictionary with more details like street, city, and zipcode.
#Accessing Nested Dictionary Elements
# Accessing the city of user1 by first accessing 'user1', then 'address', and then 'city'
city_user1 = users['user1']['address']['city']
print(city_user1)  # Output: New York

#Modifying Nested Dictionary Elements
# Updating the zipcode of user2 from '94107' to '94109'
users['user2']['address']['zipcode'] = '94109'
print(users['user2']['address']['zipcode'])  # Output: 94109

#Adding New Nested Dictionary Elements
# Adding a new key 'phone' to user1 with the value '555-1234'
users['user1']['phone'] = '555-1234'
print(users['user1']['phone'])  # Output: 555-1234

#Looping Through Nested Dictionaries
# Looping through the outer dictionary 'users'
for user, info in users.items():
    print(f"User ID: {user}")
    
    # Looping through the inner dictionary for each user
    for key, value in info.items():
        print(f"  {key}: {value}")
        
# Expected Output:
# User ID: user1
#   name: Alice
#   age: 25
#   address: {'street': '123 Main St', 'city': 'New York', 'zipcode': '10001'}
#   phone: 555-1234
# User ID: user2
#   name: Bob
#   age: 30
#   address: {'street': '456 Elm St', 'city': 'San Francisco', 'zipcode': '94109'}

#A List of Dictionaries: A list of dictionaries is a common data structure used to store
# multiple records where each record is represented as a dictionary.
# This structure is particularly useful for handling collections of related data,
# such as a list of users, products, or any other entities.
students = [
    {
        'name': 'Alice',
        'age': 25,
        'major': 'Physics'
    },
    {
        'name': 'Bob',
        'age': 22,
        'major': 'Computer Science'
    },
    {
        'name': 'Charlie',
        'age': 23,
        'major': 'Mathematics'
    }
]

#Accessing Data in a List of Dictionaries
first_student_major = students[0]['major']
print(first_student_major)  # Output: Physics

#Looping Through a List of Dictionaries
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Expected Output:
# Name: Alice, Age: 25, Major: Physics
# Name: Bob, Age: 22, Major: Computer Science
# Name: Charlie, Age: 23, Major: Mathematics

#A List within a Dictionary: To store multiple values under a single key in a dictionary, you use
# a list as the value for that key. This is useful when you want to group related items together.
favorite_books = {
    'Alice': ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice'],
    'Bob': ['The Great Gatsby', 'Catch-22', 'Moby Dick'],
    'Charlie': ['The Hobbit', 'Harry Potter', 'War and Peace']
}
# Accessing Alice's favorite books
alice_books = favorite_books['Alice']
print(alice_books)  # Output: ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice']

# Accessing Bob's second favorite book
second_favorite_bob = favorite_books['Bob'][1]
print(second_favorite_bob)  # Output: Catch-22

#Looping through Lists made inside a Dictionary
# Looping through each person and their list of favorite books
for person, books in favorite_books.items():
    print(f"{person}'s favorite books:")
    for book in books:
        print(f" - {book}")

# Expected Output:
# Alice's favorite books:
#  - 1984
#  - To Kill a Mockingbird
#  - Pride and Prejudice
# Bob's favorite books:
#  - The Great Gatsby
#  - Catch-22
#  - Moby Dick
# Charlie's favorite books:
#  - The Hobbit
#  - Harry Potter
#  - War and Peace

#Final Challenge:
#Dictionary of Students, their grades, and print each students name, along with whether they passed
# or failed. (Passing is less than or equal to 50)
students = {
    'Alice': 85,
    'Bob': 42,
    'Charlie': 68,
    'David': 49
}

for student, grade in students.items():
    if grade >= 50:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")