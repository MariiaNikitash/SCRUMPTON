from flask import Flask, render_template, request, redirect, url_for, session
import os

from classes import * 

app = Flask(__name__)

login_hidden = [False] #variable to keep track of when signin/signup option are visable
pay_hidden = [True] #variable to keep track of if payment form shows in calendar/payment page
current_user = [''] #variable to keep track of current user signed in, blank if no one is logged in



# Goes to home page when called
@app.route('/')
def home():
    return render_template('home_page.html',login_hidden = login_hidden[0])



# Goes to calendar_payment page when called
@app.route('/calendar_payment')
def calendar_payment():
    return render_template('calendar_payment.html',login_hidden = login_hidden[0],pay_hidden = pay_hidden[0])



# Goes to reservations page when called
@app.route('/reservations')
def reservations():
    return render_template('reservations.html',login_hidden = login_hidden[0])



# Goes to thankyou page when called
@app.route('/thankyou_page')
def thankyou_page():
    return render_template('thankyou_page.html')



#Handles what happens when user signs up
#Stays on home page... might change
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    #####################################
    ####TODO STORE INFORMATION INTO CLASS

    return redirect(url_for('home'))  # Redirect to home page after signup
    


# Handles what happens when user signs in
# Take user to calendar/payment page
@app.route('/signin', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']
    
    if True: #change this with actual logic
        
     #If login is sucessful it takes you to reservations/ calendar page
    #####################################################
    ####### TODO ####### DETERMINE IF LOGIN IS SUCESSFUL
        
        login_hidden[0] = True
        return redirect(url_for('calendar_payment'))
    
    else: #If login fails it will say login failed and to try again
        return redirect(url_for('home'))

  


#########################
### calendar/payment
#########################

#Processes the dates the user wants to stay at hotel
#Stays on calendar/payment page
@app.route('/process_dates', methods=['POST'])
def retrieve_calander_info():
    check_in = request.form['check_in']   #check_in FORMAT IS YYYY-MM-DD
    check_out = request.form['check_out'] #check_out FORMAT IS YYYY-MM-DD
    room_size = request.form['radio']   #small,medium, or large
    number_guests = request.form['quantity']  #integer 1-5
    
    #########################################################################################
    ###### TODO HAVE TO FIGURE HOW MUCH MONEY IT WILL COST: Determine cost the room is per day
    # ,how many people are staying in room, how many days they are staying
    # IS ROOM FULL ON THOSE DATES?
    #if the start date is after the end date then it should reset
    
    
    
    pay_hidden[0] = False
    return render_template('/calendar_payment.html',login_hidden = login_hidden[0],pay_hidden = pay_hidden[0])
  



#Processes Payment
#Goes to thankyou page
@app.route('/process_payment.php', methods=['POST'])
def process_payment():

    #TODO: if payement is correct then takes user to thank you page
    #if payment is incorrect then lets user retry
    #If payment is correct store payment info? store days the room is reserved in calander format,
   
    pay_hidden[0] = True
    return redirect(url_for('thankyou_page'))




if __name__ == '__main__':
    app.run(debug=True)
