students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
def iterateDictionary(students):
    for i in students:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")
        
print(iterateDictionary(students))

