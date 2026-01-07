person={"name":"rahul sharma","age":"40","weight":74.22,"gender":True,"ismarried":False}
print(person)
print(person["name"])
print(person.get("age"))
print(person.get("city"))
person2=person.copy()
person2.clear()
print(person,person2)
print(person.keys())
print(person.values())
print(person.items())
book=["name","author","pages","price","isbnno"]
python_book=dict.fromkeys(book)
print(python_book)
python_book["name"]="mastering python"
python_book["author"]="the easy learn"
python_book["publisher"]="ABC"
print("now python book has ",python_book)
python_book.pop("price")
python_book.pop("country",False)
print(python_book)
print("good bye")
