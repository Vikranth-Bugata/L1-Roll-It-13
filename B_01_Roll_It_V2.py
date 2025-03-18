import random


def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")



def instructions():
    """Prints Instructions"""

    print("""
*** Instructions ***

Roll the dice and try to win!
    """)


def int_check():
    """checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("What is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # roll the dice for the user and note if they got a double
    Roll_one = random.randint(1, 6)
    Roll_two = random.randint(1, 6)

    if Roll_one == Roll_two:
        double = "yes"

    total = Roll_one + Roll_two
    print(f"{which_player} - Roll 1: {Roll_one} \t| Roll 2: {Roll_two} \t| Total: {total}) ")

    return total, double


def make_statement(statement, decoration):
    """Adds emoji / additional characters to the starts and end of headings"""

    ends = decoration * 3
    print(f"\n  {ends} {statement} {ends}")

# main starts here...

# At the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0
rounds_played = 0

game_history = []

game_goal = int(input("Game Goal: "))     # should be a function call!
# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()
# Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    rounds_played += 1

    # Start of round loop
    make_statement(statement=f"Round {rounds_played}", decoration="🎲")
    # Roll the dice for the user and note if they got a double
    initial_user = initial_points("User")
    initial_comp = initial_points("Comp")

    # Retrieve user points (first item returned from function)
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # let the user know if they qualify for double points
    if double_user == "yes":
        print("Great news - if you win, you will earn double points!")

    # assume user goes first...
    first = "User"
    second = "Computer"
    player_1_points = user_points
    player_2_points = comp_points

    # if user has fewer points, they start they game
    if user_points < comp_points:
        print("You start because your initial roll was less than the computer\n")

    # if the user and the computer roll equal points, the user is player 1...
    elif user_points == comp_points:
        print("The initial rolls were the same, the user starts!")

    # if the computer has fewer points, switch the computer to 'player 1'
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # Loop until we have a winner...
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Press <enter> to continue this round\n")

        # first person rolls the die and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

        # if the first person's score is over 13, end the round
        if player_1_points >= 13:
            break

        # second person rolls the die (and score is updated)
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points} | {second} {player_2_points}")

    # end of round

    # associate player points with either the user or the computer
    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and computer points if the computer went first
    if first == "Computer":
        user_points, comp_points = comp_points, user_points

    # work out who won and set the users points to zero...
    if user_points > comp_points:
        winner = "user"
        loser = "computer"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"The {winner} won. The {loser}'s points have been reset to zero"

    # double user points if eligible
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # output round results
    make_statement(statement="Round Results", decoration="=")
    print(f"User Points: {user_points} | Computer Points: {comp_points}")
    print(round_feedback)
    print()

    # Outside rounds loop -  Update score with round points, only add points to the score of the
    comp_score += comp_points
    user_score += user_score

    # Generate round results and add it to the history list
    game_results = (f"Round {rounds_played}: User Points {user_points} | "
                    f"Computer Points {comp_points}, {winner} wins (15 | 0)"
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)

    # Show overall scores (add this to rounds loop)
    print("*** Game Update ***")    # replace with call to statement generator
    print(f"User Score: {user_score} | Computer Score: {comp_score}")


# end of entire game, output final results

make_statement(statement= "Game Over", decoration="🏁")

print()
if user_score > comp_score:
    make_statement(statement="The user won", decoration= "👍")   # replace this with statement generator call
else:
    make_statement(statement="The computer won", decoration= "💻")

print()
make_statement(statement="Game History", decoration= "🎲")

for item in game_history:
    print(item)
