# 🪙 AI Smart Coin Changer

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=flat&logo=flask)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-Frontend-38B2AC?style=flat&logo=tailwind-css)

A high-performance full-stack web application designed to solve the classic **"Coin Change"** algorithmic problem in real-time. Built specifically for Indian Rupees (INR), this app calculates the total possible ways to make a target amount, determines the absolute minimum coins required, and safely generates optimal combinations.

## 🚀 Technical Highlights

This project was built with a strict focus on algorithmic efficiency, edge-case handling, and memory safety:

* **Dynamic Programming (DP):** * Utilizes **Coin Change II** (Unbounded Knapsack) logic to calculate the total number of valid combinations.
    * Utilizes **Coin Change I** logic to find the absolute minimum coins needed.
    * Achieves an optimal **O(A * N)** time complexity (where A is the Amount and N is the number of denominations).
* **Memory-Safe Execution (DFS):** Engineered a recursive Depth-First Search algorithm to generate the exact coin combinations. It includes a strict $O(1)$ execution cap (displaying the top 100 results) to prevent server timeouts or browser crashes during high-load calculations.
* **Input Validation:** Strict backend validation ensures only valid Indian Rupee denominations (₹1, 2, 5, 10, 20) are processed.

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Frontend:** HTML5, Jinja2 Templating, Tailwind CSS
* **Algorithms:** Dynamic Programming, Recursion, Depth-First Search

## 📁 Project Structure

```text
coin-changer-ai/
│
├── app.py                  # Core backend routing and algorithmic logic
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # Tailwind CSS integrated frontend UI
