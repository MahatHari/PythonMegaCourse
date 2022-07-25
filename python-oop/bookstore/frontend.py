from curses import window
from tkinter import *
from backend import Database


# define commands

database = Database("books.db")


class Window(object):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Book Store")

        # title
        title_label = Label(window, text="Title")
        title_label.grid(row=0, column=0)

        self.title_text = StringVar()
        self.title_entry = Entry(window, textvariable=self.title_text)
        self.title_entry.grid(row=0, column=1)

        # author
        author_label = Label(window, text="Author")
        author_label.grid(row=0, column=2)

        self.author_text = StringVar()
        self.author_entry = Entry(window, textvariable=self.author_text)
        self.author_entry.grid(row=0, column=3)

        # year
        self.year_label = Label(window, text="Year")
        self.year_label.grid(row=1, column=0)

        self.year_text = StringVar()
        self.year_entry = Entry(window, textvariable=self.year_text)
        self.year_entry.grid(row=1, column=1)

        # isbn
        isbn_label = Label(window, text="ISBN")
        isbn_label.grid(row=1, column=2)

        self.isbn_text = StringVar()
        self.isbn_entry = Entry(window, textvariable=self.isbn_text)
        self.isbn_entry.grid(row=1, column=3)

        # list box
        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, rowspan=6, column=0, columnspan=2)

        # scroll bar
        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        # add scroll bar to listbox
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # control buttons
        viewall_btn = Button(window, text="View All",
                             width=12, command=self.view_command)
        viewall_btn.grid(row=2, column=3)

        search_btn = Button(window, text="Search Entry",
                            width=12, command=self.search_command)
        search_btn.grid(row=3, column=3)

        add_btn = Button(window, text="Add Entry",
                         width=12, command=self.add_command)
        add_btn.grid(row=4, column=3)

        update_btn = Button(window, text="Update",
                            width=12, command=self.update_command)
        update_btn.grid(row=5, column=3)

        delete_btn = Button(window, text="Delete",
                            width=12, command=self.delete_command)
        delete_btn.grid(row=6, column=3)

        close_btn = Button(window, text="Close", width=12,
                           command=window.destroy)
        close_btn.grid(row=7, column=3)

        self.view_command()

    def get_selected_row(self, event):

        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
            self.author_entry.delete(0, END)
            self.author_entry.insert(END, selected_tuple[2])
            self.title_entry.delete(0, END)
            self.title_entry.insert(END, selected_tuple[1])
            self.isbn_entry.delete(0, END)
            self.isbn_entry.insert(END, selected_tuple[4])
            self.year_entry.delete(0, END)
            self.year_entry.insert(END, selected_tuple[3])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(),
                        self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(),
                                self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.view_command()

    def update_command(self):
        database.update(selected_tuple[0], self.title_text.get(
        ), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.view_command()


window = Tk()
Window(window)
window.mainloop()
