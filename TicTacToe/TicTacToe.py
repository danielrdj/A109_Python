########################################################################################################################
# Daniel Johnson
# Assignment 5
# 4/4/2019
#
# Description: This is a graphical version of tic-tac-toe using tkinter. Making a graphical version eliminated the need
#              to create buttons for: adding a move (completed by clicking a square), updating board, determining whose
#              turn it is, and declaring the winner. These were all eliminated by completing the task automatically or
#              showing the board graphically. The "Restart Game" button was implemented because it could not be
#              eliminated. Have fun playing.
#
#              Note: a & b were implemented using one function ("_add_move()") it did not make sense to me to separate
#              these two functions in this situation.
#
#
# Inputs: The user must click and choose his/her square and then wait while their opponent does the same. There
#         is also an option to restart/reinitialize the game as well if you press a button next to the board.
#
# Outputs: This outputs a GUI and the rules for the game tic-tac-toe and also outputs the move that a player enters
#          every time they click an available square. The game has a text section that output who's move it is or if
#          someone has won.
#
# Picture resources:
#       O: https://www.pngarts.com/files/2/Letter-O-Transparent-Background-PNG.png
#       X: https://www.pngkey.com/png/full/128-1281692_rounded-x-black-x-clipart.png
#       White box: Created using a screenshot tool.
#
########################################################################################################################
from tkinter import *



