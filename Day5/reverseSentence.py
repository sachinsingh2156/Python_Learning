# Create a function that takes a sentence as input and returns the sentence in reverse order

def revSentence(sentence):
    reversed_sentence = ""
    words = sentence.split()
    # SentenceArr = words[::-1]
    for i in words:
        reversed_sentence = i + " " + reversed_sentence
    return reversed_sentence.strip()


# Example usage:
input_sentence = "Hello, my name is Sachin Singh."
reversed_sentence = revSentence(input_sentence)
print(reversed_sentence)
