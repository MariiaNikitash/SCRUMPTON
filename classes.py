class Guests:
        #Dictionary details -> email: [name,password,has reservation?]
    guests = {'jacob@gmail.com':['Jacob Caranci','password123',True],
              'Pyside6Luver@coolmail.com': ['Billy Bob', 'MarryPyside6',False],
                }
    
    def add_user(self,name,email,password):
        pass


    #make function to recieve all 3/4 parameters and add them to the 'guests' dictionary
    
    #make function to delete a guest if they delete account

    #make a function that returns a certain value to indicate if its a manager login

    #more????





class Rooms:
        # 2d list details -> [roomnumber,size,price per day,reserved?, start-date end-date, guest email]
    rooms = [[101,'small',300,True,'2024-07-02 2024-07-15','jacob@gmail.com'],
             [102],
             [103,'medium',500,False,'',''],
             [104],
             [105],
             [106],
             [201],
             [],
             [],
             [],
             [],
             [],
             [301],
             [],
             [],
             [],
             [],
             []
             ]


    ## ADD FUNCTIONS TO GET DATA
    
    ## make a function to return the price of the reservation

    ## make a function that loops through the 2d list. If the email matches with the 
    ## current logged in user then add the room array to a seperate list to return

    



######### more classes idk