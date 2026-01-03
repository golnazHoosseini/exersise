class Book:
   def __init__(self,title,witer,price):
        self.title=title
        self.witer=witer
        self.price=price
        

   def display_details(self):
        print("show details:")   
        print(f"title: {self.title}")
        print(f"witer: {self.witer}")
        print(f"price: {self.price}")
        print("---------------------")

   def apply_discount(self,discount):
        if 0<= discount <= 100:
            self.price=self.price -(self.price * discount/100)
         
book1 = Book("the little prince","antonio de saint",50000)
book2 = Book("the alchemist","paulo coelho",40000)

book1.display_details()

book2.display_details()

book1.apply_discount(50)
book2.apply_discount(50)

print("after discuent")

book1.display_details()
book2.display_details()