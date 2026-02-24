# # class bankaccount:
# #     def __init__(self,name,balance):
# #         self.name=name
# #         self.__balance=balance
# #         self.pin = pin
# #     def deposit(self,amount):
# #         self.__balance=amount
# #         print("deposited",amount)
# #     def withdraw(self,amount):
# #         if amount<=self.__balance:
# #             self.__balance=amount
# #             print("withdraw successfully",self.__balance)
# #         else:
# #             print("insufficient balance")
# #     def show_balance(self):
# #         print(self.__balance)

# # class savingacc:
# #     def withdrawel(self,amount):
# #         if amount<=self.__balance:
# #             self.__balance=amount
# #             print("withdraw from savings")
# #         else:
# #             print("insufficient balance")
# # class currentacc:
# #     def withdrawel(self,amount):
# #         if amount<=self.__balance:
# #             self.__balance=amount
# #             print("withdraw from savings")
# #         else:
# #             print("insufficient balance")
# # name=input("enter a name:")
# # pin=int(input("enter a pin"))
# # balance=int(input("enter a balance"))
# # print("saving")
# # print("current")
# # char=int(input ("enter a acc type"))
# # if char==1:
# #     obj=savingacc(name,balance)
# #     print(obj)
# # else:
# #     obj=currentacc(name,balance)
# #     print(obj)
# # s=bankaccount(name,balance)
# # while True:
# #     print( "1.deposit 2.withdraw 3.checkbalance 4.exist")
# #     choice=int(input("enter your choice:"))
# #     if choice==1:
# #         amount=int(input("enter a num:"))
# #         s.deposit(amount)
# #     elif choice==2:
# #         entered_pin = int(input("Enter PIN: "))
# #         if entered_pin == s.pin:
# #             amount = int(input("Enter withdrawal amount: "))
# #             s.withdraw(amount)
# #         else:
# #             print("Wrong PIN")
# #     elif choice==3:
# #         s.show_balance()
# #     else:
# #         break


# # def add(a,b):
# #      return a+b
# # print(add(11,8))
# # print(add("snap","chat"))


# # class animal:
# #      def sound(self):
# #           print("animal sounds:")
# # class dog(animal):
# #      def sound(self):
# #           print("barks")
# # class cat(animal):
# #      def sound(self):
# #           print("meow")
# # d=dog()
# # c=cat()
# # d.sound()
# # c.sound()
# # abstraction

# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class square(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side*self.side

# class circle(shape):
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return 3.14* self.radius*self.radius

# square=square(2)
# circle=circle(4)
# print(square.area())
# print(circle.area())



