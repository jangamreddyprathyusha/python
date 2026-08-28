from abc import ABC,abstractmethod

class login:
    def __init__(self):
        self.__username="Reena"
        self.__password="1234"
    def login_user(self):
        username=input("enter username:")
        password=input("enter password:")
        if username==self.__username and password==self.__password:
            print("Login successful")
            return True
        else:
            print("Invalid username or password")
            return False
class product:
    def __init__(self,pid,name,price):
        self.__pid=pid
        self.__name=name
        self.__price=price
    def get_pid(self):
        return self.__pid
    def set_pid(self,pid):
        self.__pid=pid
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price=price
class serviceMethods(ABC):
    @abstractmethod
    def add_to_cart(self):
        pass
    @abstractmethod
    def update_to_cart(self):
        pass
    @abstractmethod
    def remove_to_cart(self):
        pass
    @abstractmethod
    def check_products(self):
        pass
class productService(serviceMethods):
    def __init__(self):
        self.__products={
            1:product(1,"Mobile",20000),
            2:product(2,"Laptop",50000),
            3:product(3,"Mouse",700),
            4:product(4,"Earbuds",2000),
            5:product(5,"Keyboard",2000)
        }
        self.__cart={}
    def show_products(self):
        print("========All Products==========")
        for pid,p in self.__products.items():
            print(p.get_pid(),p.get_name(),"₹"+str(p.get_price()))
    def add_to_cart(self):
        self.show_products()
        pid=int(input("Enter product id:"))
        if pid in self.__products:
            quantity=int(input("Enter quantity:"))
            if pid in self.__cart:
                old_quantity=self.__cart[pid]
                self.__cart[pid]=old_quantity+quantity
            else:
                self.__cart[pid]=quantity
            print("Product add to cart")
        else:
            print("Invalid product id")
    def update_to_cart(self):
        if len(self.__cart)==0:
            print("cart is empty")
            return
        print("========selected cart products=======")
        for pid,quantity in self.__cart.items():
            p=self.__products[pid]
            print(p.get_pid(),p.get_name(),"₹"+str(p.get_price()),"Quantity=",quantity)
        pid=int(input("Enter product id to update:"))
        if pid in self.__cart:
            quantity=int(input("Enter new quantity:"))
            if quantity>0:
                self.__cart[pid]=quantity
                print("Cart updated successfully")
            else:
                print("Quantity must be greater than 0")
        else:
            print("Product is not in cart")
    def remove_to_cart(self):
        if len(self.__cart)==0:
            print("Cart is empty")
            return
        print("========selected cart products========")
        for pid,quantity in self.__cart.items():
            p=self.__products[pid]
            print(p.get_pid(),p.get_name(),"₹"+str(p.get_price()),"Quantity=",quantity)
        pid=int(input("Enter product id to remove:"))
        if pid in self.__cart:
            del self.__cart[pid]
            print("Product removed fromCart")
        else:
            print("Product is not in cart")
    def check_products(self):
        if len(self.__cart)==0:
            print("cart is empty")
            return
        print("========My Cart=======")
        total=0
        for pid,quantity in self.__cart.items():
            p=self.__products[pid]
            amount=p.get_price()*quantity
            print("Product:",p.get_name())
            print("Price:₹"+str(p.get_price()))
            print("Quantity:",quantity)
            print("Amount:₹"+str(amount))
            print("------------------------")
            total=total+amount
        print("Total:₹"+str(total))
class main:
    def display(self):
        l=login()
        result=l.login_user()
        if result==False:
            return
        ps=productService()
        while True:
            print("=======Flipkart")
            print("1.Add to Cart")
            print("2.Update to Cart")
            print("3.Remove to Cart")
            print("4.Check product")
            print("5.Exit")
            n=int(input("Choose any one option:"))
            match n:
                case 1:
                    ps.add_to_cart()
                case 2:
                    ps.update_to_cart()
                case 3:
                    ps.remove_to_cart()
                case 4:
                    ps.check_products()
                case 5:
                    print("Thank you for shopping")
                    break
                case _:
                    print("Your selected option is invalid")
m=main()
m.display()
    
            