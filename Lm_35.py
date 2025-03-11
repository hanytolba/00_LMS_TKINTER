from tkinter import Label, Button, Tk, CENTER, PhotoImage, StringVar, E, Toplevel
from awesometkinter.bidirender import add_bidi_support
from datetime import datetime as dt
# from tkinter.constants import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import csv

# @----------------------------------------------------------------
# region  FORM                [rgba(0,0,100,0.3)]
# @----------------------------------------------------------------
APP_DB = "lm_booklib.db"
# APP_DB = "lm_booklib_small.db"
root = Tk()
FORM_WIDTH = 1000
FORM_HEIGHT = 750
x = (root.winfo_screenwidth() - FORM_WIDTH) // 2
Y = 0
color = "#333333"
root.config(bg=color)
root.geometry(f"{FORM_WIDTH}x{FORM_HEIGHT}+" + str(x) + "+" + str(Y))
root.title("LMS V. 5.00")
root.resizable(False, False)
# endregion

# region styles               [rgba(0,100,100,0.9)]
# @----------------------------------------------------------------
style = ttk.Style()
style.theme_use("default")
#!------------------------------------------------------------
style.configure(
    "TCombobox",
    font=("Helvetica", 18),  # Font for the Combobox text
    padding=5,
    foreground="blue",  # Text color
    background="lightgray",  # Background color
    fieldbackground="white",
)
style.configure(
    "TCombobox.Listbox",
    font=("Helvetica", 18),  # Font for the dropdown list
    foreground="black",  # Text color for the list
    background="yellow",  # Background color for the list
    selectforeground="white",  # Selected item text color
    selectbackground="gray",
)
#!------------------------------------------------------------
style.configure("Treeview", font=("Arial", 14), rowheight=35)
style.configure(
    "Treeview.Heading",
    font=("Times New Roman", 16),
    background="#333333",
    foreground="#aaaaaa",
    ANCHOR=CENTER,
)
#!------------------------------------------------------------
style.configure("TLabel", font=("Tahoma", 14, "bold"), background="skyblue3")
#!------------------------------------------------------------
style.configure("TEntry", font=("Tahoma", 14), background="red")
#!------------------------------------------------------------
style.configure(
    "TButton",
    font=("Arial", 14),
    background="#999999",
    foreground="black",
    # relief="raised",
    width=6,
    align="center",
    # height=2,
    borderwidth=6,
)

style.configure(
    "book.TButton",
    font=("Arial", 14),
    background="#999999",
    foreground="black",
    relief="raised",
    width=25,
    height=4,
    borderwidth=2,
)


style.configure(
    "searchbook.TButton",
    font=("Arial", 12),
    background="#ffff00",
    foreground="black",
    relief="raised",
    width=25,
    height=4,
    borderwidth=2,
)
#!------------------------------------------------------------
style.configure(
    "TScrollbar",
    background="lightblue",
    troughcolor="#555555",
    arrowcolor="darkblue",
    arrowpadding=10,
    arrowsize=20,
)
#!------------------------------------------------------------
# endregion

# region  frames              [rgba(255,0,0,0.3)]
# @----------------------------------------------------------------
frame1 = tk.Frame(root, bg="#2f6278")
frame1.place(x=0, y=65, width=FORM_WIDTH, height=FORM_HEIGHT - 65)

cat_frame1 = tk.Frame(frame1, bg="royalblue4")
cat_frame1.place(x=0, y=94, width=390, height=124)

frame2 = tk.Frame(root, bg="skyblue2")
frame2.place(x=0, y=65, width=FORM_WIDTH, height=FORM_HEIGHT - 65)
frame3 = tk.Frame(root, bg="skyblue3")
frame3.place(x=0, y=65, width=FORM_WIDTH, height=FORM_HEIGHT - 65)
frame4 = tk.Frame(root, bg="skyblue4")
frame4.place(x=0, y=65, width=FORM_WIDTH, height=FORM_HEIGHT - 65)
# endregion

