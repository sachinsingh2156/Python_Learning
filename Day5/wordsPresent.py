# Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence

sentence = input("Enter a sentence : ")
words = input("Enter the word: ")

sentenceArr = sentence.split()
if words not in sentenceArr:
    print("Not present")
else:
    print("Present At Index ", sentenceArr.index(words))
