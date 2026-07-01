# Hangman Game

A modern, minimalist Hangman desktop game built with Python and CustomTkinter, featuring live word fetching via a REST API.

## How to use:
1. Select the difficulty (**Easy**, **Medium**, or **Hard**) from the dropdown list.
2. Press **New Game** at any time to get a new word.
3. Click the buttons on the screen keyboard to guess letters.
4. Correct guesses reveal letters instantly on the screen.
5. Incorrect guesses advance the hangman sprite animation stage by stage.
6. If you win, the text turns green. If you lose, it automatically reveals the correct answer in red.

## Preview

| Dark Mode | Light Mode |
| :---: | :---: |
| <img width="514" height="800" alt="GUI preview v1 0 0 (dark mode)" src="https://github.com/user-attachments/assets/aa8e1ac7-8966-4279-a092-5735b01f3130" />| <img width="507" height="795" alt="GUI preview v1 0 0 (light mode)" src="https://github.com/user-attachments/assets/562b150d-a487-4b9f-82c4-c2f4ef2ded5d" />|

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python gui.py
   ```