# region  MENU & header       [rgba(155,0,155,0.3)]
# @------------------- LOGO ---------------------------------------------
conn = sqlite3.connect(APP_DB)
cursor = conn.cursor()
cursor.execute("""SELECT photo FROM photos WHERE id = 1 """)
result = cursor.fetchone()
conn.close()
photo_data = result[0]
photo = PhotoImage(data=photo_data)
#!----------------------------------
photo_label = tk.Label(root)
photo_label.config(image=photo)
photo_label.place(x=940, y=5)
# @ -------------------- APP TITLE ---------------------
lbl1 = tk.Label(
    root,
    text=" نظام سما نور مصر لادارة المكتبات  اصدار 4.0 ",
    font="Arial 16 bold",
    anchor="center",
    bg="#333333",
    fg="#ffffff",
)
lbl1.place(x=568, y=20)
# @--------------------buttons-------------------------------------------
conn = sqlite3.connect(APP_DB)
cursor = conn.cursor()
cursor.execute("""SELECT photo FROM photos WHERE id = 2 """)
result = cursor.fetchone()

photo_data2 = result[0]
photo2 = PhotoImage(data=photo_data2)

cursor.execute("""SELECT photo FROM photos WHERE id = 3 """)
result = cursor.fetchone()
photo_data3 = result[0]
photo3 = PhotoImage(data=photo_data3)

cursor.execute("""SELECT photo FROM photos WHERE id = 4 """)
result = cursor.fetchone()
photo_data4 = result[0]
photo4 = PhotoImage(data=photo_data4)

cursor.execute("""SELECT photo FROM photos WHERE id = 5 """)
result = cursor.fetchone()
photo_data5 = result[0]
photo5 = PhotoImage(data=photo_data5)


conn.close()
# *==================================================================
button_books = ttk.Button(
    root,
    text="   عن \nالبرنامج",
    image=photo2,
    compound=tk.LEFT,
    command=frame4.tkraise,
)
button_books.place(
    x=0,
    y=0,
)
# *==================================================================
button_users = ttk.Button(
    root,
    text="الاستعارة",
    image=photo3,
    compound=tk.LEFT,
    command=frame3.tkraise,
)
button_users.place(x=140, y=0)
# *==================================================================
button_loan = ttk.Button(
    root,
    text="المشتركين",
    image=photo4,
    compound=tk.LEFT,
    command=frame2.tkraise,
)
button_loan.place(
    x=280,
    y=0,
)
# *==================================================================
button_about = ttk.Button(
    root,
    text="الكتب",
    image=photo5,
    compound=tk.LEFT,
    command=frame1.tkraise,
)
button_about.place(
    x=420,
    y=0,
)


# *==================================================================
# endregion

# region  Book functions      [rgba(100,0,0,0.3)]
# @----------------------------------------------------------------
def update_row_count_label(treeview, label):
    row_count = len(treeview.get_children())
    label.config(text=f"{row_count} : عدد الكتب ")


def show_custom_message_box(mtext):
    """ show_custom_message_box """
    # Create a new top-level window
    custom_msg_box = Toplevel(frame1, background="darkred")
    custom_msg_box.title("Information")

    # Set the size and position of the window
    custom_msg_box.geometry("300x200+500+250")

    # Create a custom label with a custom font
    custom_label = Label(
        custom_msg_box,
        text=mtext,
        fg="white",
        bg="darkred",
        font=("Arial", 18),
        anchor="center",
    )
    custom_label.pack(pady=10)

    # Create a close button
    close_button = Button(
        custom_msg_box,
        text="OK",
        anchor="center",
        width=8,
        font=("Arial", 14, "bold"),
        command=custom_msg_box.destroy,
    )
    close_button.pack(pady=5)


# endregion

# region  Book  LABELs        [rgb(63, 6, 34)]
# @----------------------------------------------------------------
# #! --------- labels ------------------------------
book_labels_text = [
    "المسلسل",
    "اسم الكتاب",
    "المؤلف",
    "الناشر",
    "رقم الكتاب",
    "رقم التصنيف",
    "الدولاب",
    "الرف",
    "معلومات الناشر",
    "ملاحظات",
    " التصنيف",
]
book_labels_x = [9, 9, 9, 9, 7, 4.92, 1, 2.53, 8.9, 4.92, 3.1]
book_labels_y = [0, 1, 2, 3, 0, 3, 1, 1, 4, 0, 2]
for i in range(11):
    lbl1 = tk.Label(
        frame1,
        text=book_labels_text[i],
        font=("Arial", 14, "bold"),
        background="#2f6278",
        fg="#FFFFFF"
    )
    lbl1.place(x=(book_labels_x[i] * 100) + 5, y=(book_labels_y[i] * 40) + 20)
# endregion

# region  Book Entryy         [rgba(0,105,0,0.3)]
# @----------------------------------------------------------------

