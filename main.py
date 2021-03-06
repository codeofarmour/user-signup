from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', title = "Register here!")

@app.route("/", methods=['POST'])
def validate_input():
    name = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']
    email = request.form['email']
   
    name_error = ""
    password_error = ""
    confirm_error = ""
    email_error = ""

    name_len = len(name)
    password_len = len(password)

    if not name or name_len == 0:
        name_error = 'Username required'
    else:
        name_error = ""
    
    if invalid_length(name_len):
        name_error = 'Username needs to be at least 3 characters long and less than 20'
    else:
        name_error = ""
    
    if contains_character(name, " "):
        name_error = 'Username cannot contain spaces'

    if not password:        
        password_error = 'Password required'    
    else:
        password_error = ""

    if invalid_length(password_len):
        password_error = 'Password must be at least 3 characters long but less than 20'

    if not password == confirm:
        confirm_error = 'Password required'
    else:
        confirm_error = ""
    
    if not password == confirm:
        confirm_error = "Passwords must match"
    else:
        confirm_error = ""

    email_len = len(email)
    #pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    #success = pattern.finditer(email)

    if email:
        if invalid_length(email_len):
            email_error = "Email must be at least 3 characters but less than 20"
        elif contains_character(email, " "):
            email_error = "Email cannot contain spaces"        
        #elif pattern != success:    
        #    email_error = "Email must contain one '@' character and one '.' character"
        elif '@' not in email or '@@' in email or '.' not in email or '..' in email:
            email_error = "Email must contain one '@' character and one '.' character"        
        else:
            email_error = ""
       
    if not name_error and not password_error and not confirm_error:
        if email_error:
                return render_template('index.html', title = "Register here!", name = name, email = email, email_error = email_error)
        return render_template('welcome.html', title ='Registered!', name = name, password = password, email = email)

    return render_template('index.html', title = "Register here!", name = name, name_error = name_error,\
                            password_error = password_error, confirm_error = confirm_error, email_error = email_error, email = email)

def contains_character(name, character):
    return True if character in name else False

def invalid_length(number):
    return True if number < 3 or number > 20 else False

app.run()