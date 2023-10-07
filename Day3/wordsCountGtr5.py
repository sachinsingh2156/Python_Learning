list = ["Given", "a", "list", "of", "words", "count", "the", "number", "of", "words", "with", "more", "than" ,"five", "characters"]

count = 0
for i in list:
    if len(i)>5:
        count +=1

print("The number of words having more than 5 characters = ",count)