entry_book_id = tk.Entry(
    frame1,
    font="Arial 14",
    justify="right",
    width=8,
    borderwidth=3,
    background="yellow",
)  #    textvariable=case_id,
entry_book_id.place(x=800, y=20)
#!-----------------------------------------------------------------
entry_title = tk.Entry(
    frame1,  #    textvariable=case_id,
    width=54,
    borderwidth=3,
    font="Arial 14 bold",
    justify="right",
    background="yellow",
)
entry_title.place(x=300, y=60)
arabic_text = StringVar()
add_bidi_support(entry_title)

#!-----------------------------------------------------------------
entry_writer = tk.Entry(
    frame1,
    textvariable=arabic_text,
    width=45,
    font="Arial 14 bold",
    justify="right",
    borderwidth=3,
    background="yellow",
)
entry_writer.place(x=400, y=100)
add_bidi_support(entry_writer)
#!-----------------------------------------------------------------
entry_publisher = tk.Entry(
    frame1,  #    textvariable=case_id,
    width=45,
    font="Arial 14 bold",
    justify="right",
    borderwidth=3,
    background="yellow",
)
entry_publisher.place(x=400, y=140)
add_bidi_support(entry_publisher)
#!-----------------------------------------------------------------
entry_book_no = tk.Entry(
    frame1,
    font="Arial 14 bold",
    justify="right",
    width=8,
    borderwidth=3,
    background="yellow",)
entry_book_no.place(x=600, y=20)
add_bidi_support(entry_book_no)
# #!-----------------------------------------------------------------
entry_cab = tk.Entry(
    frame1,  #    textvariable=case_id,
    width=8,
    font="Arial 14 bold",
    justify="right",
    borderwidth=3,)
entry_cab.place(x=5, y=60)
# #!-----------------------------------------------------------------
entry_shelf = tk.Entry(
    frame1,  #    textvariable=case_id,
    width=8,
    font="Arial 14 bold",
    justify="right",
    borderwidth=3,)
entry_shelf.place(x=160, y=60)
add_bidi_support(entry_shelf)
# #!-----------------------------------------------------------------
entry_pinfo = tk.Entry(
    frame1,  #    textvariable=case_id,
    width=44,
    font="Arial 14 bold",
    justify="right",
    borderwidth=3,)
entry_pinfo.place(x=400, y=180)
add_bidi_support(entry_pinfo)
#!-----------------------------------------------------------------
entry_notes = tk.Entry(
    frame1,  #    textvariable=case_id,
    width=44,
    font="Arial 14 bold",
    justify="right",
    borderwidth=3,)
entry_notes.place(x=5, y=20)
add_bidi_support(entry_notes)
# endregion

# region  Book Combo box      [rgba(255,0,0,0.1)]
# @----------------------------------------------------------------
# #todo=============== combobox style ================================================
root.option_add("*TCombobox*Listbox.font", ("arial", 14))
root.option_add("*TCombobox*Listbox.background", "#dddddd")


