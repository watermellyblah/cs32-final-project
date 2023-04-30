import csv
import random
import streamlit as st
import pandas as pd
from PIL import Image


category_files = {
	"Art History": {
		"questions_url": "questions_csv/art_questions.csv", 
		"answers_url": "answers_csv/art_answers.csv"}, 
	"Harvard": {
		"questions_url": "questions_csv/harvard_questions.csv", 
		"answers_url": "answers_csv/harvard_answers.csv"}, 
	"Sports": {
		"questions_url": "questions_csv/sports_questions.csv", 
		"answers_url": "answers_csv/sports_answers.csv"},
	"Geography": {
		"questions_url": "questions_csv/geography_questions.csv", 
		"answers_url": "answers_csv/geography_answers.csv"},
	"Disney": {
		"questions_url": "questions_csv/disney_questions.csv", 
		"answers_url": "answers_csv/disney_answers.csv"}
}

#this ask for the input of the player to pick a topic
  #need to print one question at a time from the list
  #need to use the radio button feature of streamlit
  #after pick answer, need to match answer into the answers csv


#define fucntion to load questions and answers using pandas
def load_data(category):
	questions_url = category_files[category]["questions_url"]
	answers_url = category_files[category]["answers_url"]
	questions_df = pd.read_csv(questions_url)
	#answer_choices = ["A", "B", "C", "D"]
	#questions_df["Answer"] = questions_df.apply(lambda x: random.sample(answer_choices, len(answer_choices)), axis=1)
	#answers_df = pd.read_csv(answers_url, header=None)
	answer = category_files[category]["answers_url"]
	actual_answers = []
	with open(answer, encoding="utf-8-sig") as f:
		reader = csv.DictReader(f)
		for row in reader:
			actual_answers.append(row['Correct'])
	return questions_df, actual_answers

	
#define function to randomize questions and answer choices
#def randomize_data(data):
	""" """
	#data = data.sample(frac=1).rset_index(drop=True)
	#for col in ["A", "B", "C", "D"]:
		#data[col] = data[col].apply(lambda x: x.strip())
	#return data
def randomize_answer_choices(questions_df):
    answer_choices = [
        random.sample([row["A"], row["B"], row["C"], row["D"]], 4)
        for _, row in questions_df.iterrows()
    ]
    return answer_choices

#define function to ask questions and check answers
def ask_questions(category):
	""" """
	#Pull questions/answers
	st.subheader(category)
	questions_df, actual_answers = load_data(category)
	
	#questions_df = randomize_data(questions_df)
	#start counter
	score = 0
	#basically formatted as a matrix to display the questions along with the multiple choices
	for i, row in questions_df.iterrows():
		#st.radio(f"Question {i+1}: {row['Questions']}",)
		choices = [
			"None",
			row["A"],
			row["B"],
			row["C"],
			row["D"]
		]
		
		shuffled = False
		
		if not shuffled:
			random.shuffle(choices)
			shuffled = True
		
		#answer_choices = questions_df.choices(frac=0.5)
		user_answer=st.radio(f"Question {i+1}: {row['Questions']}", choices)
		st. write('You Chose:',user_answer)
		#actual_answer = answers_df[i+1:]
		if user_answer == actual_answers[i]:
			st.write("Correct")
			score += 1
		else:
			st.write("Incorrect")
		
		
		#randomize choices
		#random.shuffle(choices)
		#for j, choice in enumerate(choices):
			#returns unicode code of a specified character and then returns the character that corresponds to specified unicdeo (A incremented by j, index of answer choice).. then made into f-string
			#st.write(f"{chr(ord('A')+j)}. {choice}")
		#input answer
		#user_answer = st.text_input("Your answer:", key = i)
		#actual_answer = "27" #need to pull actual answer from csv file using pandas framework
		#check answer to answer key
		#if user_answer.strip().lower() == actual_answer:
			#st.write("Correct!")
	#score += 1
		#else:
			#st.write(f"Incorrect. The answer is {answers_df.iloc[i+1, 0].strip().lower()}")
	st.write(f"You scored: {score}/{len(questions_df)} Congratulations!")


#def game_time(category):

#define streamlit app
def main():
	st.title("Trivia Game")
	trivia_logo = Image.open("trivia.jpeg")
	st.image(trivia_logo)
	st.write("Instructions: Pick a category and answer the questions! Get ready to test your knowledge!")
	category = st.selectbox("Select a category:", list(category_files.keys()))
	st.write('You selected:', category)
	ask_questions(category)
	
	

if __name__ == "__main__":
	main()

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
