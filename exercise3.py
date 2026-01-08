amount=input("enter amount")
amount=int(amount)
first=amount//100
print(first)
middel=(amount//10)%10
print(middel)
last=amount%10
print(last)
words=["zero","one","two","three","four","five","six","seven","eight","nine"]
print(words[first],"",words[middel],"",words[last],"",)