# # #todo================     combobox functions =======================================================
def fetch_data(Query, params=()):
    """ fetch data """
    conn = sqlite3.connect(APP_DB)
    cursor = conn.cursor()
    cursor.execute(Query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_combobox2(event):
    """update_combobox2"""
    selected_catid = combobox1.get().split(" - ")[0]  # Extract the catid
    if selected_catid:
        first_digit = selected_catid[0]
        Query = "SELECT catid, cat FROM cat WHERE catid LIKE ? AND substr(catid, 3, 1) = '0'"
        data = fetch_data(Query, (first_digit + "%",))
        combobox2["values"] = [f"{row[0]} - {row[1]}" for row in data]
        combobox2.set("")
        combobox3.set("")


def update_combobox3(event):
    selected_catid = combobox2.get().split(" - ")[0]  # Extract the catid
    if selected_catid:
        first_two_digits = selected_catid[:2]
        Query = "SELECT catid, cat FROM cat WHERE catid LIKE ?"
        data = fetch_data(Query, (first_two_digits + "%",))
        combobox3["values"] = [f"{row[0]} - {row[1]}" for row in data]
        combobox3.set("")


def fill_entry(event):
    selected_item = combobox3.get().split(" - ")[0]  # Extract the catid
    entry_cat_var.set(selected_item)


# Fetch data for combobox1
QUERY = "SELECT catid, cat FROM cat WHERE catid LIKE '%00'"
data1 = fetch_data(QUERY)

# Create Comboboxes
combobox1 = ttk.Combobox(
    frame1,
    font=("arial", 12, "bold"),
    values=[f"{row[0]} - {row[1]}" for row in data1],
    state="readonly",
)
combobox2 = ttk.Combobox(frame1, state="readonly", font=("arial", 12, "bold"))
combobox3 = ttk.Combobox(frame1, state="readonly", font=("arial", 12, "bold"))


# Create an Entry widget
entry_cat_var = tk.StringVar()
entry_cat = tk.Entry(
    frame1,
    textvariable=entry_cat_var,
    font="Arial 14 bold",
    justify="right",
    width=6,
    background="yellow",
)
entry_cat.place(x=310, y=140)

# Bind events to update comboboxes and fill entry
combobox1.bind("<<ComboboxSelected>>", update_combobox2)
combobox2.bind("<<ComboboxSelected>>", update_combobox3)
combobox3.bind("<<ComboboxSelected>>", fill_entry)

combobox1.place(x=5, y=100, width=300, height=30)
combobox2.place(x=5, y=140, width=300, height=30)
combobox3.place(x=5, y=180, width=300, height=30)


# endregion

# region  Book buttons & functions [rgba(0,0,150,0.3)]
# @-------------------------------- EXPORT -------------------------------------------------------
def book_export_data():  # * export data
    """    fksdhfskj """
    # Connect to SQLite database
    conn = sqlite3.connect(APP_DB)
    cursor = conn.cursor()

    # Execute a QUERY to fetch all data from the table
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    # Ask the user to select a file location to save the CSV
    # file_path = filedialog.asksaveasfilename(
    #     defaultextension=".csv", filetypes=[("CSV files", "*.csv")]
    # )
    now = dt.now()

    # Format the date and time as a string for the file name
    file_name = now.strftime("book_" + "%Y%m%d%H%M%S") + ".csv"
    # Write data to CSV file
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])  # Write headers
        writer.writerows(rows)  # Write data

    # Close the database connection
    conn.close()
    show_custom_message_box("تم  \n\n تصدير البيانات")


# @---------------------------------- CLEAR -----------------------------------------------------
def book_clear_field():
    """clear field"""
    for widget in frame1.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
    entry_cat_var.set("")


# @----------------------------------- SEARCH ----------------------------------------------------
# @----------------------------------- SEARCH ----------------------------------------------------
def book_search_or():  # * search book
    conn = sqlite3.connect(APP_DB)
    cursor = conn.cursor()
    tree_books.delete(*tree_books.get_children())

    query = """SELECT notes, publishinfo, shelf, cab, cat, bookno, publisher, writer, title, id
               FROM books WHERE """  # Start building the query

    conditions = []
    params = []

    if entry_book_id.get():
        conditions.append("id = ?")
        params.append(entry_book_id.get())

    if entry_writer.get():
        conditions.append("writer LIKE ?")
        params.append(
            f"%{entry_writer.get()}%"
        )  # add % to the search term to search for any part of the text

    if entry_publisher.get():
        conditions.append("publisher LIKE ?")
        params.append(
            f"%{entry_publisher.get()}%"
        )  # add % to the search term to search for any part of the text

    if entry_book_no.get():
        conditions.append("bookno LIKE ?")
        params.append(
            f"%{entry_book_no.get()}%"
        )  # add % to the search term to search for any part of the text

    if entry_cat.get():
        conditions.append("cat LIKE ?")
        params.append(
            f"%{entry_cat.get()}%"
        )  # add % to the search term to search for any part of the text

    if entry_title.get():  # If you want to include title search
        title_text = entry_title.get()  # Get the text *first*
        title_search_term = f"%{title_text}%"  # *Then* format it
        conditions.append("title LIKE ?")
        params.append(title_search_term)

    if conditions:
        query += " OR ".join(conditions)  # Combine conditions with AND
    else:
        query = """SELECT notes, publishinfo, shelf, cab, cat, bookno, publisher, writer, title, id 
               FROM books"""  # if no search terms show all books

    cursor.execute(query, tuple(params))  # Use parameters!
    rows = cursor.fetchall()
    conn.close()

    count = 0
    for row in rows:
        if count % 2 == 0:
            tree_books.insert(
                "", "end", values=row, tags=("evenrow",)
            )  # Correct values usage
        else:
            tree_books.insert(
                "", "end", values=row, tags=("oddrow",)
            )  # Correct values usage
        count += 1

    update_row_count_label(tree_books, row_count_label)

