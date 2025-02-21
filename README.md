# MATH20621 - Programming With Python Coursework

## Overview
This repository contains coursework solutions for **MATH20621 - Programming with Python**. The coursework consists of three separate assignments covering various **Python programming concepts**, including **mathematical functions, card game simulations, and board game logic implementation**.

## Files in This Repository

### 1. `coursework1.py`
- **Brief Overview**:
  - Focuses on **mathematical functions and numerical computations**.
  - Implements different **limiter functions** (WENO, MINMOD, Mean) for numerical approximation.
  - **Modular exponentiation** and **prime number verification**.
  - Introduces **Two-Knodel numbers** and their properties.
- **Key Functions**:
  - `limiter(a, b, limitertype)`: Computes a limit based on the chosen method.
  - `pow_mod(a, b, c)`: Computes modular exponentiation.
  - `is_prime(n)`: Checks if a number is prime.
  - `two_knodel(m)`: Determines if a number satisfies the Two-Knodel property.

### 2. `coursework2.py`
- **Brief Overview**:
  - Focuses on **card game simulations**, including deck creation, shuffling, and dealing.
  - Implements a **riffle shuffle** and **hand sorting**.
  - Simulates dealing cards evenly among players.
- **Key Functions**:
  - `new_deck()`: Generates a deck with predefined suit ordering.
  - `riffle(d)`: Performs a riffle shuffle on the deck.
  - `deal(d, n)`: Distributes the deck among `n` players.
  - `hand_string(h)`: Returns a sorted hand as a formatted string.

### 3. `coursework_3.py`
- **Detailed Explanation**:
  - Implements a **full board game simulation** for **Nine Men's Morris**.
  - Utilizes **graph-based adjacency lists** to manage board movements.
  - Includes **game state management** with saving and loading functionality.
  - Handles **player interactions** with turn-based logic and move validation.
  - Implements **winning conditions**, restricting movement when necessary.

- **Key Features**:
  - **Board Representation & Display**:
    - `draw_board(g)`: Displays the game board using ASCII art with colored pieces.
    - `is_adjacent(i, j)`: Checks if two positions on the board are adjacent.
  - **Game Logic & Moves**:
    - `new_game()`: Initializes a fresh game state.
    - `remaining_counters(g)`: Determines the number of pieces each player has left.
    - `place_counter(g, i)`: Places a counter for the active player on the board.
    - `move_counter(g, i, j)`: Moves a counter to an adjacent valid position.
    - `remove_opponent_counter(g, i)`: Allows a player to remove an opponent's piece if a mill is formed.
  - **Game State Management**:
    - `save_state(g, filename)`: Saves the current game state to a file.
    - `load_state(filename)`: Loads a previously saved game state.
  - **Gameplay Flow**:
    - `play_game()`: Runs the full game loop, handling turns, board updates, and win conditions.
    - Players must place pieces, move them strategically, and block their opponent while aiming to reduce the opponent’s counters.
    - If a player is left with only two pieces or has no valid moves left, they lose the game.

## How to Run
1. **Install Python** (if not already installed).
2. **Run a specific coursework file**:
   ```bash
   python coursework1.py
   python coursework2.py
   python coursework_3.py
   ```
3. **Follow on-screen prompts for interactive functionality**.

## Summary of Learning Outcomes
- **Mathematical Programming**: Implemented numerical computations and algorithms.
- **Card Game Simulation**: Developed logic for deck creation, shuffling, and dealing.
- **Board Game Implementation**: Created a functional **Nine Men's Morris** game with interactive play and game state persistence.

