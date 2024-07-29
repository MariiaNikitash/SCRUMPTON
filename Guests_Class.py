from datetime import datetime

#Handles guest sign up/login information

class Guests:
        #Dictionary details -> email: [name,password,has reservation?]
    guests_dict = {'jacob@gmail.com':['Jacob Caranci','password123',True],
              'Pyside6Luver@coolmail.com': ['Billy Bob', 'MarryPyside6',False],
              'joe@gmail.com':['John Cena','SCRUMWIZARD1234',False],
                'bob.smith@outlook.com': ['Bob Smith', 'Password2024', False],
                'carol.jones@yahoo.com': ['Carol Jones', 'Car0l@2024', False],
                'dave.miller@icloud.com': ['Dave Miller', 'SecurePass1', False],
                'frank.white@hotmail.com': ['Frank White', 'Frank!2024', True],
                'grace.lee@aol.com': ['Grace Lee', 'Grace2024!', True],
                'john.doe@live.com': ['John Doe', 'JohnDoe123!', True]
              }
    
    #adds a user to the dictionary after siging up
    def add_user(self,name,email,password):
        for emails in self.guests_dict:
            if emails == email:
                return 1
        self.guests_dict[email] = [name,password,False]

    #signs in user, if manager takes them to the manager page
    def sign_in(self,email,password):
        if email not in self.guests_dict.keys():
            return 1
        if self.guests_dict[email][1] != password:
            return 1
        if password == 'SCRUMWIZARD1234':
            return 'manager'
        self.current_user = email

    #checks if a user has a reservation
    def has_reservation(self,email):
        if self.guests_dict[email][2] == False:
            return 1

    #reset who is logged in
    def log_out(self):
        self.currrent_user = ''
    
    #keeps track of who is logged in
    current_user = ''


