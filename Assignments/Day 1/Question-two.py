# 2. Write a Python function to find the length of the last word.

def find_length_of_last_word(sentence):
    return len(sentence.split(" ")[-1])
print(find_length_of_last_word("Hello World kai"))

text = "X-DSPAM-Confidence:    0.8475"
x = (text.find(" "))
print(x)