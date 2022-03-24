import string

text = "семья, тарелка, работа, ребзя, я, ария."
text = text.replace(",", "")
text = text.replace(".", "")

count_ = text.count("я")
print(text)
print(count_)


