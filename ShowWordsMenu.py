import tkinter as tk
from tkinter import font
class ShowWordsMenu:

    def __init__(self, root, controller):
        self.top = tk.Toplevel(root)  # Create a new Toplevel window
        self.controller = controller
        self.top.title("List of Words")
        self.top.geometry("600x400")
        self.list_of_words = self.controller.get_all_words()
        self.meanings_font = font.Font(size=16)
        self.word_listbox = tk.Listbox(self.top, width=50, height=50)
        self.word_listbox.pack(pady=10)
        self.create_list()


    def create_list(self):

        for word in self.list_of_words:
            self.word_listbox.insert(tk.END, word)
        self.word_listbox.bind('<<ListboxSelect>>', self.show_meaning)

    def show_meaning(self, event):
        selected_index = self.word_listbox.curselection()
        if selected_index:
            word = self.word_listbox.get(selected_index)
            # Get the meaning of the selected word
            meaning = self.controller.get_meaning(word)
            if meaning:
                self.open_meaning_window(word, meaning)

    def open_meaning_window(self, word, meanings):
        # Create a new window
        meanings_window = tk.Toplevel(self.top)
        meanings_window.title(word)
        meanings_window.geometry("800x600")

        for index, (meaning, example) in enumerate(meanings):
            meaning_label = tk.Label(meanings_window, text=f"{index + 1}. {meaning}", wraplength=300, justify="left",
                                     font=self.meanings_font)
            # meaning_label.pack(anchor="w", padx=10, pady=(10, 0))  # Add some padding

            # Create a label for the example, indented
            meaning_label.pack(pady=20)
            if example:

                example_label = tk.Label(meanings_window, text=f"   Example: {example}", wraplength=300, justify="left",
                                     font=self.meanings_font)
                example_label.pack(pady=20, padx=30)


