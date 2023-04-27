import csv
import random
import streamlit as st
import pandas as pd

category_files = {{"category": "Art History"}: {"questions_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/questions_csv/art_questions.csv", "answers_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/answers_csv/art_answers.csv"}, 
		  {"category": "Harvard"}: {"questions_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/questions_csv/harvard_questions.csv", "answers_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/answers_csv/harvard_answers.csv"}, 
		  {"category": "Sports"}: {"questions_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/questions_csv/sports_questions.csv", "answers_url": "https://github.com/watermellyblah/cs32-final-project/blob/main/answers_csv/sports_answers.csv"}
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

#define function to get answers from csv file and randomize
def get_question_choices(df):
	df = df.sample(frac-1).reset_index(drop=True)
	for i in range(len(df)):
		choices = df.loc[i, 'A':'D'].tolist()
		random.shuffle(choices)
		df.loc[i, 'A':'D'] = choices
	return df

#define function to check user's answer
def check_answer(user_answer, answer_key):
	if user_answer.lower() == answer_key.lower():
		return True
	else:
		return False

st.write('Welcome to Trivia! Pick your category:')
category = st.sidebar.selectbox('Select a Category', list(category_files.keys()))

# load questions and answers
questions_url = category_files[category]["question_url"]
answers_url = category_files[category]["answer_url"]
questions_df = pd.read_csv(questions_url)
answers_df = pd.read_csv(answers_url, header=None)

#randomize the order of questions and answers
questions_df = questions_df.sample(frac=1).reset_index(drop=True)
questions_df.iloc[:,1:] = questions_df.iloc[:, 1:].apply(random_answers, axis=1)

#Loop through questions and have user answer each one
number_correct = 0
for i, row in questions_df.interrows():
	st.write(f"Question {i+1}: {row['Questions']}")
    	st.write(f"A. {row['Answer_1']}")
    	st.write(f"B. {row['Answer_2']}")
    	st.write(f"C. {row['Answer_3']}")
    	st.write(f"D. {row['Answer_4']}")
    	user_answer = st.text_input("Enter your answer:")
    	if user_answer.lower() == str(answers_df.iloc[i, 0]).lower():
        	st.write("Correct!")
        	score += 1
	else:
		st.write(f"Sorry your answer is incorrect! The correct answer was {answers_df.iloc[i,0]}")




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
