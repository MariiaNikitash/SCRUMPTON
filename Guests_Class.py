from datetime import datetime

class Guests:
        #Dictionary details -> email: [name,password,has reservation?]
    guests_dict = {'jacob@gmail.com':['Jacob Caranci','password123',True],
              'Pyside6Luver@coolmail.com': ['Billy Bob', 'MarryPyside6',False],
              'joe@gmail.com':['John Cena','SCRUMWIZARD1234',False],
              'alice123@example.com': ['Alice Wonderland', 'Wonder123!', True],
                'bob.smith@outlook.com': ['Bob Smith', 'Password2024', False],
                'carol.jones@yahoo.com': ['Carol Jones', 'Car0l@2024', True],
                'dave.miller@icloud.com': ['Dave Miller', 'SecurePass1', False],
                'eve.green@gmail.com': ['Eve Green', 'EveGreen@2024', True],
                'frank.white@hotmail.com': ['Frank White', 'Frank!2024', False],
                'grace.lee@aol.com': ['Grace Lee', 'Grace2024!', True],
                'hank.davis@protonmail.com': ['Hank Davis', 'DavisH@2024', False],
                'irene.taylor@zoho.com': ['Irene Taylor', 'Irene!2024', True],
                'john.doe@live.com': ['John Doe', 'JohnDoe123!', False]
              }
    
    def add_user(self,name,email,password):
        for emails in self.guests_dict:
            if emails == email:
                return 1
        self.guests_dict[email] = [name,password,False]

    
    def sign_in(self,email,password):
        if email not in self.guests_dict.keys():
            return 1
        if self.guests_dict[email][1] != password:
            return 1
        if password == 'SCRUMWIZARD1234':
            return 'manager'
        self.current_user = email

    def has_reservation(self,email):
        if self.guests_dict[email][2] == False:
            return 1

    def log_out(self):
        self.currrent_user = ''
    
    
    current_user = ''


