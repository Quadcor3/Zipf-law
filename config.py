import random
import accounts

class account():
    def __init__(self, balance=0):
        accountnu=random.randint(10000, 99999)
        self.accountno=accountnu
        self.balance=balance
        #acctype   #??

    def passinp(self):
        x=input("Şifrenizi belirleyin")
        self.accpass=x

balance=0
x=input("enter no")
accounts.accountlist[x]