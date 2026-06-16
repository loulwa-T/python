list=[["sad","happy","mad"],["food","snacks","dinner"],["tulip","rose","daisy"],["morning","noon","evening"],["he","she","you"]]
print(list[1][1])
for i in list:
    for j in i:
        print(j)
for i in list:
    print(i)
for i in range(5):
    for j in range(3):
        print (list[i][j])