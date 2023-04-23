import csv
import random
import streamlit as st

#this ask for the input of the player to pick a topic
#def game_time():
  #need to print one question at a time from the list
  #need to use the radio button feature of streamlit
  #after pick answer, need to match answer into the answers csv
  

#def main():
st.write('Welcome to Trivia! Pick your category:')
#while true:
topic_option = st.selectbox('Category',('Art History','Harvard', 'Sports'))
st.write('You selected:', topic_option)
if topic_option == 'Art History':
   open(art_questions.csv) 
   open(art_answers.csv)
   print(art_answers.csv)
        #need to create a new function
if topic_option == 'Harvard':
   open(harvard_questions.csv)
   open(harvard_answers.csv)
        #need to create a new function
else:
   open(sports_questions.csv)
   open(sports_answers.csv)
        #need to create a new function
  
  #return main()
          
          #open sportsadfdhaoif
#with what ever topic they choose open the file of that topic
  #use a streamlit function with the different buttons to choose from 
#using the dictionary key, show a question and the answer choices
  #use streamlit function to create 4 answer bubble choices that prompt user to click
  #need to make the bubble answer choices randomized, but know the right anaswer choice
#ask for input from user to pick the answer
#show the the result/the correct answer
  #somehow let the computer know the right answer choice
#add points to the system
#points = 0
#for #something:
  #if #user answer# == questions[question][-1]
  
  #probably need to use a counter of some sort that adds points and use something to print the counter
#at the end of the game show the number of points recieved
#with open(questions.csv) as q:
  #readq = csv.reader(q)
  #chosen_question = random.choice(list(readq))
  #print(chosen_question)
  
  #this will hopefully print out a chosen question from our CSV file

#with open(answers.csv) as a:
#.....
  #answerchoices = st.radio(...) #using the radio widget to make the choice and then
