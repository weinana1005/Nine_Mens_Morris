def request_location(question_str):
    loc = int(input(question_str))
    if loc<0 or loc>=24:
        raise RuntimeError("Not a valid location")
    return loc


def draw_board(g):

    def colored(r, g, b, text):

        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

    def piece_char(i):
        """
        Return the (coloured) character corresponding to player i's counter,
        or a + to indicate an unoccupied point
        """
        if i==0:
            return colored(100,100,100,'+')
        elif i==1:
            return colored(255,60,60,'X')
        elif i==2:
            return colored(60,120,255,'O')

        
    board = '''
x--------x--------x  0--------1--------2 
|        |        |  |        |        |
|  x-----x-----x  |  |  3-----4-----5  |
|  |     |     |  |  |  |     |     |  |
|  |  x--x--x  |  |  |  |  6--7--8  |  |
|  |  |     |  |  |  |  |  |     |  |  |
x--x--x     x--x--x  9-10-11    12-13-14
|  |  |     |  |  |  |  |  |     |  |  |
|  |  x--x--x  |  |  |  | 15-16-17  |  |
|  |     |     |  |  |  |     |     |  |
|  x-----x-----x  |  |  18---19----20  |
|        |        |  |        |        |
x--------x--------x  21------22-------23
'''    
    boardstr = ''
    i = 0
    for c in board:
        if c=='x':
            boardstr += piece_char(g[0][i])
            i += 1
        else:
            boardstr += colored(100,100,100,c)
    if g[1]>0 or g[2]>0:
        boardstr += '\nPlayer 1: ' + (piece_char(1)*g[1])
        boardstr += '\nPlayer 2: ' + (piece_char(2)*g[2])
    print(boardstr)

# Task1
def is_adjacent(i, j):
    """Check if two points are adjacent on the Nine Men's Morris board."""
    # Adjacent points on the board
    adjacent_points = {
        0: [1, 9],
        1: [0, 2, 4],
        2: [1, 14],
        3: [4, 10],
        4: [1, 3, 5, 7],
        5: [4, 13],
        6: [7, 11],
        7: [4, 6, 8],
        8: [7, 12],
        9: [0, 10, 21],
        10: [3, 9, 11, 18],
        11: [6, 10, 15],
        12: [8, 13, 17],
        13: [5, 12, 14, 20],
        14: [2, 13, 23],
        15: [11, 16],
        16: [15, 17, 19],
        17: [12, 16],
        18: [10, 19],
        19: [16, 18, 20, 22],
        20: [13, 19],
        21: [9, 22],
        22: [19, 21, 23],
        23: [14 ,22]
    }

    return j in adjacent_points.get(i, [])
    pass

# Task2
def new_game():
    """Initialize a new game state."""
    # Initialize the board with all points empty
    board = [0] * 24

    # Both players start with 9 unplaced counters
    p1_counters = 9
    p2_counters = 9

    # Player 1 starts the game
    active_player = 1

    # Compile the game state
    g = [board, p1_counters, p2_counters, active_player]

    return g
    pass
# Task3
def remaining_counters(g):
    """
    Count the total number of counters the current player has available.
    This includes both the counters on the board and the counters in hand.
    """
    # Identify the active player
    active_player = g[3]

    # Count the number of counters on the board for the active player
    counters_on_board = g[0].count(active_player)

    # Get the number of counters in hand for the active player
    counters_in_hand = g[active_player]

    # Total counters available for the active player
    total_counters = counters_on_board + counters_in_hand

    return total_counters
    pass
# Task4
def is_in_mill(g, i):
    """Check if the counter at point i is in a mill."""
    # Predefined mills on the board
    mills = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Horizontal top three lines
        [9, 10, 11], [12, 13, 14],         # Horizontal middle two lines
        [15, 16, 17], [18, 19, 20], [21, 22, 23],  # Horizontal bottom three lines
        [0, 9, 21], [3, 10, 18], [6, 11, 15],      # Vertical left three lines
        [1, 4, 7], [16, 19, 22],                   # Vertical middle two lines
        [8, 12, 17], [5, 13, 20], [2, 14, 23]      # Vertical right three lines
    ]

    # Check if the index is valid and if there is a counter at index i
    if i < 0 or i >= 24 or g[0][i] == 0:
        return -1

    # Identify which player's counter is at point i
    player_at_i = g[0][i]

    # Check each mill
    for mill in mills:
        if i in mill and all(g[0][point] == player_at_i for point in mill):
            return player_at_i

    return 0
    pass
# Task5
def player_can_move(g):
    """
    Check if the current player has a valid move to make.
    """
    active_player = g[3]
    player_counters = [i for i, x in enumerate(g[0]) if x == active_player]

    # Check if the player has any counters left to place
    if g[active_player] > 0:
        return True

    # Check if any of the player's counters can be moved to an adjacent empty spot
    for counter in player_counters:
        for adjacent in range(24):
            if is_adjacent(counter, adjacent) and g[0][adjacent] == 0:
                return True

    # No valid moves
    return False
    pass

# Task6
def place_counter(g, i):
    """
    Place a counter of the current player at point i on the board.
    Raises a RuntimeError if the target position is already occupied.
    """
    # Check if the target position is already occupied
    if g[0][i] != 0:
        raise RuntimeError("The position is already occupied")

    # Get the current player and place the counter
    active_player = g[3]
    g[0][i] = active_player

    # Decrease the number of unplaced counters for the active player
    g[active_player] -= 1
    pass