def book_search_and():  # * search book
    conn = sqlite3.connect(APP_DB)
    cursor = conn.cursor()
    tree_books.delete(*tree_books.get_children())

    query = """SELECT notes, publishinfo, shelf, cab, cat, bookno, publisher, writer, title, id
               FROM books WHERE """  # Start building the query

    conditions = []
    params = []

    if entry_book_id.get():
        conditions.append("id = ?")
        params.append(entry_book_id.get())

    if entry_writer.get():
        conditions.append("writer LIKE ?")
        params.append(
            f"%{entry_writer.get()}%"
        )  # add % to the search term to search for any part of the text

    if entry_publisher.get():
        conditions.append("publisher LIKE ?")
        params.append(
            f"%{entry_publisher.get()}%"
        )  # add % to the search term to search for any part of the text

    if entry_book_no.get():
        conditions.append("bookno LIKE ?")
        params.append(
            f"%{entry_book_no.get()}%"
        )  # add % to the search term to search for any part of the text

    if entry_cat.get():
        conditions.append("cat LIKE ?")
        params.append(
            f"%{entry_cat.get()}%"
        )  # add % to the search term to search for any part of the text

    if entry_title.get():  # If you want to include title search
        title_text = entry_title.get()  # Get the text *first*
        title_search_term = f"%{title_text}%"  # *Then* format it
        conditions.append("title LIKE ?")
        params.append(title_search_term)

    if conditions:
        query += " AND ".join(conditions)  # Combine conditions with AND
    else:
        query = """SELECT notes, publishinfo, shelf, cab, cat, bookno, publisher, writer, title, id 
               FROM books"""  # if no search terms show all books

    cursor.execute(query, tuple(params))  # Use parameters!
    rows = cursor.fetchall()
    conn.close()

    count = 0
    for row in rows:
        if count % 2 == 0:
            tree_books.insert(
                "", "end", values=row, tags=("evenrow",)
            )  # Correct values usage
        else:
            tree_books.insert(
                "", "end", values=row, tags=("oddrow",)
            )  # Correct values usage
        count += 1

    update_row_count_label(tree_books, row_count_label)


# @-------------------------------------- EDIT -------------------------------------------------
def book_edit():  # * edit book

    if entry_book_id.get() == "" or entry_title.get() == "":
        show_custom_message_box(f"تحذير: \n\n لا يوجد رقم و اسم")
    else:
        book_id = entry_book_id.get()
        book_title = entry_title.get()
        book_writer = entry_writer.get()
        book_publisher = entry_publisher.get()
        book_no = entry_book_no.get()
        book_cat = entry_cat.get()
        book_cab = entry_cab.get()
        book_shelf = entry_shelf.get()
        book_publishinfo = entry_pinfo.get()
        book_notes = entry_notes.get()
        conn = sqlite3.connect(APP_DB)
        cursor = conn.cursor()
        #!-------------------------------------------
        cursor.execute(
            """UPDATE books
            SET 
                title= ?   , 
                writer=?,
                publisher=?,
                bookno=?,
                cat=?,
                cab=?,
                shelf=?,
                publishinfo=?,
                notes=?
    
        WHERE id =?""",
            (
                book_title,
                book_writer,
                book_publisher,
                book_no,
                book_cat,
                book_cab,
                book_shelf,
                book_publishinfo,
                book_notes,
                book_id,
            ),
        )

        conn.commit()
        conn.close()
        filltree()


# @---------------------------------- DELETE -----------------------------------------------------
def book_delete():  # * delete book
    row_id = entry_book_id.get()
    conn = sqlite3.connect(APP_DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (row_id,))
    conn.commit()
    conn.close()
    filltree()


