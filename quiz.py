import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Venus", "Jupiter"],
                "correct_answer": "Mars"
            },
            {
                "question": "Which gas do plants use for photosynthesis?",
                "options": ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"],
                "correct_answer": "Carbon Dioxide"
            }
            # Add more questions here
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=300)
        self.question_label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set("")

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value="", command=self.on_select)
            self.radio_buttons.append(rb)
            rb.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.load_question(self.current_question)

    def load_question(self, question_idx):
        question_data = self.questions[question_idx]
        self.question_label.config(text=question_data["question"])
        
        for i in range(4):
            self.radio_buttons[i].config(text=question_data["options"][i])
            self.radio_buttons[i].config(value=question_data["options"][i])
        
        self.radio_var.set("")

    def on_select(self):
        selected_answer = self.radio_var.get()
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if selected_answer == correct_answer:
            self.score += 1

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.load_question(self.current_question)
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
