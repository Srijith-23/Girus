# 🧠 Programming Assignment: Advanced Algorithmic Challenges

## 👩‍💻 Author: Srijith 
This repository contains solutions to a set of algorithmic programming problems focused on logic building, data structures, and clean code practices.

---

## ✅ Assignment Problems

### 🔸 Problem 1: Sudoku Validator With Custom Zones
Validate a 9x9 Sudoku board with:
- Row, column, and subgrid validation.
- Additional **custom zone** validation (each consisting of 9 unique cells).

📁 File: `sudoku_validator.py`  
🧪 Sample Test: Valid board + custom zones → ✅ Output: `True`

---

### 🔸 Problem 2: Alien Dictionary
Given a sorted list of words from an alien language, determine the order of characters used.

📁 File: `alien_dictionary.py`  
🧪 Sample Input: `["wrt", "wrf", "er", "ett", "rftt"]`  
📤 Output: `wertf`

---

### 🔸 Problem 3: Knights and Portals
Shortest path from top-left to bottom-right in a grid using:
- Normal BFS traversal
- One-time teleportation between any two empty cells (`0`s)

📁 File: `knights_and_portals.py`  
🧪 Sample Grid: `[[0,1,0],[1,0,1],[0,0,0]]`  
📤 Output: `3`

---

### 🔸 Problem 4: Bitwise Matching Pattern
Find the next larger integer that has the **same number of 1s in binary** as the given integer.

📁 File: `bitwise_matching.py`  
🧪 Input: `6` (binary `110`)  
📤 Output: `9` (binary `1001`)

---

### 🔸 Problem 5: Matrix Islands with Diagonals
Count the number of islands in a matrix where `1`s are connected in **horizontal, vertical, or diagonal** directions.

📁 File: `matrix_islands.py`  
🧪 Sample Matrix: See example in code  
📤 Output: `3`

---

### 🔹 Bonus Challenge (Optional): Mini Interpreter
A basic interpreter that supports:
- `let` variable assignments
- `if` conditionals with print statements

📁 File: `mini_interpreter.py`  
🧪 Input: 
```txt
let x = 5;
if x == 5 then print("x is five");
