# 🐍 Python Beginner Level Projects

A collection of beginner-friendly Python projects built to practice core programming concepts such as functions, dictionaries, loops, conditionals, file handling, and regular expressions.

---

## 📁 Projects Overview

| File | Project | Concepts Covered |
|------|---------|-----------------|
| `Simple Calculator.py` | Simple Calculator | Conditionals, loops, history tracking |
| `Tic-Tac-Toe_.py` | Tic-Tac-Toe Game | 2D lists, loops, game logic |
| `hangman_game.py` | Hangman Game | Random module, strings, sets |
| `Chatbot.py` | Rule-Based Chatbot | Dictionaries, input handling |
| `Stock_Portfolio.py` | Stock Portfolio Tracker | Dictionaries, file I/O, arithmetic |
| `Task_Automation.py` | Email Extractor | Regex, file reading/writing |

---

## 📂 Project Descriptions

### 1. 🧮 Simple Calculator — `Simple Calculator.py`
A console-based calculator that supports basic arithmetic operations.

**Features:**
- Addition, subtraction, multiplication, and division
- Calculation history tracking
- Option to clear history

**Run:**
```bash
python "Simple Calculator.py"
```

---

### 2. ❌⭕ Tic-Tac-Toe — `Tic-Tac-Toe_.py`
Classic two-player Tic-Tac-Toe played in the terminal.

**Features:**
- Interactive console board display
- Two-player turn-based gameplay
- Win and draw detection

**Run:**
```bash
python Tic-Tac-Toe_.py
```

---

### 3. 🪤 Hangman Game — `hangman_game.py`
A word-guessing game where the player tries to uncover a hidden word letter by letter.

**Features:**
- Randomly selected word from a predefined list
- Limited number of attempts
- Tracks already-guessed letters to prevent repeats
- Dynamic word reveal as correct guesses are made

**Run:**
```bash
python hangman_game.py
```

---

### 4. 🤖 Rule-Based Chatbot — `Chatbot.py`
A simple terminal chatbot that responds to a set of predefined inputs.

**Features:**
- Responds to greetings and basic queries using a dictionary lookup
- Case-insensitive input handling
- Type `exit` to quit the conversation

**Run:**
```bash
python Chatbot.py
```

**Sample Interaction:**
```
Chatbot (type 'exit' to quit)
You: hello
Chatbot: Hi!
You: how are you
Chatbot: I'm fine, thanks!
You: exit
Chatbot: Bye!
```

---

### 5. 📊 Stock Portfolio Tracker — `Stock_Portfolio.py`
A console app to track your stock investments and calculate total portfolio value.

**Features:**
- Supports stocks: `AAPL`, `TSLA`, `GOOG`, `MSFT`
- Add multiple stocks and quantities
- Calculates total investment value
- Saves portfolio summary to `portfolio.txt`

**Run:**
```bash
python Stock_Portfolio.py
```

**Sample Output:**
```
📊 Stock Portfolio Tracker
Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 2
Your Portfolio: {'AAPL': 2}
💰 Total Investment Value: $360
✅ Portfolio saved to portfolio.txt
```

---

### 6. 📧 Email Extractor (Task Automation) — `Task_Automation.py`
A file automation script that extracts all email addresses from a text file using regex.

**Features:**
- Reads from an input `.txt` file
- Uses regular expressions to find all email addresses
- Writes extracted emails to an output file
- Handles `FileNotFoundError` gracefully

**Setup:**
Create a file named `sample.txt` with some text containing email addresses, then run:

```bash
python Task_Automation.py
```

Output will be saved to `emails.txt`.

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.x installed on your system
- No external libraries required (all projects use the Python standard library)

### Clone the Repository
```bash
git clone https://github.com/Roshan1351/Python_beginner_level_project.git
cd Python_beginner_level_project
```

### Run Any Project
```bash
python <filename>.py
```

---

## 🧠 Concepts Practiced

- Functions and modular code structure
- Dictionaries and dictionary lookups
- Loops (`while`, `for`) and conditionals (`if/elif/else`)
- String manipulation and `.lower()` / `.upper()` methods
- File reading and writing (`open`, `read`, `write`)
- Regular expressions (`re` module)
- Random module for word selection
- Input validation and error handling

---

## 👤 Author

**Roshan Giri**  
BSc Computer Science | BK Birla College, Kalyan (University of Mumbai)  
📧 roshangiri711@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/roshan-giri123) | [LeetCode](https://leetcode.com/RoshanGiri)

---

## 📄 License

This repository is open for learning and reference purposes.
