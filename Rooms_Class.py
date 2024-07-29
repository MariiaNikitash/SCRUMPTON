from random import randint


#Has all data on rooms and the functions manage everything related to reserving a room
class Rooms:
    def __init__(self,date_calc):
        self.date_calc = date_calc

    #2d array to keep track of all of the hotel rooms data
    rooms = [
    [101, 'small', 300, [[3,'2024-07-02', '2024-07-15', 'jacob@gmail.com', 11700,1243432423],
                            [3,'2024-07-25', '2024-07-28', 'jacob@gmail.com', 2700,1908947839]]],
    [102, 'small', 300, []],
    [103, 'small', 300,  []],
    [104, 'medium', 500,  []],
    [105, 'medium', 500,  []],
    [106, 'large', 700,  []],
    [201, 'small', 300,  []],
    [202, 'small', 300,  [[1,'2024-06-15', '2024-06-30', 'frank.white@hotmail.com', 4500,1238943785]]],
    [203, 'small', 300,  [[2,'2024-07-10', '2024-07-25', 'grace.lee@aol.com', 4500,3894027405]]],
    [204, 'medium', 500,  []],
    [205, 'medium', 500, []],
    [206, 'large', 700,  []],
    [301, 'small', 300,  []],
    [302, 'small', 300,  []],
    [303, 'small', 300,  [[4,'2024-06-01', '2024-06-15', 'john.doe@live.com', 4200,4083956483]]],
    [304, 'medium', 500,  []],
    [305, 'medium', 500,  []],
    [306, 'large', 700,  []],
]

    unpaid_reservation = []


    #adds a pending reservation before someone pays
    def add_pending_reservation(self,*,size,guests,start_date,end_date,email):
        print(size)
        self.unpaid_reservation = []
        for room in self.rooms:
            if room[1] == size:
                
                if self.available_room(start_date,end_date,room): 
                   
                    room_number = room[0]
                    self.unpaid_reservation.extend([room_number,size,guests,start_date,end_date,email])
                    return
        return 1

    #adds reservation after someone pays
    def add_reservation(self):
        for room in self.rooms:
            if len(self.unpaid_reservation) == 0:
                return 1
            if room[0] == self.unpaid_reservation[0]:
                room[3].append([self.unpaid_reservation[2],self.unpaid_reservation[3],self.unpaid_reservation[4],self.unpaid_reservation[5],self.unpaid_reservation[6],randint(1000000000,9999999999)])
               
                self.unpaid_reservation = []
                return

    #returns all reservations as a list
    def get_reservations(self,email,manager):
        reservations = []
        for room in self.rooms:
            for reservation in room[3]:
                if reservation[3] == email or manager:
                    reservations.append(self.format_reservation(room, reservation, manager))
        return reservations

    #formats the reservation when displaying as html
    def format_reservation(self, room, reservation, manager):
        if manager:
            return [
                str(room[0]), room[1], str(reservation[0]), reservation[1], reservation[2], reservation[3], reservation[4], str(reservation[5])
            ]
        return [
            f'Room Number: {room[0]}', f'Room Size: {room[1]}', f'Number of guests: {reservation[0]}',
            f'Check-in Date: {reservation[1]}', f'Check-out Date: {reservation[2]}', f'User: {reservation[3]}'
        ]
     
    #checks if theres an available room for the given dates
    def available_room(self,start_date,end_date,room):
        if len(room[3]) == 0:
            return True
        overlap = True
        for dates in room[3]:
            if self.date_calc.no_overlap(start_date,end_date,dates[1],dates[2]):
                pass
            else:
                overlap = False
        return overlap

    #deletes a reservation based on room_id       
    def delete_reservation(self,room_id):
        for room in self.rooms:
            for reservation in room[3]:
                if str(reservation[5]) == room_id:
                    index = room[3].index(reservation)
                    room[3].pop(index)
    
    #Clears the pending reservation
    def remove_pending(self):
        self.unpaid_reservation.clear()