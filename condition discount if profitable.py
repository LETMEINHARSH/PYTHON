# WAP to take selling price andd cost price of item,checkif the sale is profitable or 
# loss making if the sale is profitable give discount of 5% and print new selling price.

sp=int(input("Enter selling price of item:"))
cp=int(input("Enter cost price of item:"))
if sp>cp:
    print("Discounted Price is:",sp-(sp*0.05))
else:
    print("Sale is in loss")