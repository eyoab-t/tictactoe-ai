# 🎮 Tic-Tac-Toe AI with Pygame

A classic **Tic-Tac-Toe** game where the computer plays **perfectly** using the **Minimax algorithm**.  
Challenge it if you dare—you can only draw or lose!

---

## ✨ Features

- **Perfect Play:** Implements a full Minimax search.  
- **Clean GUI:** Built with [Pygame](https://www.pygame.org/).  
- **Modular Code:** AI logic completely isolated in `tictactoe.py` for easy testing.  
- **Replay Anytime:** Instant reset to play again.

## 🧠 How the AI Works

1. **Game-Tree Search:** Explores every possible sequence of moves until a terminal board state is reached.  
2. **Utility Scoring:**  
   - `+1` if X wins  
   - `-1` if O wins  
   - `0` if draw  
3. **Optimal Decision:**  
   - `max_value` chooses moves that maximise X’s outcome.  
   - `min_value` chooses moves that minimise it for O.  

Because Tic-Tac-Toe has a small search space, the AI can look at *all* possibilities and never miss the best move.

---

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/eyoab-t/tictactoe-ai.git
   cd tictactoe-ai

2. **Install Dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. **Run the game**
   ```bash
    python runner.py

**About This Project**

This was my first AI project, originally built in 2023 and uploaded here in 2025.
— Eyoab
