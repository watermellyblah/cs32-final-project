import csv
import random
import streamlit as st

with open(questions.csv) as q:
  readq = csv.reader(q)
  chosen_question = random.choice(list(readq))
  print(chosen_question)
  
  #this will hopefully print out a chosen question from our CSV file

with open(answers.csv) as a:
#.....
  #answerchoices = st.radio(...) #using the radio widget to make the choice and then
