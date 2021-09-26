import turtle
import pandas
from scoreboard import Scoreboard

#create screen with background image of blank states
screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic(r"US-states-game\blank_states_img.gif")


#import csv data and create pandas dataframe
us_states = pandas.read_csv(r"US-states-game\50_states.csv")

#create a list containing only state names
states_only = us_states["state"].to_list()

#create a list to store strings containing correct guesses
correct_guesses = []

#create an instance of scoreboard class
scoreboard = Scoreboard()

#boolean to determine if game is on or off
game_is_on = True

while game_is_on:
    #prompt user for input and store as a variable
    input_prompt = turtle.textinput("Your Guess", "Enter a state name: ")
    #create a 'stop' option for debugging
    if input_prompt == 'stop':
        game_is_on = False
    #if the user repeats a guess restart loop
    if input_prompt.lower() in correct_guesses:
        continue
    #check if user input matches a genuine state name
    for state in states_only:
        if input_prompt.lower() == state.lower():
            #if user input matches a state
            #write state name at the coordinates found in the csv file
            correct_guess = turtle
            correct_guess.hideturtle()
            correct_guess.penup()
            correct_guess.color("black")
            x = int(us_states[us_states.state == state].x)
            y = int(us_states[us_states.state == state].y)
            correct_guess.goto(x, y)
            correct_guess.write(f"{state}")

            #add the correct guess to the correct guesses list
            correct_guesses.append(input_prompt.lower())
            #increase score and update the screen
            scoreboard.playerscore += 1
            scoreboard.update_score()
    #if player names all 50 states the game is won
    if scoreboard.playerscore == 50:
        scoreboard.victory()
        game_is_on = False

states_to_learn = [state for state in states_only if state.lower() not in correct_guesses]

#for state in states_only:
    #if state.lower() not in correct_guesses:
        #states_to_learn.append(state)

learning_data = pandas.DataFrame(states_to_learn)
learning_data.to_csv("states_to_learn.csv")


screen.exitonclick()