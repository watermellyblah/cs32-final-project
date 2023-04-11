# cs32-final-project
My CS32 final project with Angel You and Melanie Volz. 
Dream Project: How can we create a trivia game?

Subtasks:
(Need to first get the questions from somewhere. We want to create multiple genre of questions such as: Art history, sports, Harvard. (If this goes well we want to add more genres)
We need to create a server and a client to communicate with and to send the questions and answers choices
Need to create a random dictionary. Probably will need to use random.choice like in roshambo. 
Need to create a counter that gives points to every correct answer and set values for points according to difficulty (ie. 100, 200, 200, 400, 500).
Maybe a time limit to respond? Don't know how to create that right now.
Probably will not do and only do it if we finish the project early.

Main Computational Task for Final Project: 
Creating a server and client to communicate between to give/answer questions.
Obviously have questions that we make with answers.
After the communication works, we can count the number of questions and give points according to difficulty
.
New Updates to Readme
We are going to use either Flask or Streamlit (most likely streamlit) to create an app interface for our trivia game.

We want our app to take our CSV files of questions and answer choices and using a dictionary function to randomly give the user a question.

We will ask for input from the user to choose the correct answer. Each question will have a different number of points to it. We will ask a series of questions and it will collect the number of points the user gets at the end of the game.

Using Streamlit will give the interface a better apperance and we can add different compendents such as a button to click and other widgets.

Some current unknowns for our project is how exactly to use Streamlit and Flask such as transfering our Github project and having it output in Streamlit app.

Some examples of our code is:

import csv
import random
import streamlit as st

with open(questions.csv) as q:
  readq = csv.reader(q)
  chosen_question = random.choice(list(readq))
  print(chosen_question)
  
  #this will hopefully print out a chosen question from our CSV file

with open(answers.csv) as a:
.....
  answerchoices = st.radio(...) #using the radio widget to make the choice and then
 
 We are still working on the logistics of the project and the coding and figuring out how to use streamlit to make the appearance of our trivia game look pleasing.