class TicTacToe:

    ########################################
    # Description: This initializes the GUI,
    # instance variables, and the game board
    # for tic-tac-toe.
    #
    # Inputs: This function takes no inputs
    # other than the user inputs from the GUI
    # when clicking.
    #
    # Returned value: There is no returned
    # value.
    #
    # Preconditions: None.
    ########################################
    def __init__(self):

        # Holds the game board in a 2d list for easy board tracking
        self.list_game_board = [["n","n","n"],
                           ["n","n","n"],
                           ["n","n","n"]]


        # Window setup##############################################
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.minsize(width=750, height=425)
        self.window.maxsize(width=750, height=425)
        self.window.configure(background="dark grey")
        # Window setup##############################################


        # Board ####################################################
        self.frame_frame_frame = Frame(self.window, bd=5, bg="dark grey", width=500, height=400, padx=15, pady=15)
        self.frame_frame_frame.grid(row=0, column=1)
        self.frame_frame = Frame(self.frame_frame_frame, bd=5, relief="groove", bg="black", width=350, height=350)
        self.frame_frame.pack()

        self.white_box = PhotoImage(file="WhiteBox.png")  # Initialization of white placeholder picture
        self.o_image = PhotoImage(file="O.png")  # Initialization of O's picture
        self.x_image = PhotoImage(file="X.png")  # Initialization of X's picture

        # First Row on board #####
        # Label frames
        self.frame1 = Frame(self.frame_frame, bg="white")
        self.frame2 = Frame(self.frame_frame, bg="white")
        self.frame3 = Frame(self.frame_frame, bg="white")

        # Labels
        self.label1 = Label(self.frame1, image=self.white_box, bg="white")
        self.label2 = Label(self.frame2, image=self.white_box, bg="white")
        self.label3 = Label(self.frame3, image=self.white_box, bg="white")

        # Label events
        self.label1.bind("<Button>", lambda e: self._add_move(1))
        self.label2.bind("<Button>", lambda e: self._add_move(2))
        self.label3.bind("<Button>", lambda e: self._add_move(3))

        # Label packing
        self.label1.pack(expand=False)
        self.label2.pack(expand=False)
        self.label3.pack(expand=False)

        # Adding framed labels to board
        self.frame1.grid(row=0, column=0, padx=(0, 12.5), pady=(0, 12.5))
        self.frame2.grid(row=0, column=1, padx=(12.5, 12.5), pady=(0, 12.5))
        self.frame3.grid(row=0, column=2, padx=(12.5, 0), pady=(0, 12.5))
        # First Row on board #####

        # Second Row on board ####
        # Label frames
        self.frame4 = Frame(self.frame_frame, bg="white")
        self.frame5 = Frame(self.frame_frame, bg="white")
        self.frame6 = Frame(self.frame_frame, bg="white")

        # Labels
        self.label4 = Label(self.frame4, image=self.white_box, bg="white")
        self.label5 = Label(self.frame5, image=self.white_box, bg="white")
        self.label6 = Label(self.frame6, image=self.white_box, bg="white")

        # Label events
        self.label4.bind("<Button>", lambda e: self._add_move(4))
        self.label5.bind("<Button>", lambda e: self._add_move(5))
        self.label6.bind("<Button>", lambda e: self._add_move(6))

        # Label packing
        self.frame4.grid(row=1, column=0, padx=(0, 12.5), pady=(12.5, 12.5))
        self.frame5.grid(row=1, column=1, padx=(12.5, 12.5), pady=(12.5, 12.5))
        self.frame6.grid(row=1, column=2, padx=(12.5, 0), pady=(12.5, 12.5))

        # Adding framed labels to board
        self.label4.pack(expand=False)
        self.label5.pack(expand=False)
        self.label6.pack(expand=False)
        # Second Row on board ####

        # Third Row on board #####
        # Label frames
        frame7 = Frame(self.frame_frame, bg="white")
        frame8 = Frame(self.frame_frame, bg="white")
        frame9 = Frame(self.frame_frame, bg="white")

        # Labels
        self.label7 = Label(frame7, image=self.white_box, bg="white")
        self.label8 = Label(frame8, image=self.white_box, bg="white")
        self.label9 = Label(frame9, image=self.white_box, bg="white")

        # Label events
        self.label7.bind("<Button>", lambda e: self._add_move(7))
        self.label8.bind("<Button>", lambda e: self._add_move(8))
        self.label9.bind("<Button>", lambda e: self._add_move(9))

        # Label packing
        self.label7.pack(expand=False)
        self.label8.pack(expand=False)
        self.label9.pack(expand=False)

        # Adding framed labels to board
        frame7.grid(row=2, column=0, padx=(0, 12.5), pady=(12.5, 0))
        frame8.grid(row=2, column=1, padx=(12.5, 12.5), pady=(12.5, 0))
        frame9.grid(row=2, column=2, padx=(12.5, 0), pady=(12.5, 0))
        # Third Row on board #####
        # Board ####################################################



        # Menu ####################################################
        self.menu_frame_frame = Frame(self.window, bg="black", relief="raised", bd=15, width=250, height=500)
        self.menu_frame_frame.grid(row=0, column=0, padx=(5, 0))

        self.menu_frame = Frame(self.menu_frame_frame, padx=25, pady=25)
        self.menu_frame.pack()

        self.menu_label = Label(self.menu_frame, text="Tic-Tac-Toe", font="Times 30 bold")
        self.menu_label.grid(row=0, column=0, padx=5, pady=(0, 20))


        self.restart_game_button = Button(self.menu_frame, command=self._reinitialize_game, text="Restart Game", font="Times 15", padx=5, pady=5, width=20)
        self.restart_game_button.grid(row=1, column=0)


        self.text_box = Text(self.menu_frame, font="Times 8", width=39, height=11)
        self.text_box.grid(row=3, column=0, pady=(10, 0))
        rule1 = "1. X's goes first and O's go second."
        rule2 = "2. First player to get their three consecutive shapes wins."
        rule3 = "3. If nobody gets three consecutive shapes the game ends with a draw."
        have_fun = "Have fun! (Click a square to start)"
        self.rules = "Rules:" + "\n" + rule1 + "\n" + rule2 + "\n" + rule3 + "\n\n" + have_fun
        self.text_box.insert(INSERT, self.rules)
        self.text_box.config(state="disabled")
        # Menu ####################################################

        # Creates window mainloop
        self.window.mainloop()
        # Creates window mainloop


    #a. add a move
    #b. display the board
    ########################################
    # Description: This adds a move and
    # updates the game board at the same time.
    #
    # Inputs: This takes a number (1-9) as
    # inputs to determine which square was
    # chosen as the move of the user.
    #
    # Returned value: There is no returned
    # value.
    #
    # Preconditions: None; if num is not
    # within the given threshold (1-9), the
    # function will not break.
    ########################################
    def _add_move(self, num):

        winner = self._determine_if_winner()
        if winner == "x" or winner == "o" or winner == "none":
            return

        # Function to retrieve the letter and picture of letter for the if and elif statements below
        def _get_letter():
            if self._determine_turn():
                temp_image = self.x_image
                letter = "x"
                return [letter,temp_image]
            else:
                temp_image = self.o_image
                letter = "o"
                return [letter,temp_image]

        if num == 1 and self.list_game_board[0][0] == "n":
            temp = _get_letter()
            temp_letter = temp[0]
            temp_image = temp[1]
            self.label1.config(image=temp_image)
            self.list_game_board[0][0] = temp_letter
        elif num == 2  and self.list_game_board[0][1] == "n":
            temp = _get_letter()
            temp_letter = temp[0]
            temp_image = temp[1]
            self.label2.config(image=temp_image)
            self.list_game_board[0][1] = temp_letter
        elif num == 3  and self.list_game_board[0][2] == "n":
            temp = _get_letter()
            temp_letter = temp[0]
            temp_image = temp[1]
            self.label3.config(image=temp_image)
            self.list_game_board[0][2] = temp_letter
        elif num == 4 and self.list_game_board[1][0] == "n":
            temp = _get_letter()
            temp_letter = temp[0]
            temp_image = temp[1]
            self.label4.config(image=temp_image)
            self.list_game_board[1][0] = temp_letter
        elif num == 5 and self.list_game_board[1][1] == "n":
            temp = _get_letter()
            temp_letter = temp[0]
            temp_image = temp[1]
            self.label5.config(image=temp_image)
            self.list_game_board[1][1] = temp_letter
        elif num == 6 and self.list_game_board[1][2] == "n":
            temp = _get_letter()
            temp_letter = temp[0]
            temp_image = temp[1]
            self.label6.config(image=temp_image)
            self.list_game_board[1][2] = temp_letter
        elif num == 7 and self.list_game_board[2][0] == "n":
            temp = _get_letter()
            temp_letter = temp[0]
            temp_image = temp[1]
            self.label7.config(image=temp_image)
            self.list_game_board[2][0] = temp_letter
        elif num == 8 and self.list_game_board[2][1] == "n":
            temp = _get_letter()
            temp_letter = temp[0]
            temp_image = temp[1]
            self.label8.config(image=temp_image)
            self.list_game_board[2][1] = temp_letter
        elif num == 9 and self.list_game_board[2][2] == "n":
            temp = _get_letter()
            temp_letter = temp[0]
            temp_image = temp[1]
            self.label9.config(image=temp_image)
            self.list_game_board[2][2] = temp_letter
        else:
            self.text_box.config(state="normal")
            self.text_box.insert(INSERT, "\nYou played an invalid move; please choose again.")
            self.text_box.config(state="disabled")
            self.text_box.see("end")
        self._determine_if_winner()
            #print(self.list_game_board)


    #c. determine whose turn it is (X or O)
    ########################################
    # Description: This determines whose
    # turn it is during the game by counting
    # the moves on the 2d board
    #
    # Inputs: This does not take input
    #
    # Returned value: This returns True
    # when it is X's turn and False when
    # it is O's turn
    #
    # Preconditions: None
    ########################################
    def _determine_turn(self):
        x_count = 0
        o_count = 0
        # Counts all X's and O's
        for listing in self.list_game_board:
            for place in listing:
                if place == "x":
                    x_count += 1
                elif place == "o":
                    o_count +=1
        # Determines it is X's turn and signals that it is O's turn because X's turn will be fulfilled
        if x_count == 0 and o_count == 0:
            self.text_box.config(state= "normal")
            self.text_box.insert(INSERT, "\n" + "It is O's turn.")
            self.text_box.config(state="disabled")
            self.text_box.see("end")
            return True
        # Determines it is O's turn and signals that it is X's turn because O's turn will be fulfilled
        elif x_count > o_count:
            self.text_box.config(state="normal")
            self.text_box.insert(INSERT, "\n" + "It is X's turn.")
            self.text_box.config(state="disabled")
            self.text_box.see("end")
            return False
        # Determines it is X's turn and signals that it is O's turn because X's turn will be fulfilled
        else:
            self.text_box.config(state="normal")
            self.text_box.insert(INSERT, "\n" + "It is O's turn.")
            self.text_box.config(state="disabled")
            self.text_box.see("end")
            return True


    #d. determine if there is a winner
    ########################################
    # Description: This determines if there
    # is a winner during the game.
    #
    # Inputs: This does not take input
    #
    # Returned value: This returns "x" if
    # X is the winner and "o" if O is the
    # winner
    #
    # Preconditions: None
    ########################################
    def _determine_if_winner(self):
        #Checks rows for winner
        for x in range(3):
            count_o = 0
            count_x = 0
            for y in range(3):
                if self.list_game_board[x][y] == "x":
                    count_x += 1
                elif self.list_game_board[x][y] == "o":
                    count_o += 1
                # Checks for 3 in a row
                if count_o == 3:
                    self._declare_winner("o")
                    return "o"
                elif count_x == 3:
                    self._declare_winner("x")
                    return "x"
        #Checks columns for winner
        for y in range(3):
            count_o = 0
            count_x = 0
            for x in range(3):
                if self.list_game_board[x][y] == "x":
                    count_x += 1
                elif self.list_game_board[x][y] == "o":
                    count_o += 1
                # Checks for 3 in a row
                if count_o == 3:
                    self._declare_winner("o")
                    return "o"
                elif count_x == 3:
                    self._declare_winner("x")
                    return "x"


        #Checks both diagonals for winner
        if self.list_game_board[0][0] == "x" and self.list_game_board[1][1] == "x" and self.list_game_board[2][2] == "x":
            self._declare_winner("x")
            return "x"
        elif self.list_game_board[0][0] == "o" and self.list_game_board[1][1] == "o" and self.list_game_board[2][2] == "o":
            self._declare_winner("o")
            return "o"
        elif self.list_game_board[0][2] == "x" and self.list_game_board[1][1] == "x" and self.list_game_board[2][0] == "x":
            self._declare_winner("x")
            return "x"
        elif self.list_game_board[0][2] == "o" and self.list_game_board[1][1] == "o" and self.list_game_board[2][0] == "o":
            self._declare_winner("o")
            return "o"

        count = 0
        for x in range(3):
            for y in range(3):
                if self.list_game_board[x][y] == "n":
                    count += 1
        if count == 0:
            self._declare_winner("none")
            return "none"


    #e. say who the winner is
    ########################################
    # Description: This declares the winner
    # when called. It will declare X is
    # the winner, O is the winner, or
    # no one has won. This depends on the
    # input.
    #
    # Inputs: This takes a string as input.
    #
    # Returned value: This returns no value.
    #
    # Preconditions: None.
    ########################################
    def _declare_winner(self, letter):
        if letter == "x":
            self.text_box.config(state="normal")
            self.text_box.insert(INSERT, "\n" + "X won!!" + "\n" + "Start a new game by pressing the restart button!")
            self.text_box.config(state="disabled")
            self.text_box.see("end")
        elif letter == "o":
            self.text_box.config(state="normal")
            self.text_box.insert(INSERT, "\n" + "O won!!" + "\n" + "Start a new game by pressing the restart button!")
            self.text_box.config(state="disabled")
            self.text_box.see("end")
        elif letter == "none":
            self.text_box.config(state="normal")
            self.text_box.insert(INSERT, "\n" + "Nobody won this game :(" + "\n" + "Start a new game by pressing the restart button!")
            self.text_box.config(state="disabled")
            self.text_box.see("end")


    #f. reinitialize the game to the beginning
    ########################################
    # Description: This resets the graphical
    # game board and the 2D list game board.
    #
    # Inputs: This takes no input
    #
    # Returned value: This returns no value
    #
    # Preconditions: None; This will always
    # reset the board
    ########################################
    def _reinitialize_game(self):
        #print(self.list_game_board)
        for x in range(len(self.list_game_board)):
            for y in range(len(self.list_game_board[x])):
                self.list_game_board[x][y] = "n"
        #print(self.list_game_board)
        self.label1.config(image= self.white_box)
        self.label2.config(image=self.white_box)
        self.label3.config(image=self.white_box)
        self.label4.config(image=self.white_box)
        self.label5.config(image=self.white_box)
        self.label6.config(image=self.white_box)
        self.label7.config(image=self.white_box)
        self.label8.config(image=self.white_box)
        self.label9.config(image=self.white_box)

        self.text_box.config(state="normal")
        self.text_box.delete("0.0", END)
        self.text_box.insert(INSERT, self.rules)
        self.text_box.config(state="disabled")
        self.text_box.see("end")
    


# Making the class object will start the GUI
ttt = TicTacToe()
