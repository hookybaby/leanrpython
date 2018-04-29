import os
try:
    doc = open("a1.txt", "a+")
    print(doc.name)

    doc.write("welcome!\n")
    print(doc.tell())

    doc.seek(os.SEEK_SET)

    context = doc.read()

except IOError as identifier:
    print("IOError")
else:
    print(context)
    doc.close()


print(os.getcwd)