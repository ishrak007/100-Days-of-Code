import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = r"D:\CODED_LIFE\###Udemy-100 Days of Pyt\Projects\25- US States Game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"D:\CODED_LIFE\###Udemy-100 Days of Pyt\Projects\25- US States Game\50_states.csv")
states = data.state.to_list()

# co_ordinates_x = data.x.to_list()
# co_ordinates_y = data.y.to_list()
# ans = "ohio".title()
# co_ord_x = data[data.state == ans].x.item()
# co_ord_y = data[data.state == ans].y.item()
# co_ord_y = data[data.state == ans].state.item()
# print(co_ord_x)
# print(co_ord_y)

game_end = False
writer = turtle.Turtle()
writer.ht()
writer.pu()
guessed_states = []
global score
score = 0
ans = screen.textinput(title="Guess The States", prompt="Name a State").title()
while not game_end:
    
    if ans in states:
        state_x = data[data.state == ans].x.item()
        state_y = data[data.state == ans].y.item()
        writer.goto(state_x, state_y)
        writer.write(arg=data[data.state == ans].state.item(), 
                     align="center", font=("Arial", 8, "normal"))
        guessed_states.append(ans)
        score += 1
        
    if score == 50 or ans == "exit".title():
        game_end = True
        show_states = [state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         show_states.append(state)
        remaining_states_df = pandas.DataFrame(show_states)
        remaining_states_df.to_csv(r"D:\CODED_LIFE\###Udemy-100 Days of Pyt\Projects\25- US States Game\States To Learn 2.csv")
        
    if not game_end:
        ans = screen.textinput(title=f"{score}/50 States Correct", prompt="Name a State").title()
        