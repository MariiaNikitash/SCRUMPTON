from flask import Flask, render_template, request, redirect, url_for

from Guests_Class import * 
from Rooms_Class import *
from Date_calculations_class import*

app = Flask(__name__)

date_calc = Date_calculations()
guests = Guests()
rooms = Rooms(date_calc)

#variables to keep track of when html elements are showing
login_hidden = [False] 
pay_hidden = [True] 
logout_hidden = [True]



# Goes to home page when called
@app.route('/')
def home():
    return render_template('home_page.html',login_hidden = login_hidden[0],logout = logout_hidden[0])



# Goes to calendar_payment page when called
@app.route('/calendar_payment')
def calendar_payment():
    return render_template('calendar_payment.html',pay_hidden = pay_hidden[0])



# Goes to reservations page when called
@app.route('/reservations')
def reservations():
    reservations = rooms.get_reservations(guests.current_user,False)

    return render_template('reservations.html',reservations = reservations)



# Goes to thankyou page when called
@app.route('/thankyou_page')
def thankyou_page():
    return render_template('thankyou_page.html')

# Goes to activity page when called
@app.route('/activity')
def activity():
    return render_template('activity.html')

# Handles what happens when user signs up
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    if guests.add_user(name,email,password) == 1:
        return render_template('home_page.html',signup_message = 'Email with account already exists',logout = logout_hidden[0])
    return render_template('home_page.html',signup_message = 'Scrumpton Account Created, Please login',logout = logout_hidden[0])
    


# Handles what happens when user signs in
# Take user to calendar/payment page if they dont have a reservations
@app.route('/signin', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']
    
    if guests.sign_in(email,password) == 1:
         #If login fails it will say login failed and to try again
         return render_template('home_page.html',signup_message = 'Email password combination does not exist',logout = logout_hidden[0])
    
    logout_hidden[0] = False
    login_hidden[0] = True
    if guests.sign_in(email,password) == 'manager':
        reservations = rooms.get_reservations(guests.current_user,True)
        return render_template('manager.html',reservations = reservations)
    
    #if user has no reservation then it takes you to calendar page
    if guests.has_reservation(guests.current_user) == 1:
        return redirect(url_for('calendar_payment')) 
    
    #if guest has a reservation then it takes you to reservations page
    return redirect(url_for('reservations'))
    
  
#Handles logout
@app.route('/logout')
def logout():
    logout_hidden[0] = True
    login_hidden[0] = False
    guests.current_user = ''

    return redirect(url_for('home'))

#Goes to homepage when the logo is clicked
@app.route('/logo_home')
def logo_home():
    pay_hidden[0] = True
    rooms.remove_pending()
    return redirect(url_for('home'))



#Deletes a reservation 
@app.route('/delete_reservation',methods=['POST'])
def delete_reservation():
    room_id = request.form['delete_reservation']
    rooms.delete_reservation(room_id)
    reservations = rooms.get_reservations(guests.current_user,True)
    return render_template('/manager.html',reservations = reservations)




#########################
### calendar/payment
#########################

#Processes the dates the user wants to stay at hotel
#Stays on calendar/payment page
@app.route('/process_dates', methods=['POST'])
def retrieve_calander_info():
    if guests.current_user == '':
        return redirect(url_for('home'))
    check_in = request.form['check_in']   #check_in FORMAT IS YYYY-MM-DD
    check_out = request.form['check_out'] #check_out FORMAT IS YYYY-MM-DD
    room_size = request.form['radio']   #small,medium, or large
    number_guests = request.form['quantity']  #integer 1-5
   
    if rooms.add_pending_reservation(size=room_size,start_date=check_in,end_date=check_out
                                     ,guests=number_guests,email=guests.current_user) == 1:
        
        return render_template('calendar_payment.html',login_hidden = login_hidden[0],
                               pay_hidden = pay_hidden[0],message = 'Room Size Unavaiable')

    if rooms.date_calc.room_cost_calculator(check_in,check_out,room_size,int(number_guests),
                                            rooms.unpaid_reservation) == 1:
         
         return render_template('calendar_payment.html',login_hidden = login_hidden[0],
                                pay_hidden = pay_hidden[0],message = 'Reservation cant exceed 30 days,Check-in must be before check-out')
      
    total,per_night = rooms.date_calc.room_cost_calculator(check_in,check_out,room_size,
                                                           int(number_guests),rooms.unpaid_reservation)
  
    pay_hidden[0] = False
    return render_template('calendar_payment.html',pay_hidden = pay_hidden[0],check_in = check_in, 
                           check_out = check_out, size = room_size, guests=number_guests,
                           email=guests.current_user,total=total,per_night=per_night)
  



#Processes Payment
#Goes to thankyou page
@app.route('/process_payment.php', methods=['POST'])
def process_payment():

    # if payement is correct then takes user to thank you page
    #if payment is incorrect then lets user retry
    #If payment is correct store payment info? store days the room is reserved in calander format,
    if guests.current_user == '':
        return redirect(url_for('home'))
    rooms.add_reservation()
    pay_hidden[0] = True
    return redirect(url_for('thankyou_page'))




if __name__ == '__main__':
    app.run(debug=True)
