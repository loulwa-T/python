dictionary={"japan":"Tokyo"}
dictionary["USA"]="washington"
print(dictionary["japan"])
del dictionary["japan"]
print(dictionary)
dictionary["USA"]="new york"


for keys in dictionary:
    print(dictionary[keys])
