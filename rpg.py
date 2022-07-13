#random password generator

import string
import random
password = []
special_char = ['!','@','#','$','(','%','^','&','*',')']

def start(length):
    if(length>0):
        while(length-4>0):
        # Randomly choose a letter from all the ascii_letters
            randomLetter = random.choice(string.ascii_letters)
            password.append(randomLetter)
            length-=1
        randomNumber()
    else:
        st.warning("Enter a valid password length")
    

    
   
    

def randomNumber():
    num = 2
    for i in range(num):
        x = random.randint(0,10)
        password.insert(random.randint(0,len(password)),str(x))
        password.insert(random.randint(0,len(password)),special_char[random.randint(0,len(special_char))])
    passwd = ""
    passwd = passwd.join(password)
    #st.write(passwd)
    #streamlit subheader
    st.subheader("Your password :-")
    st.code(passwd)
    
    
import streamlit as st
import pandas as pd
import numpy as np


st.title('Password generator')
val = 0
val = st.number_input("enter the password length", key=int)
val = int(val)
# st.write(val)


start(val)
# py -m streamlit run app.py
# to render the app

#streamlit footer




# if(keyboard.read_event('enter')){
#     start(val)

#   }