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

#define function to randomzie answer choices
def random_answers(row):
	answers = row.iloc[1:].tolist()
	random.shuffle(answers)
	return pd.Series(answers)

#define function to check user's answer
def check_answer(user_answer, answer_key):
	if user_answer.lower() == answer_key.lower():
		return True
	else:
		return False

st.write('Welcome to Trivia! Pick your category:')
category = st.sidebar.selectbox('Select a Category', list(categories_dict.keys()))

# load questions and answers
questions_url = category_dict[category]["question_url"]
answers_url = category_dict[category]["answer_url"]
questions_df = pd.read_csv(questions_url)
answers_df = pd.read_csv(answers_url, header=None)

#randomize the order of questions and answers
questions_df = questions_df.sample(frac=1).reset_index(drop=True)
questions_df.iloc[:,1:] = questions_df.iloc[:, 1:].apply(random_answers, axis=1)

#Loop through questions and have user answer each one
number_correct = 0
for i, in row in questions_df.interrows():
	st.write(f"Question {i+1}: {row['Questions]}")
	st.write("Answer choices:")
    	st.write("A. " + row.iloc[1])
    	st.write("B. " + row.iloc[2])
   	st.write("C. " + row.iloc[3])
    	st.write("D. " + row.iloc[4])




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
