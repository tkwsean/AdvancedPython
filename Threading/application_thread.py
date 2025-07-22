from threading import *


class flighReservation:
    def __init__(self, ticket_left):
        self.ticket_left = ticket_left

    def buy(self, ticketRequested):
        if self.ticket_left >= ticketRequested:
            print("Your Ticket is confirmed")
            print("Plzz make a Payment and take your ticket")
            self.ticket_left -= ticketRequested
        else:
            print("There is not enough tickets Remaining")


myobj = flighReservation(10)  # Assuming 10 tickets available
t1 = Thread(
    target=myobj.buy, args=[3]
)  # Incomplete; should include target and arguments
t2 = Thread(target=myobj.buy, args=[11])
t3 = Thread(target=myobj.buy, args=[3])
t1.start()
t2.start()
t3.start()
