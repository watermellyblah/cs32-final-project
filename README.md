# cs32-final-project: Trivia Game
My CS32 final project with Angel You and Melanie Volz. 
Dream Project: How can we create a trivia game?

**Planning Stages**
Subtasks:
(Need to first get the questions from somewhere. We want to create multiple genre of questions such as: Art history, sports, Harvard. (If this goes well we want to add more genres)
We need to create a server and a client to communicate with and to send the questions and answers choices
Need to create a random dictionary. Probably will need to use random.choice like in roshambo. 
Need to create a counter that gives points to every correct answer and set values for points according to difficulty (ie. 100, 200, 200, 400, 500).
Maybe a time limit to respond? Don't know how to create that right now.
Probably will not do and only do it if we finish the project early.

**Main Computational Task for Final Project: **
Creating a server and client to communicate between to give/answer questions.
Obviously have questions that we make with answers.
After the communication works, we can count the number of questions and give points according to difficulty
.
**New Updates to Readme**
We are going to use either Flask or Streamlit (most likely streamlit) to create an app interface for our trivia game.

We want our app to take our CSV files of questions and answer choices and using a dictionary function to randomly give the user a question.

We will ask for input from the user to choose the correct answer. Each question will have a different number of points to it. We will ask a series of questions and it will collect the number of points the user gets at the end of the game.

Using Streamlit will give the interface a better apperance and we can add different compendents such as a button to click and other widgets.

Some current unknowns for our project is how exactly to use Streamlit and Flask such as transfering our Github project and having it output in Streamlit app.

Some examples of our code is:

<img width="583" alt="Screen Shot 2023-04-10 at 9 47 38 PM" src="https://user-images.githubusercontent.com/130410836/231034254-9876136c-c86e-4303-862d-833230ed09ce.png">
 
 We are still working on the logistics of the project and the coding and figuring out how to use streamlit to make the appearance of our trivia game look pleasing.

The steps we need to take to make this FP possible:
1. We need to figure out how to import streamlit and using the features of it to output in the appface
2. We need to see how we can use a key within a dictionary to find the answer choices to the questions and then print out the corresponding answer choices to the randomly selected quesiton.
3. We also need to have different CSV files with different genres, and then have the player be asked to input and using the "radio" widget in Streamlit to pick the topic which pickes the CSV file.
4. Then we need to make sure that the code will not pick the same question, so we need to somehow take it away from the ones we can choose.

**Final Product**
Our Main Computational Task:
Using Streamlit as our output, we are going to us Streamlit to create a user friendly web-app interface to present our trivia game.

Steps to run the app and play the game:
1. open codespace in GitHub
2. download the necessary packages into your codespace
   install python! 
   in the terminal type: 
   install streamlit!
   in the terminal type: pip install streamlit
   to check if it has been installed run: streamlit hello --server.enableCORS false --server.enableXsrfProtection false
   to run the app: streamlit run app.py  --server.enableCORS false --server.enableXsrfProtection false
