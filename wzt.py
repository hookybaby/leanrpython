import os

doc = open("a.txt", "a+")

print(doc.name)

doc.write("welcome!\n")

print(doc.tell())

doc.seek(os.SEEK_SET)

context = doc.read()
print(context)
doc.close()
