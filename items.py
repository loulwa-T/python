products={"bag":20,"shoes":10,"shirt":25,"jacket":30,"pant":5}
cart={}
while True:
 product=input("what do you want to purchase")
 if product=="stop":
  break

 quantity=int(input("how many items would you like"))
 cart[product]=quantity
 
print(cart)
total=0
for key, value in cart. items():
 print(key,value,products[key])
 amount=value*products[key]
 print(amount)
 tota=total+amount
print(total)