person = {
    "name": "Alex",
    "age": 25,
    "country": "USA",
    "city": "New York",
    "job": "Engineer",
    "hobby": "Reading",
    "height_cm": 175,
    "married": False,
    "email": "alex@example.com",
    "phone": "123-456-7"
}

print(person)
print(person.get("phone"))
print(person.get("weight"))
print(person["name"])
print(person["married"])
person2=person


print(person,person2)

print(person.keys())
print(person.items())

print(person.values())

print(person.pop("age"))
print(person.get("hobby"))

