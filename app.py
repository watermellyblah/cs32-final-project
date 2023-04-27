import csv
import random
import streamlit as st
import pandas as pd

category_files = {"Art History": {"questions_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/questions_csv/art_questions.csv", "answers_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/answers_csv/art_answers.csv"}, 
		  "Harvard": {"questions_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/questions_csv/harvard_questions.csv", "answers_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/answers_csv/harvard_answers.csv"}, 
		  "Sports": {"questions_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/questions_csv/sports_questions.csv", "answers_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/answers_csv/sports_answers.csv"}
		 }

#this ask for the input of the player to pick a topic
#def game_time():
  #need to print one question at a time from the list
  #need to use the radio button feature of streamlit
  #after pick answer, need to match answer into the answers csv

#st.write('You selected:', topic_option)

pd.read_csv("https://github.com/watermellyblah/cs32-final-project/blob/main/questions_csv/art_questions.csv") 

questions_df = pd.read_csv(questions_url)
category_questions_df = questions_df.loc[questions_df['Category'] == selected_category]
category_questions_df = category_questions_df.sample(frac=1).reset_index(drop=True)

#ask for the user to choose a category and display a random question from the selected category
st.write('Welcome to Trivia! Pick your category:')
#while true:
category = st.selectbox('Category', list(categories.keys()))
question = random.choice(categories[category])
st.write(question["question"])

answers_df = pd.read_csv(answers_url)
category_answers_df = answers_df.loc[answers_df['Category'] == selected_category]
correct_answers = dict(zip(category_answers_df['Question'], category_answers_df['Answer']))


#ask for user's answer and chheck if it's correct or not
user_answer = st.text_input("Your Answer:")
if user_answer.lower() == question["answer"].lower():
	st.write("You are correct!")
else:
	st.write(f"You are incorrect! The correct answer is {question['answer']}.")

#st.write('Welcome to Trivia! Pick your category:')
#while true:
#topic_option = st.selectbox('Category',('Pick a Category','Art History','Harvard', 'Sports'))
#st.write('You selected:', topic_option)
#if topic_option == 'Art History':
   #open(art_questions.csv) 
   #open(art_answers.csv)
   #st.write(art_answers.csv)
        #need to create a new function
#if topic_option == 'Harvard':
   #open(harvard_questions.csv)
   #open(harvard_answers.csv)
        #need to create a new function
#else:
   #open(sports_questions.csv)
   #open(sports_answers.csv)
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
