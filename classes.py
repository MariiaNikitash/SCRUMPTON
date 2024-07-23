class Guests:
        #Dictionary details -> email: [name,password,has reservation?]
    guests_dict = {'jacob@gmail.com':['Jacob Caranci','password123',True],
              'Pyside6Luver@coolmail.com': ['Billy Bob', 'MarryPyside6',False],
              }
    
    def add_user(self,name,email,password):
        for emails in self.guests_dict:
            if emails == email:
                print('email already exists')
                return 1
        self.guests_dict[email] = [name,password,False]

    
    def sign_in(self,email,password):
        if email not in self.guests_dict.keys():
            return 1
        if self.guests_dict[email][1] != password:
            return 1

    def has_reservation(self,email):
        if self.guests_dict[email][2] == False:
            return 1
   

    #make a function that returns a certain value to indicate if its a manager login

   





class Rooms:
        # 2d list details -> [roomnumber,size,price per day,reserved?,guests, start-date end-date, guest email]
    rooms = [[101,'small',300,3,True,'2024-07-02', '2024-07-15','jacob@gmail.com'],
             [102],
             [103,'small',500,0,False,'',''],
             [104],
             [105],
             [106,'large',700,5,True,'2024-08-02', '2024-08-17','jacob@gmail.com'],
             [201],
             [],
             [],
             [],
             [],
             [],
             [301,'small',300,2,True,'2024-07-02', '2024-07-15','jacob@gmail.com'],
             [],
             [],
             [],
             [],
             []
             ]
    unpaid_reservation = []


    def add_unpaid_reservation(self,*,size,guests,start_date,end_date,email):
        #calc price idk
        self.unpaid_reservation.append(size,guests,start_date,end_date,email)




    def get_reservations(self,email):
        user_reservations = []
        
        for i in self.rooms:
            try:
                if i[7] == email:
                     user_reservations.append(i)
            except IndexError:
                pass
               
        formated_user_reservations = []
        for i in user_reservations:
            room_num = i[0]
            size = i[1]
            guests = i[3]
            start = i[5]
            end = i[6]
            email_ = i[7]
            
            room_num_extend ='Room Number: ' + str(room_num)
            size_extend ='Room Size: ' + size
            guests_extend='Number of guests: '+ str(guests)
            start_extend='Check-in Date: ' +start
            end_extend='Check-out Date: ' +end
            email_extend='User: ' +email

            formated_user_reservations.append([room_num_extend,size_extend,guests_extend,start_extend,end_extend,email_extend])
       
        return formated_user_reservations
    ## ADD FUNCTIONS TO GET DATA
    
    ## make a function to return the price of the reservation

    ## make a function that loops through the 2d list. If the email matches with the 
    ## current logged in user then add the room array to a seperate list to return

    
name = 'jacob@gmail.com'
roommmms = Rooms()
print(roommmms.get_reservations(name))


######### more classes idk