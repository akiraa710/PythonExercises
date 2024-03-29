# Import tkinter for GUI.
from tkinter import *
# Import random to pick questions in a random order.
import random

# Names will be put in here later for scoreboard etc.
names = []
global questions_answers
# Will store questions that have already been asked so they don't get randomly picked again.
asked = []
score = int(0)

questions_answers = {
    1: ["What must you do when you see blue and red flashing lights behind you?", 'Speed up to get out of the way', 'Slow down and drive carefully', 'Slow down and stop', 'Drive on as usual', 'Slow down and stop',3],
    2: ["You may stop on a motorway only:", 'If there is an emergency', 'To let down or pick up passengers', 'To make a U-turn', 'To stop and take a photo', 'If there is an emergency', 11],
    3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?", "Speed up before the pedestrians cross", 'Stop and give way to pedestrians on any part of the crossing', "Sound the horn on your vehicle to warn the pedestrians", "Slow down to 30kph", 'Stop and give way to pedestrians on any part of the crossing', 2],
    4: ["Can you stop on a bus stop in a private motor vehicle?", 'Only between midnight and 6am', "Under no circumstances", "When dropping off passengers", 'Only if it is less than 5 minutes', "Under no circumstances", 2],
    5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)", '70 km/h', "100 km/h so you do not hold up traffic", "80 km/h and if the wheel spacer displays a lower limit that applies", "90 km/h", "80 km/h and if the wheel spacer displays a lower limit that applies",3],
    6: ["When following another vehicle on a dusty road, you should:", 'Speed up to get passed',"Turn your vehicle's windscreen wipers on", "Stay back from the dust cloud", 'Turn your vehicles headlights on', "Stay back from the dust cloud", 31],
    7: ["What does the sign containing the letters 'LSZ' mean", 'Low safety zone', "Low stability zone", "Lone star zone", 'Limited speed zone', 'Limited speed zone',4],
    8: ["What speed are you allowed to pass a school bus that has stopped to let students get on or off?", '20 km/h', "30 km/h", "70 km/h", '10 km/h', '20 km/h',1], 
    9: ["What is the maximum distance a load may extend in front of a car?", '2 meters forward of the front edge of the front seat', "4 meters forward of the front edge of the front seat", "3 meters forward of the front edge of the front seat", '2.5 meters forward of the front edge of the front seat', '3 meters forward of the front edge of the front seat',3],
    10: ["To avoid being blinded by the headlights of another vehicle coming towards you what should you do?", 'Look to the left of the road', "Look to the centre of the road", "Wear sunglasses that have sufficient strength", 'Look to the right side of the road', 'Look to the left of the road',1],
    }

class QuizStarter:
    def __init__(self, parent):
        # Sets window background colour to a dark red.
        background_colour="#C73D2D"

        # Sets up frame.
        self.quiz_frame = Frame(parent, bg = background_colour, padx=100, pady=100)
        self.quiz_frame.grid()

        # Heading label widget.
        self.heading_label = Label(self.quiz_frame, text = "Quiz", font=("Futura", "18", "bold"), bg=background_colour)
        self.heading_label.grid(row=0, padx=20)

        # Username label.
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Futura", "16"), bg=background_colour)
        self.user_label.grid(row=1, padx=20, pady=20)

        # Answer entry box.
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)

        # Continue button.
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Roboto Slab", "13", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)


    def name_collection(self):
        name=self.entry_box.get()
        # Adds name entered earlier into previously empty names dictionary.
        names.append(name)
        # Closes starter window.
        self.quiz_frame.destroy()
        Quiz(root)


class Quiz:
    def __init__(self, parent):
        # Sets window background colour to a dark red.
        background_colour="#C73D2D"

        # Sets up frame.
        self.quiz_frame = Frame(parent, bg = background_colour, padx=100, pady=100)
        self.quiz_frame.grid()

        # Stores radio button values.
        self.var1=IntVar()
        randomiser()

        # Heading label widget.
        self.question_label = Label(self.quiz_frame, text=questions_answers [qnum][0], font=("Futura", "18", "bold"), bg=background_colour)
        self.question_label.grid(row=0, padx=20)

        # Radio button 1.
        self.rb1= Radiobutton(self.quiz_frame, text=questions_answers [qnum][1], font=("Helvetica", "12"), bg=background_colour, value=1, padx=10, pady=10,
            variable=self.var1, indicator = 0, background = "light blue")
        self.rb1.grid(row=1, sticky=W)

        # Radio button 2.
        self.rb2= Radiobutton(self.quiz_frame, text=questions_answers [qnum][2], font=("Helvetica", "12"), bg=background_colour, value=2, padx=10, pady=10,
            variable=self.var1, indicator = 0, background = "light blue")
        self.rb2.grid(row=2, sticky=W)

        # Radio button 3.
        self.rb3= Radiobutton(self.quiz_frame, text=questions_answers [qnum][3], font=("Helvetica", "12"), bg=background_colour, value=3, padx=10, pady=10,
            variable=self.var1, indicator = 0, background = "light blue")
        self.rb3.grid(row=3, sticky=W)

        # Radio button 4.
        self.rb4= Radiobutton(self.quiz_frame, text=questions_answers [qnum][4], font=("Helvetica", "12"), bg=background_colour, value=4, padx=10, pady=10,
            variable=self.var1, indicator = 0, background = "light blue")
        self.rb4.grid(row=4, sticky=W)

        # Confirm button.
        self.quiz_instance = Button(self.quiz_frame, text="Confirm.", font=("Roboto Slab", "13", "bold"), bg="SpringGreen3", command=self.test_progress)
        self.quiz_instance.grid(row=7, padx=5, pady=5)

        # Score label.
        self.score_label=Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT", "16"), bg=background_colour)
        self.score_label.grid(row=8, padx=10, pady=1)

    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        self.rb4.config(text=questions_answers[qnum][4])
    
    def test_progress(self):
        # Makes this function use the score variable from the start.
        global score
        # Renames the score label every time the score changes.
        scr_label=self.score_label
        # Gets the user's answer choice.
        choice=self.var1.get()
        # Checks if it's the last question, and if so, ends the quiz afterwards.
        if len(asked)>9:
            if choice == questions_answers[qnum][6]:
                score = score + 1
                # Changes score label each time the score changes to the new one.
                scr_label.configure(text=score)
                self.quiz_instance.config(text="Confirm.")
            else:
                # Score stays the same because the user's answer was incorrect.
                score+=0
                scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5] )
                self.quiz_instance.config(text="Confirm.")
        # If the length of the asked list is 9 questions or less, which means there are still questions to be asked.
        else:
            # If the user presses confirm without selecting an option.
            if choice == 0:
                self.quiz_instance.config(text="Please try again and select an option.")
                choice = self.var1.get()
            # If the user did make a choice.
            else:
                # If the user's choice is correct.
                if choice == questions_answers [qnum][6]:
                    score = score + 1
                    scr_label.configure(text=score)
                    self.questions_setup()
                # If the user's choice was incorrect.
                else:
                    score+=0
                    scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5] )
                    self.quiz_instance.config(text="Confirm.")
                    self.questions_setup()






def randomiser():
    # Makes this function used the qnum variable from elsewhere.
    global qnum
    # Picks a random order of questions.
    qnum = random.randint (1,10)
    # Checks question selected against previously asked question so they're not asked twice.
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()

# Start of program.
if __name__ == "__main__":
    root = Tk()
    # Title of window.
    root.title("Quiz")
    # Makes an instance of the Quiz class.
    quiz_instance = QuizStarter(root)
    # Keeps window from closing.
    root.mainloop()
