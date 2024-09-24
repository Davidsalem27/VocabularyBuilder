import tkinter as tk

import ShowWordsMenu


class ManageWordsMenu:
    def __init__(self, root, controller):

        self.top = tk.Toplevel(root)  # Create a new Toplevel window
        self.controller=controller
        self.top.title("Manage the words!")
        self.top.geometry("600x400")


        # Create a label in the new screen
        label = tk.Label(self.top, text="Enter a word you wish to add or delete:")
        label.pack(pady=10)
        # Create a text entry field
        self.entry = tk.Entry(self.top, width=30)
        self.entry.pack(pady=5)

        # Create a submit button
        self.submit_button = tk.Button(self.top, text="Add a new word", command=self.submit_word)
        self.submit_button.pack(pady=20)  # Add some vertical padding
        # Create a delete button
        self.delete_button = tk.Button(self.top, text="delete a word", command=self.delete_word)
        self.delete_button.pack(pady=20)  # Add some vertical padding

        self.meanings_button = tk.Button(self.top, text="meaning", command=self.get_meanings)
        self.meanings_button.pack(pady=20)  # Add some vertical padding
        show_words_button = tk.Button(self.top, text="show all words", command=self.open_show_words_menu)
        show_words_button.pack(pady=20)  # Add some vertical padding
    def get_meanings(self):
        self.controller.get_meanings(self.entry.get())
        self.entry.delete(0, tk.END)
    def delete_word(self):
        self.controller.delete_word( self.entry.get())

        self.entry.delete(0, tk.END)


    def submit_word(self):
        new_word = self.entry.get()
        if new_word:
            self.controller.submit_new_word(new_word)

            self.entry.delete(0, tk.END)
        else:
            self.output_label.config(text="Please enter a word.")

    def open_show_words_menu(self):
        show_words_controller=self.controller.open_show_words_menu()
        ShowWordsMenu.ShowWordsMenu(self.top,show_words_controller)
