import tkinter as tk
from tkinter import font
SIZE_QUIZ = 5

class BasicQuizMenu:
    """
    the view aspect of the quiz, represents the window of the quiz
    """
    def __init__(self, root, controller):
        if root:
            self.top = tk.Toplevel(root)
        else:
            self.top=tk.Tk()
        self.controller = controller
        self.current_window_index = 0
        self.top.title("Basic Quiz")
        self.top.geometry("800x800")
        # self.top.bind('<Escape>', self.close)
        self.definitions = self.controller.get_n_definitions()
        self.meanings_font=font.Font(size=16)
        self.word_font=font.Font(size=30)

        self.create_window()
        self.top.mainloop()

    def create_window(self):
        current_meaning = self.definitions[self.current_window_index][1]
        current_word = self.definitions[self.current_window_index][0]
        for widget in self.top.winfo_children():
            widget.destroy()
        #create word label
        self.word_label = tk.Label(self.top, text=current_word,font=self.word_font)
        self.word_label.pack(pady=20)
        #create meaning label
        prev_button = tk.Button(self.top, text="Previous", command=self.prev_window)
        prev_button.place(x=10,y=0,width=100,height=100)
        self.top.bind('<Left>', self.prev_window)
        # Create Next button
        next_button = tk.Button(self.top, text="Next", command=self.next_window)
        # next_button.pack(side=tk.RIGHT, padx=20)
        next_button.place(x=700,y=0,width=100,height=100)
        self.top.bind('<Right>', self.next_window)
        func_button1 = tk.Button(self.top, text="Reveal meaning!",
                                 command=lambda: self.reveal_meaning(label_meanings_examples))
        func_button1.pack(side=tk.RIGHT, padx=20)
        self.top.bind('<r>', lambda event: self.reveal_meaning(label_meanings_examples))
        func_button2 = tk.Button(self.top, text="Easy", command=lambda: self.easy_word(current_word))
        func_button2.pack(side=tk.RIGHT, padx=20)

        func_button3 = tk.Button(self.top, text="Hard", command=lambda: self.hard_word(current_word))
        func_button3.pack(side=tk.RIGHT, padx=20)
        label_meanings_examples=[]
        #create the labels for meaning
        for index, (meaning, example) in enumerate(current_meaning):
            # Create a label for the meaning
            meaning_label = tk.Label(self.top, text=f"{index + 1}. {meaning}",
                                     wraplength=700, justify="left",
                                     font=self.meanings_font)
            # meaning_label.pack(anchor="w", padx=10, pady=(10, 0))  # Add some padding

            # Create a label for the example, indented
            if example:
                example_label = tk.Label(self.top, text=f"   Example: {example}",
                                         wraplength=700, justify="left",
                                         font=self.meanings_font)
            # example_label.pack(anchor="w", padx=20)  # Indent the example
                label_meanings_examples.append((meaning_label,example_label))
            else:
                label_meanings_examples.append((meaning_label, None))
        # Create Previous button

    def reveal_meaning(self, meaning_label):
        window_width = self.top.winfo_width()
        print(window_width)
        label_width = int(window_width * 0.8)
        # self.meanining_label.config(text="Function 1 executed!")
        # self.meaning_label.config(text=meaning_label)

        for i in range(len(meaning_label)):
            meaning_label[i][0].place(x=10,y=100+(i*120))
            if meaning_label[i][1]:
                meaning_label[i][1].place(x=10,y=150+(i*120))

    def easy_word(self,word):
        self.controller.update_word_easy(word)

    def hard_word(self,word):
        self.controller.update_word_hard(word)


    def next_window(self, event=None):
        if self.current_window_index < SIZE_QUIZ - 1:
            self.current_window_index += 1
            self.create_window()

    def prev_window(self, event=None):
        if self.current_window_index > 0:
            self.current_window_index -= 1
            self.create_window()
