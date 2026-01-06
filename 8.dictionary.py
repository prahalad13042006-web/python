book={}
print(book)
book["name"]="Atomic habit"
book["Author"]="James clear"
book["price"]=5000
print(book)

book["chapter"]=1,2,3,4,5
book["topics"]="abc","cde","efg","xyz","pqr"
print(book["chapter"][0])
print(book["chapter"][1])

print(book["topics"][2])
print(book["topics"][3])

book["topics"]="aabbbcc"
print(book)