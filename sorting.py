

s=input("type a sentence ")
words=[word for word in s.split(" ")]

print (" ".join(sorted(set(words))))