# Task7
def move_counter(g, i, j):
    """
    Move a counter of the currently active player from point i to point j.
    Raises RuntimeError for invalid moves.
    """
    active_player = g[3]

    # Validate the move
    if g[0][i] != active_player:
        raise RuntimeError("No counter of the current player at the start position")

    if not is_adjacent(i, j) or g[0][j] != 0:
        raise RuntimeError("Invalid move: target position is not adjacent or is occupied")

    # Move the counter
    g[0][i] = 0  # Remove counter from the start position
    g[0][j] = active_player  # Place counter at the target position
    pass

# Task8
def remove_opponent_counter(g, i):
    """
    Remove an opponent's counter from point i on the board.
    Raises RuntimeError if the removal is not valid.
    """
    active_player = g[3]
    opponent = 3 - active_player  # If active player is 1, opponent is 2 and vice versa

    # Check if the target position has the opponent's counter
    if g[0][i] != opponent:
        raise RuntimeError("Point does not contain an opponent's counter")

    # Remove the opponent's counter
    g[0][i] = 0
    pass

# Task9
def get_placement_position(g):
    while True:
        try:
            # Prompt with the active player
            prompt = f"Player {g[3]}, enter the position to place your counter (0-23): "
            position = request_location(prompt)
            if g[0][position] != 0:
                print("Invalid position. Please try again.")
            else:
                return position
        except RuntimeError as e:
            print(e)

def get_move_positions(g):
    while True:
        try:
            # Prompt for the starting position with the active player
            start_prompt = f"Player {g[3]}, enter the starting position of your counter (0-23): "
            start_position = request_location(start_prompt)
            opponent = 3 - g[3]
            if start_position == g[opponent]:
                print("This is not your counter")
            else:
                start_position == g[0][0]
                print("There is no counter in this position")

            # Prompt for the ending position with the active player
            end_prompt = f"Player {g[3]}, enter the ending position of your counter (0-23): "
            end_position = request_location(end_prompt)

            if not is_adjacent(start_position, end_position) or g[0][end_position] != 0:
                print("Invalid move. Please try again.")
            else:
                return start_position, end_position
        except RuntimeError as e:
            print(e)
def turn(g):
    location = None  # Initialize location to None

    if not player_can_move(g):
        print(f"Player {g[3]} cannot move. Game over.")
        return False

    active_player_prompt = f"Player {g[3]}'s turn. "

    if g[g[3]] > 0:
        while True:
            try:
                location = request_location(active_player_prompt + "Enter a location to place your counter (0-23): ")
                place_counter(g, location)
                break
            except RuntimeError as e:
                print(e)
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 23.")

    else:
        while True:
            try:
                start_pos = request_location(active_player_prompt + "Enter the location of your counter to move (0-23): ")
                if g[0][start_pos] != g[3]:
                    print("You do not have a counter at this location. Please choose a valid location.")
                    continue
                end_pos = request_location("Enter a new location to move your counter to (0-23): ")
                if is_adjacent(start_pos, end_pos) != True:
                    print("You can not move to this location. Please choose a valid location.")
                move_counter(g, start_pos, end_pos)
                location = end_pos  # Update location after successful move
                break
            except RuntimeError as e:
                print(e)
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 23.")

    if location is not None and is_in_mill(g, location):
        while True:
            try:
                draw_board(g)
                remove_location = request_location(active_player_prompt + "Enter the location of an opponent's counter to remove (0-23): ")
                remove_opponent_counter(g, remove_location)
                break
            except RuntimeError as e:
                print(e)
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 23.")

    g[3] = 2 if g[3] == 1 else 1
    return True
    pass

# Task10
def save_state(g, filename):
    """Saves the game state to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(','.join(map(str, g[0])) + '\n')
            file.write(str(g[1]) + '\n')
            file.write(str(g[2]) + '\n')
            file.write(str(g[3]) + '\n')
    except Exception as e:
        raise RuntimeError(f"An error occurred while writing to the file: {e}")

def load_state(filename):
    """Loads the game state from a file."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) != 4:
                raise RuntimeError("Invalid file format")

            board = list(map(int, lines[0].strip().split(',')))
            p1_counters = int(lines[1].strip())
            p2_counters = int(lines[2].strip())
            active_player = int(lines[3].strip())
            return [board, p1_counters, p2_counters, active_player]
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the file: {e}")
    pass

# Task11
def play_game():
    # Create a new game state
    g = new_game()

    while True:
        # Display the current game state
        draw_board(g)

        # Check if the current player has only two counters left
        if remaining_counters(g) <= 2:
            winner = 2 if g[3] == 1 else 1
            print(f"Plaer{g[3]} only has 2 counters left. Player{g[3]} lose. Congratulations to Player {winner}! You have won the game.")
            break  # Break out of the loop, ending the game

        # Take a turn and check if the game is over (player cannot move)
        if not turn(g):
            winner = 2 if g[3] == 1 else 1
            print(f"Congratulations to Player {winner}! You have win the game.")
            break  # Break out of the loop, ending the game

    print("Thank you for playing!")
    pass



def main():
    play_game()
main()
