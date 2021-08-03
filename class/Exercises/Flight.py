class Flight():
    airline = 'Turkish Airlines' # static attribute
    def __init__(self,flightNum,takeOff,arrival,duration,airplaneCapacity,passenger): # dunder is used.
        self.flightNum = flightNum
        self.takeOff = takeOff
        self.arrival = arrival
        self.duration = duration
        self.airplaneCapacity = airplaneCapacity
        self.passenger = passenger
    def __repr__(self):
        return "{} has been created.".format(self.flightNum)        
    def announce(self):
        return "{}-{} flight {} will take {} minutes.".format(self.takeOff,
                self.arrival,self.flightNum,self.duration)
    def seatingCapacity(self):
        return self.airplaneCapacity - self.passenger
    def ticketSales(self,numOfTicket = 1): # number of ticket is as a default 1.
        if self.passenger + numOfTicket < self.airplaneCapacity:
            self.passenger += numOfTicket
            self.seatingCapacity()
            print("{} seat has been saled,rest is {}.".format(numOfTicket,self.seatingCapacity()))
        else:
            print("There is not enough seat to buy.")
    def cancellationTicket(self,numOfTicket = 1):
        if self.passenger >= numOfTicket:
            self.passenger -= numOfTicket
            print("{} ticket has been cancelled, current number of seat is {}.".format(numOfTicket,self.seatingCapacity()))
        else:
            print("Operation failed.")


flight1 = Flight('TK123',"IST","AN",40,200,180) # creating an object

print(flight1.__dir__()) # to see the content of the class that I created.
