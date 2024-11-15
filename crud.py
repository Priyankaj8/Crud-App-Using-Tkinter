from tkinter import *
from tkinter import ttk
import psycopg2
from tkinter import messagebox
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get database credentials from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")

# Now use these credentials to connect to the PostgreSQL database
try:
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=db_port
    )
    print("Connected to the database successfully!")
except Exception as e:
    print("Error while connecting to the database:", e)

def run_query(query,parameters=()): #to execute sql query
    conn = psycopg2.connect(dbname=db_name,user=db_user,password=db_password,host=db_host,port=db_port)
    cur = conn.cursor()
    query_result = None
    try:        #sometimes query might fail, so to avoid program from breaking we include the code in try block
        cur.execute(query,parameters)
        if query.lower().startswith("select"):   #as delete query doesn't give back any result
            query_result = cur.fetchall()
        conn.commit()
    except psycopg2.Error as e:
        messagebox.showerror("Database Error",str(e))

    finally:
        cur.close()
        conn.close()

    return query_result

def refresh_treeview(): # It refreshes everytime the fucntion is called
    for item in tree.get_children(): # everytime refresh_treeview  is called the same data is added to the treeview, to avoid that we delete the data before the query is executed.
        tree.delete(item)
    records = run_query("select * from students;")
    for record in records:  #inserts the records to tree view
        tree.insert('',END,values=record)

def insert_data():
    query = "insert into students(name,address,age,number)values(%s,%s,%s,%s)"
    parameters = (name_entry.get(), address_entry.get(), age_entry.get(), phone_entry.get())
    run_query(query,parameters)
    messagebox.showinfo("Information", "Data inserted sucessfully!")
    refresh_treeview()

def delete_data():
    selected_item = tree.selection()[0]    #gives the selected row
    student_id = tree.item(selected_item)['values'][0]
    query = "delete from students where student_id=%s"
    parameters = (student_id,)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data deleted successfully!")
    refresh_treeview()

def update_data():
    selected_item = tree.selection()[0]    #gives the selected row
    student_id = tree.item(selected_item)['values'][0]
    query = "update students set name= %s,address=%s, age=%s, number=%s where student_id=%s"
    parameters = (name_entry.get(), address_entry.get(), age_entry.get(), phone_entry.get(), student_id)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data updated successfully!")
    refresh_treeview()

def create_table():
    query = "create table if not exists students(student_id serial primary key,name text,address text, age int, number text);"
    run_query(query)
    messagebox.showinfo("Information","Table created!")
    refresh_treeview()

#creating a window
root = Tk()
root.title("Student Management System")

#creating the frame
frame = LabelFrame(root, text="Student Data") #labelframe allows us place entries and labels on frame
frame.grid(row=0, column = 0, padx=10, pady=10,sticky="ew") #sticky is used for alignment 
#ew - east and west, we are making the label stretch from RHS to LHS

Label(frame, text="Name:").grid(row=0,column=0,padx=2,sticky="w")
name_entry = Entry(frame)
name_entry.grid(row=0,column=1,pady=2,sticky="ew")

Label(frame, text="Address:").grid(row=1,column=0,padx=2,sticky="w")
address_entry = Entry(frame)
address_entry.grid(row=1,column=1,pady=2,sticky="ew")

Label(frame, text="Age:").grid(row=2,column=0,padx=2,sticky="w")
age_entry = Entry(frame)
age_entry.grid(row=2,column=1,pady=2,sticky="ew")

Label(frame, text="Phone Number:").grid(row=3,column=0,padx=2,sticky="w")
phone_entry = Entry(frame)
phone_entry.grid(row=3,column=1,pady=2,sticky="ew")

button_frame = Frame(root)
button_frame.grid(row=1,column=0,pady=5,sticky="ew")
Button(button_frame,text="Create Table",command=create_table).grid(row=0,column=0,padx=5)
Button(button_frame,text="Add Data",command=insert_data).grid(row=0,column=1,padx=5)
Button(button_frame,text="Update Data",command=update_data).grid(row=0,column=2,padx=5)
Button(button_frame,text="Delete Data",command=delete_data).grid(row=0,column=3,padx=5)

tree_frame = Frame(root)
tree_frame.grid(row=2,column=0,padx=10,sticky="nsew")

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="browse")  #yscrollcommand - links the scroll bar with the tree view, selectmode="browse", let's us select particular data in the treeview
tree.pack()
tree_scroll.config(command=tree.yview)  #connecting scrollbar to the treeview, it enables the scrollbar to control the vertical position of the content in the tree

tree['columns']=("student_id","name","address","age","number") #creating the columns on the treeview

#configuring columns
tree.column("#0",width=0,stretch=NO)    #makes the column invisible -> #0 is used for heirarchical structure, as we do not have any we make it invisible
tree.column("student_id",anchor=CENTER,width=80)
tree.column("name",anchor=CENTER,width=120)
tree.column("address",anchor=CENTER,width=120)
tree.column("age",anchor=CENTER,width=50)
tree.column("number",anchor=CENTER,width=120)

#configuring headings of the treeview
tree.heading("student_id",text="ID",anchor=CENTER)
tree.heading("name",text="Name",anchor=CENTER)
tree.heading("address",text="Address",anchor=CENTER)
tree.heading("age",text="Age",anchor=CENTER)
tree.heading("number",text="Phone Number",anchor=CENTER)

refresh_treeview()
root.mainloop()