# @---------------------------------- ADD -----------------------------------------------------
def book_add():  # * add book
    book_id = entry_book_id.get()
    book_title = entry_title.get()
    book_writer = entry_writer.get()
    book_publisher = entry_publisher.get()
    book_no = entry_book_no.get()
    book_cat = entry_cat.get()
    book_cab = entry_cab.get()
    book_shelf = entry_shelf.get()
    book_publishinfo = entry_pinfo.get()
    book_notes = entry_notes.get()
    #!-------------------------------------------
    conn = sqlite3.connect(APP_DB)
    cursor = conn.cursor()
    #!-------------------------------------------
    cursor.execute("SELECT COUNT(*) FROM books WHERE id = ?", (book_id,))
    count = cursor.fetchone()
    if book_id == "":
        show_custom_message_box("تحذير: \n\n لا يوجد رقم و اسم")
    elif count is None or count[0] == 0:
        # Insert the new book record
        cursor.execute(
            """INSERT INTO books (id, title, writer,publisher,
            bookno,cat,cab,shelf,publishinfo,notes) VALUES (?, ?, ?,?,?,?, ?, ?,?,?)""",
            (
                book_id,
                book_title,
                book_writer,
                book_publisher,
                book_no,
                book_cat,
                book_cab,
                book_shelf,
                book_publishinfo,
                book_notes,
            ),
        )
        conn.commit()

    else:
        show_custom_message_box(f"تحذير: \n\nالكتاب رقم {book_id} \nموجود.")

    #!=========================================

    conn.close()
    filltree()


# @---------------------------------- SHOW -----------------------------------------------------
def book_show():  # * show books
    filltree()

# @--------------- بداية رسم الازرار---------------------------------
buttontxt_book = [
    " << تصدير",
    "مسح الخانات",
    " البحث (أو)",
    " البحث (مع)",
    "تعديل كتاب",
    "حذف كتاب",
    "اضافة كتاب",
    "عرض الكتب",
]
butt_func = [
    book_export_data,
    book_clear_field,
    book_search_or,
    book_search_and,
    book_edit,
    book_delete,
    book_add,
    book_show,
]
for i in range(0, 8):
    
    if i == 2 or i == 3 :
        button = ttk.Button(
            frame1,
            text=buttontxt_book[i],
            style="searchbook.TButton",
            command=butt_func[i],
        )  # Text color when clicked

        button.place(x=i * 105 + 160, y=222, width=100, height=40)
    else:
        button = ttk.Button(
            frame1,
            text=buttontxt_book[i],
            style="book.TButton",
            command=butt_func[i],
        )  # Text color when clicked

        button.place(x=i * 105 + 160, y=222, width=100, height=40) 

#! /////////////////  counter    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
row_count_label = tk.Label(
    frame1,
    text="Row Count: 0",
    font="Arial 14 bold",
    relief="sunken",
    bg="#555555",
    fg="#ffffff",
)
row_count_label.place(x=5, y=223, width=150, height=40)

# endregion

# region  Book Treeview       [rgba(10,50,0,1)]
# @----------------------------------------------------------------
#! define columns
tree_books = ttk.Treeview(
    frame1,
    columns=(
        "notes",
        "publishinfo",
        "shelf",
        "cab",
        "cat",
        "bookno",
        "publisher",
        "writer",
        "title",
        "bookid",
    ),
)
#! FFormat columns
tree_books.column("#0", width=0, stretch=tk.NO)
tree_books.column("bookid", width=60, anchor=CENTER, stretch=tk.NO)
tree_books.column("title", width=500, anchor=E, stretch=tk.NO)
tree_books.column("writer", width=400, anchor=E, stretch=tk.NO)
tree_books.column("publisher", width=450, anchor=E, stretch=tk.NO)
tree_books.column("bookno", width=80, anchor=CENTER, stretch=tk.NO)
tree_books.column("cat", width=80, anchor=CENTER, stretch=tk.NO)
tree_books.column("cab", width=60, anchor=CENTER, stretch=tk.NO)
tree_books.column("shelf", width=60, anchor=CENTER, stretch=tk.NO)
tree_books.column("publishinfo", width=450, anchor=E, stretch=tk.NO)
tree_books.column("notes", width=450, anchor=E, stretch=tk.NO)
#! FFormat heders
tree_books.heading("#0", text="")
tree_books.heading("bookid", text="م")
tree_books.heading("title", text="العنوان")
tree_books.heading("writer", text="المؤلف")
tree_books.heading("publisher", text="الناشر")
tree_books.heading("bookno", text="رقم ")
tree_books.heading("cat", text="التصنيف")
tree_books.heading("cab", text="الدولاب")
tree_books.heading("shelf", text="الرف")
tree_books.heading("publishinfo", text="معلومات الناشر")
tree_books.heading("notes", text="ملاحظات")

#! PLACE TREE
tree_books.place(x=0, y=270, width=1000, height=400)
# todo================ scroll bar ================================

