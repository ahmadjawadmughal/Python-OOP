class User:
    country = "Pakistan"
    def __init__(self,name,mail):

        self.name = name
        self.mail = mail
        self.password = ""

    def create_password(self,password):

        password += "123"
        self.password = password
        
    def decrypt_password(self):
        password = self.password[:-3]
        return password

    def __str__(self):

        return f" {self.name},{self.mail}"

u1 = User("xyz","xyz@gmail.com")
u2 = User("abc", "abc@gmail.com")

u1.create_password("ahmad")
print(u1.password)
print(u1.decrypt_password())



bank_record ={"345-686":567,"081-528":342,"982-926":687}

class User:
    bank_name = "HBL"
    def __init__(self,name,mail):

        self.name = name
        self.mail = mail
        self.password = ""
        self.credit_card_no = "" 
        self.card_password = ""


    def create_password(self,password,credit_card_no,card_password):

        password += "922"
        self.password = password
        credit_card_no += "123"
        self.credit_card_no = credit_card_no
        card_password += "900"
        self.card_password = card_password
        

        
    def decryption(self):

        password = self.password[:-3]
        credit_card_no = self.credit_card_no[:-3]
        card_password = self.card_password[:-3]

        
        return card_password,credit_card_no,password

    def bank_transaction(self):

        card_password,credit_card_no,password = self.decryption()
        

        if credit_card_no in bank_record and bank_record[credit_card_no] == int(card_password):
                
            print("Transaction successful")

        else:
            print("Transaction not successful")
    
        
            
    def __str__(self):

        return f"{User.bank_name}, {self.name},{self.mail}"
            
u1 = User("ajm","ajm@mail.com")
u1.create_password("ahmad","345-686","567")
u1.password
u1.bank_transaction()


u2 = User("xyz","xyz@mail.com")
u2.create_password("xyz","081-528","342")
u2.password
u2.bank_transaction()

u3 = User("abc","abc@mail.com")
u3.create_password("abc","528-923","822")
u3.password
u3.bank_transaction()



def func_execute(one,two):

    one()
    two()

def func():
    def func1():
        print("function 1")

   

    def func2():

        print("function 2")

    return func1,func2

func1,func2 = func()
func_execute(func1,func2)

# None type obj is not callable
"""
def new_func():

    def new_func1():
        
        print("new function 1")

    def new_func2():

        print("new function 2")

    return new_func1(),new_func2()

new_func1, new_func2 = new_func() 
func_execute(new_func1(),new_func2())
"""
# Another function

def main_func(func1,func2):

    func1()
    func2()



def first_func():
    print("first function")

    def nested():
        print("nested function")

    return nested


def second_func():
    print("second function")

    def inside_func():
        print("inside function")

    return inside_func


main_func(first_func(),second_func())
        

## Callable & Uncallable 








        
        




