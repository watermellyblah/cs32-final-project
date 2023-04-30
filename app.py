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



#define fucntion to load questions and answers, making them separate functions to better index them later on
@st.cache_data
def load_questions(category):
	questions = category_files[category]["questions_url"]
	colnames = ["question", "answer_A", "answer_B", "answer_C", "answer_D"]
	questions_df = pd.read_csv(questions, names=colnames, skiprows=1) #first row is naming the columns
	questions_df = randomize_answer_choice(questions_df)
	return questions_df

@st.cache_data
def load_answers(category):
	answer = category_files[category]["answers_url"]
	answer_answers = []
	with open(answer, encoding="utf-8-sig") as f:
		reader = csv.DictReader(f)
		for row in reader:
			actual_answers.append(row['Correct'])
	return actual_answers

	
#define function to randomize answer choices
def randomize_answer_choices(questions_df):
    questions_df["answer_choices"] = ""
    for question_idx, question in questions_df.iterrows():
        choices = [
            question.answer_A,
            question.answer_B,
            question.answer_C,
            question.answer_D,
        ]
        random.shuffle(choices)
	#making last choice to be none
        choices.append("None")
        questions_df.loc["answer_choices"][question_idx] = choices
    return questions_df

# define function to ask questions and check answers
def ask_questions(questions_df, answers_df):
    """ """
    score = 0
    # basically formatted as a matrix to display the questions along with the multiple choices
    for question_idx, question in questions_df.iterrows():
        question_header = f"Question {question_idx+1}: {question.question}"
        # index=4 to default to "None" answer choice
        user_answer = st.radio(question_header, question.answer_choices, index=4)

        # don't print anything if answer is none
        if user_answer == "None":
            continue
	
	#checking answer, add a point if it is correct, no point is added if incorrect
        if user_answer.lower() == answers_df[question_idx].lower():
            st.write("Correct!!!")
            score += 1
        else:
            st.write("Incorrect")
    return score

# define streamlit app
def main():
    st.title("Trivia Game")
    trivia_logo = Image.open("trivia.jpeg")
    st.image(trivia_logo)
    st.write(
        "Instructions: Pick a category and answer the questions! Get ready to test your knowledge!"
    )

    category = st.selectbox("Select a category:", list(category_files.keys()))
    st.write("You selected:", category)

    st.subheader(category)
    questions_df = load_questions(category)
    answers_df = load_answers(category)

#Making it a form because for some reason randomizing was messing everything up without this
    with st.form(key="form"):
	# whole way the code works is by putting parameters (questions_df and answers_df into a function to spit out a score for our interpretation)
        score = ask_questions(questions_df, answers_df)
        st.form_submit_button(label="Submit choice")
        st.write(f"You scored: {score}/{len(questions_df)} Congratulations!")


if __name__ == "__main__":
    main()

