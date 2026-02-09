import random
wordlist=["guess it","hey you"]
word=random.choice(wordlist)
wlist=list(word)
random.shuffle(wlist)
jmbl="".join(wlist)
while True:
 print (jmbl)
 print("try to guess the word")
 gues=input()
 if gues==word:
  print("you solved the puzzle")
  break
 else:
   ("you guessed incorrectly, try again")
 