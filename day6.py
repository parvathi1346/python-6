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


from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, number, total_seats):
        self.number = number
        self.total_seats = total_seats

    
    @abstractmethod
    def calculate_fare(self):
        pass

    
    def show_details(self):
        print("Bus Number:", self.number)
        print("Total Seats:", self.total_seats)

class LuxuryBus(Vehicle):
    def calculate_fare(self):
        return 500
class OrdinaryBus(Vehicle):
    def calculate_fare(self):
        return 200
class SeatManager:
    def __init__(self, total_seats):
        self.__total_seats = total_seats
        self.__booked = []
    def book_seat(self):
        if len(self.__booked) < self.__total_seats:
            seat_no = len(self.__booked) + 1
            self.__booked.append(seat_no)
            return seat_no
        else:
            return None
    def cancel_seat(self, seat_no):
        if seat_no in self.__booked:
            self.__booked.remove(seat_no)
            print("Seat", seat_no, "cancelled successfully")
        else:
            print("Invalid seat number")
    def available_seats(self):
        return self.__total_seats - len(self.__booked)
class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Passenger Name:", self.name)
        print("Passenger Age:", self.age)
class Ticket:
    def __init__(self, passenger, bus, seat, fare):
        self.passenger = passenger
        self.bus = bus
        self.seat = seat
        self.fare = fare
    def show_ticket(self):
        print("\n----- TICKET DETAILS -----")
        self.passenger.show()
        print("Bus Number:", self.bus.number)
        print("Seat Number:", self.seat)
        print("Fare:", self.fare)
        print("---------------------------")
print("1 → Luxury Bus")
print("2 → Ordinary Bus")

choice = int(input("Enter your choice: "))
if choice == 1:
    bus = LuxuryBus("L100", 5)
else:
    bus = OrdinaryBus("O200", 5)
seat_manager = SeatManager(bus.total_seats)
tickets = []
while True:
    print("\n1  Available Seats")
    print("2  Book Seat")
    print("3  Cancel Seat")
    print("4  Show Tickets")
    print("5 Exit")

    option = int(input("Enter option: "))
    if option == 1:
        print("Available Seats:", seat_manager.available_seats())
    elif option == 2:
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))

        seat_no = seat_manager.book_seat()

        if seat_no is None:
            print("Bus Full")
        else:
            passenger = Passenger(name, age)
            fare = bus.calculate_fare()  
            ticket = Ticket(passenger, bus, seat_no, fare)
            tickets.append(ticket)
            ticket.show_ticket()
    elif option == 3:
        seat_no = int(input("Enter seat number to cancel: "))
        seat_manager.cancel_seat(seat_no)
    elif option == 4:
        if len(tickets) == 0:
            print("No tickets booked yet")
        else:
            for t in tickets:
                t.show_ticket()
    elif option == 5:
        print("Thank you for Booking")
        break

    else:
        print("Invalid option")
