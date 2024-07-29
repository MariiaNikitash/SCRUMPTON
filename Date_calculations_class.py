from datetime import datetime
from random import randint

#Helper class to determine calculations with dates
class Date_calculations:
  
    #returns the cost of the room based on the parameters
    def room_cost_calculator(self,check_in, check_out, room_size, num_guests,unpaid_reservation):
        check_in = datetime.strptime(check_in, "%Y-%m-%d")
        check_out = datetime.strptime(check_out, "%Y-%m-%d")
        delta = check_out - check_in
        total_days = delta.days

        if(total_days < 0):
            return 1

        if(total_days > 30):
            return 1

        if(total_days == 0):
            return 1
        
        total_price = 0
        if room_size == "small":
            total_price = 300 * total_days

        elif room_size == "medium":
            total_price = 500 * total_days

        else:
            total_price = 700 * total_days
        total_price = num_guests * total_price
        price_per_night = int(total_price/total_days)
        unpaid_reservation.append(total_price)
        return total_price, price_per_night

           
    #checks theres no overlap with the two start and end dates 
    def no_overlap(self,start1, end1, start2, end2):

        #Turning the dates into usable objects
        start1 = datetime.strptime(start1, "%Y-%m-%d")
        end1 = datetime.strptime(end1, "%Y-%m-%d")

        start2 = datetime.strptime(start2, "%Y-%m-%d")
        end2 = datetime.strptime(end2, "%Y-%m-%d")

        #Finding latest start date
        latest_start = max(start1, start2)

        #Finding earliest end date
        earliest_end = min(end1, end2)

        #Finding the delta
        delta = earliest_end - latest_start

        #Check for overlap; If delta is positive there is overlap.
        if delta.days >= 0:
            return False

        return True














