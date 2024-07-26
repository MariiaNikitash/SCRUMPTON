from datetime import datetime

class Rooms:
       
    rooms = [
    [101, 'small', 300, 3, [['2024-07-02', '2024-07-15', 'jacob@gmail.com', 11700],
                            ['2024-07-25', '2024-07-28', 'jacob@gmail.com', 2700]]],
    [102, 'small', 300, 0, []],
    [103, 'small', 300, 0, []],
    [104, 'medium', 500, 0, []],
    [105, 'medium', 500, 0, []],
    [106, 'large', 700, 0, []],
    [201, 'small', 300, 0, []],
    [202, 'small', 300, 1, [['2024-06-15', '2024-06-30', 'frank.white@hotmail.com', 4500]]],
    [203, 'small', 300, 1, [['2024-07-10', '2024-07-25', 'grace.lee@aol.com', 4500]]],
    [204, 'medium', 500, 0, []],
    [205, 'medium', 500, 0, []],
    [206, 'large', 700, 0, []],
    [301, 'small', 300, 0, []],
    [302, 'small', 300, 0, []],
    [303, 'small', 300, 1, [['2024-06-01', '2024-06-15', 'john.doe@live.com', 4200]]],
    [304, 'medium', 500, 0, []],
    [305, 'medium', 500, 1, [['2024-08-01', '2024-08-10', 'jane.doe@example.com', 25000]]],
    [306, 'large', 700, 0, []],
    [307, 'small', 300, 2, [['2024-07-01', '2024-07-10', 'lucas.wilson@domain.com', 5400],  
                            ['2024-07-15', '2024-07-25', 'lucas.wilson@domain.com', 3000]]],
    [308, 'medium', 500, 1, [['2024-08-01', '2024-08-20', 'emily.clark@domain.com', 15000]]],
    [309, 'large', 700, 2, [['2024-09-01', '2024-09-15', 'nathan.brown@domain.com', 98000],
                            ['2024-09-20', '2024-10-05', 'nathan.brown@domain.com', 119000]]]
]

    unpaid_reservation = []


    def add_pending_reservation(self,*,size,guests,start_date,end_date,email):
        print(size)
        self.unpaid_reservation = []
        for room in self.rooms:
            if room[1] == size:
                
                if self.available_room(start_date,end_date,room): ##todo
                   
                    room_number = room[0]
                    self.unpaid_reservation.extend([room_number,size,guests,start_date,end_date,email])
                    
                    return
        return 1

    
    def add_reservation(self):
        for room in self.rooms:
            if len(self.unpaid_reservation) == 0:
                return 1
            if room[0] == self.unpaid_reservation[0]:
                room[3] = self.unpaid_reservation[2]
                room[4].append([self.unpaid_reservation[3],self.unpaid_reservation[4],self.unpaid_reservation[5],self.unpaid_reservation[6]])
               
                self.unpaid_reservation = []
                return

    def get_reservations(self,email,manager):
        user_reservations = []
        
        if manager == False:
            for room in self.rooms:
                for reservation in room[4]:
                    if reservation[2] == email:
                        user_reservations.append([room[0],room[1],room[3],reservation[0],reservation[1],reservation[2]])
        else:
            for room in self.rooms:
                for reservation in room[4]:
                    user_reservations.append([room[0],room[1],room[3],reservation[0],reservation[1],reservation[2],reservation[3]])


        formated_user_reservations = []
        for i in user_reservations:
            room_num = i[0]
            size = i[1]
            guests = i[2]
            start = i[3]
            end = i[4]
            email_ = i[5]
            if manager == True:
                total_payment = i[6]
                formated_user_reservations.append([str(room_num),size,str(guests),start,end,email_,total_payment])
                continue
            room_num_extend ='Room Number: ' + str(room_num)
            size_extend ='Room Size: ' + size
            guests_extend='Number of guests: '+ str(guests)
            start_extend='Check-in Date: ' + start
            end_extend='Check-out Date: ' + end
            email_extend='User: ' + email_
            
            formated_user_reservations.append([room_num_extend,size_extend,guests_extend,start_extend,end_extend,email_extend])
       
        return formated_user_reservations
            
           
     


    def room_cost_calculator(self,check_in, check_out, room_size, guests):
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
        total_price = guests * total_price
        price_per_night = total_price/total_days
        self.unpaid_reservation.append(total_price)
        return total_price, price_per_night

    
    def available_room(self,start_date,end_date,room):
        if len(room[4]) == 0:
            return True
        overlap = True
        for dates in room[4]:
            if self.no_overlap(start_date,end_date,dates[0],dates[1]):
                pass
            else:
                overlap = False
        return overlap
           


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