verscrlbar = ttk.Scrollbar(
    tree_books,
    orient="vertical",
    command=tree_books.yview,
)
verscrlbar.pack(side="left", fill="y")
# #!---------------------------------------------------------------------------
herscrlbar = ttk.Scrollbar(
    tree_books,
    orient="horizontal",
    command=tree_books.xview,
)
herscrlbar.pack(side="bottom", fill="x")

tree_books.xview_moveto(1.0)
tree_books.configure(yscrollcommand=verscrlbar.set, xscrollcommand=herscrlbar.set)


#! ------------  FILL TREE  ------------------------------
def filltree():
    conn = sqlite3.connect(APP_DB)
    cursor = conn.cursor()
    tree_books.delete(*tree_books.get_children())
    cursor.execute(
        """SELECT notes,publishinfo,shelf,
                   cab,cat,bookno,publisher, writer,title,id  
                   FROM books"""
    )

    rows = cursor.fetchall()
    count = 0
    for row in rows:
        if count % 2 == 0:
            tree_books.insert("", "end", text=row, values=(row), tags=("evenrow",))
        else:
            tree_books.insert("", "end", text=row, values=(row), tags=("oddrow",))

        count += 1
    conn.close()
    #!--------------------------------------------------------
    tree_books.tag_configure("evenrow", background="#aaaaaa")
    tree_books.tag_configure("oddrow", background="#eeeeee")

    update_row_count_label(tree_books, row_count_label)


# calll filltree
filltree()


#! ------------  select data from TREE  ------------------------------
def on_treeview_double_click(event):
    if tree_books.identify_region(event.x, event.y) == "separator":
        return "break"
    item = tree_books.identify("item", event.x, event.y)
    if item:
        item_values = tree_books.item(item, "values")
        entry_book_id.delete(0, tk.END)
        entry_book_id.insert(0, item_values[9])

        entry_title.delete(0, tk.END)
        entry_title.insert(0, item_values[8])

        entry_writer.delete(0, tk.END)
        entry_writer.insert(0, item_values[7])

        entry_publisher.delete(0, tk.END)
        entry_publisher.insert(0, item_values[6])

        entry_book_no.delete(0, tk.END)
        entry_book_no.insert(0, item_values[5])

        entry_cat.delete(0, tk.END)
        entry_cat.insert(0, item_values[4])

        entry_cab.delete(0, tk.END)
        entry_cab.insert(0, item_values[3])

        entry_shelf.delete(0, tk.END)
        entry_shelf.insert(0, item_values[2])

        entry_pinfo.delete(0, tk.END)
        entry_pinfo.insert(0, item_values[1])

        entry_notes.delete(0, tk.END)
        entry_notes.insert(0, item_values[0])


def block_resize(event):  # prevent resize column
    if tree_books.identify_region(event.x, event.y) == "separator":
        return "break"


tree_books.bind("<Double-1>", on_treeview_double_click)
tree_books.bind("<Button-1>", block_resize)
# endregion

# region  FRAME borrow        [rgba(10,80,80,1)]
# @----------------------------------------------------------------
lbl_footer = tk.Label(
    frame3,
    text="""  غير متوفر فى النسخة التجريبية
    
    قم بالتحديث 
        """,
    font="Arial 18 bold",
    justify="center",
    bg="skyblue3",
)
lbl_footer.place(anchor="center", relx=0.5, rely=0.5)


# endregion

# region  FRAME Members       [rgba(0,0,255,0.1)]
# @----------------------------------------------------------------
lbl_footer = tk.Label(
    frame2,
    text="""  غير متوفر فى النسخة التجريبية
    
    قم بالتحديث 
        """,
    font="Arial 18 bold",
    justify="center",
    bg="skyblue2",
)
lbl_footer.place(anchor="center", relx=0.5, rely=0.5)
# endregion

# region  FRAME ABOUT         [rgba(255,0,0,0.3)]
# @----------------------------------------------------------------
lbl_footer = tk.Label(
    frame4,
    text="""مرحبا بكم فى  
        \n نظام سما نور لادارة المكتبات
        \n اصدار 4.00
        \nتطوير م/هانئ عصمت 
        \nhanytolba@gmail.com
        """,
    font="Arial 18 bold",
    justify="center",
    bg="lightgray",
)
lbl_footer.pack(expand=True, fill="both")
# endregion

frame1.tkraise()
root.mainloop()
