import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.constants import INSERT
from tkinter.scrolledtext import ScrolledText


def launch(main):
    root = tkinter.Tk()

    def _label(text):
        Label(root, text=text, wraplength=200).pack(anchor=tkinter.W)

    _label("Url to calculate Tag:")

    url_ui = ttk.Entry()
    url_ui.pack()

    result_ui = ScrolledText()

    ttk.Button(text="Load",
               command=lambda: result_ui.insert(INSERT, main.get_command(url_ui.get()))).pack()

    ttk.Button(text="View from Base",
               command=lambda: result_ui.insert(INSERT, main.view_command(url_ui.get()))).pack()

    _label("List of synonyms:")

    def _text_update(event):
        current = url_ui.get()
        url_ui.delete(0, len(current))
        url_ui.insert(0, synonyms_combo_ui.selection_get())

    synonyms_combo_ui = ttk.Combobox(values=main.synonym_keys(), state='readonly')
    synonyms_combo_ui.bind("<<ComboboxSelected>>", _text_update)
    synonyms_combo_ui.pack()

    _label("Result calculation:")
    result_ui.pack()

    root.mainloop()
