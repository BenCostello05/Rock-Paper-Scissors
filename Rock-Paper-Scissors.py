#This program is the game rock paper scissors. It has a singleplayer, multiplayer and simluation mode. You can also look at the
#graphs for how many times each were used in each gamemode.

#Author: Ben Costello

#This creates the windows for the game
from tkinter import *
import random
import statistics

#Allows you to change the background colour of buttons using tkinter on mac
from tkmacosx import Button

#Used to create the graphs
import matplotlib.pyplot as plt
import csv

counterrock1 = 0
counterpaper1 = 0
counterscissors1 = 0

counterrock2 = 0
counterpaper2 = 0
counterscissors2 = 0

counterrock3 = 0
counterpaper3 = 0
counterscissors3 = 0

def main():
    rootm = Tk()
    
    #Creates homes screen
    rootm.geometry("400x340")
 
    rootm.title("Rock Paper Scissors Game")

    Label(rootm,text="Rock Paper Scissors",font="normal 20 bold",fg="green").pack(padx=10, pady=10)

    Label(rootm,text="Main Menu",font="normal 20",fg="blue").pack(padx=10, pady=10)
    
    #This function will close the game
    def destroym():
        rootm.destroy()
    
    #This function is for the graphs and holds all the code to make each mode's graph
    def graphmenu():
        
        #Creates the graph menu
        rootg = Tk()
        
        rootg.geometry("487x250")
        
        rootg.title("Rock Paper Scissors Game")
        
        Label(rootg,text="Rock Paper Scissors",font="normal 20 bold",fg="green").pack(pady=10)
        
        Label(rootg,text="Graphs",font="normal 20",fg="blue").pack(pady=10)
        
        #This function creates the graphs for the singleplayer mode
        def graphs():
            
            #Creates a list to store the count of each rock, paper and scissors.
            count  = [ ["Rock",counterrock1],["Paper",counterpaper1],["scissors", counterscissors1]]
            
            #Creates a csv file for the singleplayer mode
            filename = "singleplayer_count.csv"
            
            #Puts  the list count (the amount of times rock,paper and scissors shows up in singleplayer)
            #in the CSV file to make a graph
            with open(filename, "w") as csvfile:
            
                csvw = csv.writer(csvfile)
            
                csvw.writerows(count)
        
            xs = []
            ys = []
        
            with open(filename, "r") as csvfile:
                graph = csv.reader(csvfile, delimiter = ",")
            
            #Reading each piece of data in the file and putting it into the lists for the x-axis and y-axis
                for section in graph:
                    if section:
                        xs.append(section[0]) #The names of rock, paper and scissors
                        ys.append(section[1]) #The amount each were used
            
            #Converting the numbers from strings to integers
            y_int=[]
            for a in ys:
                a=int(a)
                y_int.append(a)
     
            
            #Calculating the mean of the numbers
            mean = statistics.mean(y_int)
            
            #Plotting the data onto the graph, labelling the x and y axis and showing it on screen
            plt.bar(xs, y_int, color ="black", width = 0.5, label = "= Frequency")
            plt.xlabel("Options")
            plt.ylabel("How many times each appeared")
            plt.legend( title = "Mean = " + str(mean))
            plt.title("How many times each option was selected in Singleplayer")
            plt.show()
            
            #End of graphs function
        
        #This function creates the graphs for the multiplayer mode
        def graphm():
            
            #Creates a list to store the count of each rock, paper and scissors.
            countm  = [ ["Rock",counterrock2], ["Paper",counterpaper2], [ "Scissors",counterscissors2]]
        
            #Creates a csv file for the multiplayer mode        
            filename = "multiplayer_count.csv"
            
            #Puts  the list count (the amount of times rock,paper and scissors shows up in multiplayer)
            #in the CSV file to make a graph
            with open(filename, "w") as csvfile:
            
                csvw = csv.writer(csvfile)
    
                csvw.writerows(countm)
        
            xm = []
            ym = []
        
            with open(filename, "r") as csvfile:
                graph = csv.reader(csvfile, delimiter = ",")
                
            #Reading each piece of data in the file and putting it into the lists for the x-axis and y-axis
                for section in graph:
                    if section:
                        xm.append(section[0])
                        ym.append(section[1])
        
            y_intm=[]
            
            #Converting the numbers from strings to integers
            for am in ym:
                am = int(am)
                y_intm.append(am)
            
            #Calcualting the mean of the numbers
            meanm = statistics.mean(y_intm)
            
            #Plotting the data onto the graph, labelling the x and y axis and showing it on screen        
            plt.bar(xm, y_intm, color ="black", width = 0.5, label = "= Frequency")
            plt.xlabel("Options")
            plt.ylabel("How many times each were selected")
            plt.legend(title = "Mean = " + str(meanm))
            plt.title("How many times each option was selected in Multiplayer")
            plt.show()
            
            #End of graphm function
            
            
        #This function creates the graphs for the multiplayer mode
        def graphsim():
            
            #Creates a list to store the count of each rock, paper and scissors.
            countsim  = [ ["Rock",counterrock3], ["Paper",counterpaper3], [ "Scissors",counterscissors3]]
            
            #Creates a csv file for the simulation mode
            filename = "simulation_count.csv"
            
            #Puts  the list count (the amount of times rock,paper and scissors shows up in simulation)
            #in the CSV file to make a graph
            with open(filename, "w") as csvfile:
            
                csvw = csv.writer(csvfile)
            
                csvw.writerows(countsim)
        
            xsim = []
            ysim = []
        
            with open(filename, "r") as csvfile:
                graph = csv.reader(csvfile, delimiter = ",")
                
                #Reading each piece of data in the file and putting it into the lists for the x-axis and y-axis
                for section in graph:
                    if section:
                        xsim.append(section[0])
                        ysim.append(section[1])
        
            y_intsim=[]
            
            #Converting the numbers from strings to integers
            for asim in ysim:
                asim = int(asim)
                y_intsim.append(asim)
            
            #Calculating the mean of the numbers
            meansim = statistics.mean(y_intsim)
            
            #Plotting the data onto the graph, labelling the x and y axis and showing it on screen
            plt.bar(xsim, y_intsim, color ="black", width = 0.5, label = "= Frequency")
            plt.xlabel("Options")
            plt.ylabel("How many times each were selected")
            plt.legend(title = "Mean = " + str(meansim))
            plt.title("How many times each option was selected in Simulation mode")
            plt.show()
            
            #End of graphsim function
        
        
        #This closes the graph menu
        def destroyg():
            rootg.destroy()
        
        #Button to go back to the main menu
        btgmenu = Button(rootg, text="Main Menu",font=10, width='5c',fg="red",bg="yellow",command=lambda: [destroyg(),main()]).pack(side=BOTTOM,padx=10,pady= 10)
        
        #Button to open the singleplayer graph
        btgsingle = Button(rootg,text="Graph Singleplayer", font=10, width='5c',bg='black', fg="white",command=graphs ).pack(side=LEFT, padx=10, pady=10)
        
        #Button to open the multiplayer graph
        btgmulti = Button(rootg,text="Graph Multiplayer",font=10, width='5c',bg='purple', fg="white",command=graphm ).pack(side=LEFT, padx=10, pady=10)
        
        #Button to open the simulation graph
        btgsim = Button(rootg,text="Graph Simulation",font=10, width='5c',bg='#cc5500', fg="white",command=graphsim ).pack(side=LEFT, padx=10, pady=10)
        
        rootg.mainloop()
        #End of graph menu function
        
    
    #This function is for the singleplayer mode. It holds all the code for the mode to run
    def singleplayer():
        
        #Creates the singleplayer menu        
        roots = Tk()
        roots.geometry("488x350")

        roots.title("Rock Paper Scissors Game")
    
        Label(roots,text="Rock Paper Scissors",font="normal 25 bold",fg="green").pack(padx=10, pady=10)

        Label(roots,text="Player VS Computer",font="normal 25",fg="blue").pack(padx=10,pady=10)
        
        lsp = Label(roots,text="",font="normal 20",fg="red")
        lsp.pack(padx=10,pady=10)
        
        #A list of the options the computer can choose from
        computer = ["Rock", "Paper", "Scissors"]
    
        lsr = Label(roots,text="",font="normal 20",fg="grey", width=20,height=1, borderwidth=2, relief="ridge")
        lsr.pack(padx=10,pady=10)

        
        #This closes the singleplayer menu
        def destroys():
            roots.destroy()
        
        #This function is used when the player chooses rock
        def rock():
            value = random.choice(computer) #Computer randomly selects a option from the list
            lsp.configure(text = "Rock vs " + value) #Outputs the Computers option to screen alongside the players choice

            #Made them global so the whole program can see the changes to the variables
            global counterrock1
            global counterscissors1
            global counterpaper1
            counterrock1 = counterrock1 + 1 #Adds on to the counter for rocks for the singleplayer graphs
            
            #This if-elif-else statement checks who won depending on the computers choice and adds one to that options counter
            if value == "Scissors":
                result = "Player Won"
                counterscissors1 = counterscissors1 + 1
            elif value == "Rock":
                result = "Draw"
                counterrock1 = counterrock1 + 1
            else:
                result = "Computer Won"
                counterpaper1 = counterpaper1 + 1
            lsr.config(text=result)
        
        #This function is used when the player chooses scissors
        def scissors():
            value = random.choice(computer) #Computer randomly selects a option from the list
            lsp.configure(text = "Scissors vs " + value) #Outputs the Computers option to screen alongside the players choice
            
            #Made them global so the whole program can see the changes to the variables
            global counterscissors1
            global counterpaper1
            global counterrock1
            counterscissors1 = counterscissors1 + 1 #Adds one to the counter for scissors for the singleplayer graphs
            
            #This if-elif-else statement checks who won depending on the computers choice and adds one to that options counter
            if value == "Paper":
                result = "Player Won"
                counterpaper1 = counterpaper1 + 1
            elif value == "Scissors":
                result = "Draw"
                counterscissors1 = counterscissors1 + 1
            else:
                result = "Computer Won"
                counterrock1 = counterrock1 + 1
            lsr.config(text=result)
        
         #This function is used when the player chooses scissors
        def paper():
            value = random.choice(computer) #Computer randomly selects a option from the list
            lsp.configure(text = "Paper vs " + value) #Outputs the Computers option to screen alongside the players choice
            
            #Made them global so the whole porgram can see the changes to the variables
            global counterpaper1
            global counterscissors1
            global counterrock1
            counterpaper1 = counterpaper1 + 1 #Adds one to the counter for paper for the singleplayer graphs
            
            #This if-elif-else statement checks who won depending on the computers choice and adds one to that options counter
            if value == "Rock":
                result = "Player Won"
                counterrock1 = counterrock1 + 1
            elif value == "Paper":
                result = "Draw"
                counterpaper1 = counterpaper1 + 1
            else:
                result = "Computer Won"
                counterscissors1 = counterscissors1 + 1
            lsr.config(text=result)
        
        #Button to go back to the main menu
        btm = Button(roots, text="Main Menu",font=20, width='5c',fg="red",bg="yellow",command=lambda: [destroys(),main()]).pack(side=BOTTOM,padx=10,pady= 0)
        
        #These buttons allow the player to input their choice either rock,paper or scissors
        btr = Button(roots, text="Rock",font="normal 20",width='5c',height='1c',fg="white", bg="black",command=rock).pack(side=LEFT,padx=10,pady=0)
        btp = Button(roots, text="Paper",font="normal 20", width='5c', height = '1c',fg="white", bg="black", command=paper).pack(side=LEFT,padx=10,pady=0)
        bts = Button(roots, text="Scissors",font="normal 20", width='5c', height = '1c',fg="white", bg="black", command=scissors).pack(side=LEFT,padx=10,pady= 0)
    
        roots.mainloop()
        #End of singleplayer function
    
    #This function is for the multiplayer mode. It holds all the code to run the mode
    def two():
        
        #Creates the two-player menu    
        roott = Tk()
        roott.geometry("520x320")

        roott.title("Rock Paper Scissors Game")
    
        Label(roott,text="Rock Paper Scissors",font="normal 20 bold",fg="green").pack(padx=10, pady=10)

        lsshow= Label(roott,text="Player 1 VS Player 2",font="normal 20",fg="blue")
        lsshow.pack(padx=10,pady=10)
        
        computer = ["Rock", "Paper", "Scissors"]
    
        lsa = Label(roott,text="Player 1's Turn",font="normal 20",fg="grey", width=20,height=1, borderwidth=2, relief="ridge")
        lsa.pack(padx=10,pady=10)
        
        #This creates an enter box on screen so the players can enter the choice
        chose = Entry(roott, width=20)
        chose.pack(padx=10,pady=10)
        
        #Resets the mode so the two player's can play again/restart   
        def restart():
            lsa.configure(text="Player One's Turn")
            bte.configure(text="Press to Submit", command=player1)
            chose.config(state="normal")
            lsshow.configure(text="Player 1 VS Player 2")
        
        #This function is for when player one enters rock into the box and player 2 has entered their choice
        def p1rock():
            #This deletes what was typed into the entry box and disbles it so no one else can type in it.
            chose.delete(0,END)
            chose.config(state="disabled")
            lsshow.configure(text=player1a + " VS "+ player2a)
            #Made them global so the whole porgram can see the changes to the variables
            global counterscissors2
            global counterrock2
            global counterpaper2
            counterrock2 = counterrock2 + 1 #adds one to the rock counter for the multiplayer graphs
            if player2a =="Rock": #If player 2 enters rock
                lsa.configure(text="Draw") #Changes label to draw
                counterrock2 = counterrock2 + 1 #Adds one to the rock counter
            elif player2a=="Paper": #If player 2 enters paper
                lsa.configure(text="Player 2 wins")#Changes label to player 2 wins
                counterpaper2 = counterpaper2 + 1 #Adds 1 to the paper counter
            else: #Final option is player 2 enters scissors
                lsa.configure(text="Player 1 wins") #Changes label to player 1 won
                counterscissors2 = counterscissors2 + 1 #Adds 1 to the scissors counter
            bte.configure(text="Play Again", command=restart) #Creates the play again button so they can restart which runs the restart fuction from above
        
        #This function is for when player one enters paper into the box and player 2 has chosen their choice 
        def p1paper():
            #This deletes what was typed into the entry box and disbles it so no one else can type in it.
            chose.delete(0,END)
            chose.config(state="disabled")
            lsshow.configure(text=player1a + " VS "+ player2a)
            global counterscissors2
            global counterrock2
            global counterpaper2
            counterpaper2 = counterpaper2 + 1 #adds one to the paper counter for the multiplayer graphs
            if player2a =="Paper": #If player 2 enters paper
                lsa.configure(text="Draw")
                counterpaper2 = counterpaper2 + 1
            elif player2a=="Scissors": #If player 2 enters scissors
                lsa.configure(text="Player 2 wins")
                counterscissors2 = counterscissors2 + 1
            else: #Final option is if player 2 enters rock
                lsa.configure(text="Player 1 wins")
                counterrock2 = counterrock2 + 1
            bte.configure(text="Play Again", command=restart)
        
        #This function is for when player one enters scissors into the box and player 2 has chosen thier choice
        def p1scissors():
            #This deletes what was typed into the entry box and disbles it so no one else can type in it.
            chose.delete(0,END)
            chose.config(state="disabled")
            lsshow.configure(text=player1a + " VS "+ player2a)
            global counterscissors2
            global counterrock2
            global counterpaper2
            counterscissors2 = counterscissors2 + 1 #adds one to the scissors counter for the multiplayer graphs
            if player2a =="Scissors": #if player 2 enters scissors
                lsa.configure(text="Draw")
                counterscissors2 = counterscissors2 + 1
            elif player2a=="Rock": #If player 2 enters Rock
                lsa.configure(text="Player 2 wins")
                counterrock2 = counterrock2 + 1
            else: #Final option is if player 2 enters paper
                lsa.configure(text="Player 1 wins")
                counterpaper2 = counterpaper2 + 1
            bte.configure(text="Play Again", command=restart)
        
        
        #The answer function checks to see what player 1 entered and runs the function associated with that choice
        def answer():
            if player1a=="Rock":
                p1rock()
            elif player1a=="Paper":
                p1paper()
            elif player1a=="Scissors":
                p1scissors()
        
        #This function takes the answer that player 1 entered makes it lower case and capitalizes it and checks to see if
        #they enetered rock,paper or scissor and if not get them to re-enter.
        def player1():
            global player1a #Global player 1 so the whole progrma can see what they entered
            player1=chose.get() #Puts the word they enetered into the variable player1
            player1l = player1.lower() #Makes the word lowercase
            player1a = player1l.capitalize() #Capitalizes the word
            
            #Checks to see if they entered a correct option and if not gets them to try again.
            if player1a=="Rock" or player1a=="Paper" or player1a=="Scissors":
                #Start's player 2's turn
                lsa.configure(text="Player's Two Turn") 
                bte.configure(command=player2) #Reconfigures the button so that when it sumbits next it will run the player2 function
                chose.delete(0,END)
            else:
                lsa.configure(text="Player one try again")
                chose.delete(0,END)
        
        #This function takes the answer that player 2 entered makes it lower case and capitalizes it and checks to see if
        #they enetered rock,paper or scissor and if not get them to re-enter.
        def player2():
            global player2a
            player2=chose.get()
            player2l = player2.lower()
            player2a = player2l.capitalize()
            #Checks to see if they entered a correct option and if not gets them to try again
            if player2a=="Rock" or player2a=="Paper" or player2a=="Scissors":
                answer() #If so runs the answer function above on line 420 to start the check to see who won
                chose.delete(0,END)
            else:
                lsa.configure(text="Player two try again")
                chose.delete(0,END)
        
        #This button is the submit button so they can submit their answer
        bte = Button(roott,text="Press to submit", font=20, width='5c',fg="white", bg="black", command=player1)
        bte.pack(padx=10,pady=0)
        
        #A message so the plaeyrs know what to enter
        lsc = Label(roott, text="Please enter: Rock or Paper or Scissors", font="normal 20", fg="red",width=30, height=1)
        lsc.pack(padx=10,pady=10)

        
        #This closes the multiplayer menu
        def destroys():
            roott.destroy()
          
        #Main menu button so they can go back to the main menu.
        btm = Button(roott, text="Main Menu",font=20, width='5c',fg="red", bg="yellow",command=lambda: [destroys(),main()]).pack(side=BOTTOM,padx=10,pady= 0)
    
        roott.mainloop()
        #End of two funtion - multiplayer mode
    
    #This function is for the simulation mode - it simulates games of rock,paper,scissors everytime the button is clicked
    def sim():
        
        #Creates the simulation menu
        rootsim = Tk()
        rootsim.geometry("500x300")

        rootsim.title("Rock Paper Scissors Game")
    
        Label(rootsim,text="Rock Paper Scissors",font="normal 20 bold",fg="green").pack(padx=10, pady=10)

        Label(rootsim,text="Computer 1 VS Computer 2 ",font="normal 20",fg="blue").pack(padx=10,pady=10)
        
        lsc = Label(rootsim,text="",font="normal 20",fg="red", width=20,height=1, borderwidth=2)
        lsc.pack(padx=10,pady=10)
        
        lsa = Label(rootsim,text="",font="normal 20",fg="grey", width=20,height=1, borderwidth=2, relief="ridge")
        lsa.pack(padx=10,pady=10)
         
        #A list of the options both computers can choose from
        computer = ["Rock", "Paper", "Scissors"]
        
        #This function runs when Computer 1 chooses rock
        def simrock():
            computer2= random.choice(computer) #Computer two chooses a random choice from the list computer (line 499)
            lsc.configure(text=computer1 + " vs " + computer2) #Outputs what each computer chose to screen
            
            #Made them global so the whole porgram can see the changes to the variables
            global counterpaper3
            global counterrock3
            global counterscissors3
            counterrock3 = counterrock3 + 1 #Adds one to the rock counter for the simulation graphs
            if computer2=="Rock": #If computer 2 chooses rock
                lsa.configure(text="Draw") #Outputs result of game to screen
                counterrock3 = counterrock3 + 1 #Adds one to the counter for rock
            elif computer2=="Paper": #If computer 2 chooses paper
                lsa.configure(text="Computer 2 Wins")
                counterpaper3 = counterpaper3 + 1
            else: #Final option is if computer 2 chooses scissors
                lsa.configure(text="Computer 1 Wins")
                counterscissors3 = counterscissors3 + 1
                
        #This function is runs when computer 1 chooses paper
        def simpaper():
            computer2= random.choice(computer) #Computer two chooses a random choice from the list computer (line 499)
            lsc.configure(text=computer1 + " vs " + computer2)
            global counterpaper3
            global counterrock3
            global counterscissors3
            counterpaper3 = counterpaper3 + 1 #Adds one to the paper counter for the simulation graphs
            if computer2=="Paper": #If computer 2 chooses paper
                lsa.configure(text="Draw")
                counterpaper3 = counterpaper3 + 1
            elif computer2=="Scissors": #If computer 2 chooses scissors
                lsa.configure(text="Computer 2 Wins")
                counterscissors3 = counterscissors3 + 1
            else: #Final option is if computer 2 chooses rock
                lsa.configure(text="Computer 1 Wins")
                counterrock3 = counterrock3 + 1
        
        #This function is runs when computer 1 chooses scissors
        def simscissors():
            computer2= random.choice(computer) #Computer two chooses a random choice from the list computer (line 499)
            lsc.configure(text=computer1 + " vs " + computer2)
            global counterpaper3
            global counterrock3
            global counterscissors3
            counterscissors3 = counterscissors3 + 1 #Adds one to the scissors counter for the simulation graphs
            if computer2=="Scissors": #If computer 2 chooses scissors
                lsa.configure(text="Draw")
                counterscissors3 = counterscissors3 + 1
            elif computer2=="Rock": #If computer 2 chooses rock
                lsa.configure(text="Computer 2 Wins")
                counterrock3 = counterrock3 + 1
            else: #If computer 2 chooses paper
                lsa.configure(text="Computer 1 Wins")
                counterpaper3 = counterpaper3 + 1
        
        #This function gets computer 1 to choose a random choice from the list computer (line 499) and then depending on
        # what it chose runs the associated function for that choice.
        def simulate():
            #Make computer1 global so the whole program can see any changes.
            global computer1
            computer1 = random.choice(computer) #Computer one chooses a random choice from the list computer (line 499) 
            if computer1 == "Rock":
                simrock()
            elif computer1=="Paper":
                simpaper()
            elif computer1=="Scissors":
                simscissors()
        
        
        #This button simulates a game of rock,paper scissors eveytime clicked - runs the simulate function (line 555)
        btsim = Button(rootsim, text="Simulate",font=10, width='5c',fg="white", bg="black",command=simulate).pack(side=TOP, padx=10, pady=10)
        
        #This closes the simulation menu
        def destroys():
            rootsim.destroy()
          
        #Main menu button so they can go back to the main menu.
        btm = Button(rootsim, text="Main Menu",font=20, width='5c',fg="red", bg="yellow",command=lambda: [destroys(),main()]).pack(side=BOTTOM,padx=10,pady= 0)
        
        rootsim.mainloop()
        #End of sim function
        
    
    #Buttons for the main menu screen
    #Singleplayer button - runs the singleplayer function (line 219)
    bts = Button(rootm, text="Singleplayer",font=10, width='5c',fg="white",bg="black",command= lambda: [destroym(), singleplayer()]).pack(side=TOP, padx=10, pady=10)
    
    #Multiplayer button - runs the two function (line 255)
    btt = Button(rootm, text="Two player",font=10, width='5c',fg="white",bg ="purple",command= lambda: [destroym(), two()]).pack(side=TOP, padx=10, pady=10)
     
    #Simmulation button - runs the sim function (line 480)
    btsim = Button(rootm, text="Simulation mode",font=10, width='5c',bg='#cc5500', fg="white",command= lambda: [destroym(), sim()]).pack(side=TOP, padx=10, pady=10)
    
    #Graph menu button - runs the graphmenu function (line 45)
    btg = Button(rootm, text="Graph",font=10, width='5c',bg='#808080', fg="white",command= lambda: [destroym(), graphmenu()]).pack(side=TOP, padx=10, pady=10)
    
    #Exit the game button - runs the destroym function (line 41)
    bte = Button(rootm, text="Exit Game",font=10, width='5c',fg="red", bg="yellow",command=destroym).pack(side=TOP, padx=10, pady=10)
 

    rootm.mainloop()

main() #End of program