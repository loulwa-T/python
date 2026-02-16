word="python"
list=["_"]*len(word)
ans=input("gues a letter")
if ans in word:
    for i in range (len(word)):
        if word[i]==ans:
            list[i]=ans
print(list)
print(" ".join(list))