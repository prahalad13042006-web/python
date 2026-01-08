amount=input("enter amount")
amount=int(amount)
first=amount//100
print(first)
middel=(amount//10)%10
print(middel)
last=amount%10
print(last)
words=["zero","one hundred","two hundred","three hundred","four hundred","five hundred","six hundred","seven hundred","eight hundred","nine hundred"]
print(words[first],"")

words=["zero","one","twenty","thirty","fourty","fifthty","sixty","seventy","eighty","ninety"]
print(words[middel],"")

words=["zero","one","two","three","four","five","six","seven","eight","nine"]
print(words[last],"")

