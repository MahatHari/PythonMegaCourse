from curses import window
from tkinter import *
import backend

# define commands


def get_selected_row(event):

    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        author_entry.delete(0, END)
        author_entry.insert(END, selected_tuple[2])
        title_entry.delete(0, END)
        title_entry.insert(END, selected_tuple[1])
        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_tuple[4])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_tuple[3])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(author_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),
                 year_text.get(), isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


def update_command():
    backend.update(selected_tuple[0], title_text.get(
    ), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


window = Tk()

window.title("HK's BookStore")

# title
title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

# author
author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

# year
year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

# isbn
isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)


# list box
list_text = StringVar()
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, rowspan=6, column=0, columnspan=2)

# scroll bar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# add scroll bar to listbox
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

# control buttons
viewall_btn = Button(window, text="View All", width=12, command=view_command)
viewall_btn.grid(row=2, column=3)

search_btn = Button(window, text="Search Entry",
                    width=12, command=search_command)
search_btn.grid(row=3, column=3)

add_btn = Button(window, text="Add Entry", width=12, command=add_command)
add_btn.grid(row=4, column=3)

update_btn = Button(window, text="Update", width=12, command=update_command)
update_btn.grid(row=5, column=3)

delete_btn = Button(window, text="Delete", width=12, command=delete_command)
delete_btn.grid(row=6, column=3)

close_btn = Button(window, text="Close", width=12, command=window.destroy)
close_btn.grid(row=7, column=3)

view_command()
window.mainloop()
