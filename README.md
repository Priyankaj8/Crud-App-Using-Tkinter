# STUDENT MANAGEMENT SYSTEM 
---
This is a simple Student Management System built using Python with `Tkinter` for the GUI and `PostgreSQL` for database management. The system allows users to add, update, delete, and view student records. The project also includes functionality to create the database table if it doesn't exist.

## Features

- **Create Table**: Creates a PostgreSQL table to store student data if it doesn't exist.
- **Add Data**: Insert student information (Name, Address, Age, and Phone Number) into the database.
- **Update Data**: Update existing student records.
- **Delete Data**: Delete student records from the database.
- **View Data**: View all student records in a table format.
---
## Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.x**
- **PostgreSQL** for the database
- **Required Python Libraries**:
  - `Tkinter` (Usually comes pre-installed with Python)
  - `psycopg2`: For PostgreSQL database interaction.
  - `python-dotenv`: For loading environment variables from `.env` file.
--- 
## Run the Program:
To start the Student Management System, execute the following command in your terminal:

```bash
python student_management_system.py
```
---
## Using the Interface:
- **Create Table:** Click "Create Table" to initialize the students table in PostgreSQL.
- **Add Data:** Enter student details (Name, Address, Age, Phone Number) and click "Add Data" to insert the information into the database.
- **Update Data:** Select a record from the table, modify the student details, and click "Update Data" to save the changes.
- **Delete Data:** Select a record from the table and click "Delete Data" to remove it from the database.
- **View Data:** The records will automatically refresh and display in the table view.
---
## Screenshot
![crud-1](https://github.com/user-attachments/assets/91708b23-94b0-4b21-85f0-f574ad2d4495)
![crud-2](https://github.com/user-attachments/assets/b6552a06-4196-4471-a94a-e5f56405ea85)
![crud-3](https://github.com/user-attachments/assets/236ce0f7-16aa-4571-be25-bff60ca0d949)
![crud-4](https://github.com/user-attachments/assets/3a2a9fc9-0988-4078-b93d-8d9e58922897)
![crud-5](https://github.com/user-attachments/assets/d48e0bd9-83e8-4742-be89-7323e2470510)
![crud-6](https://github.com/user-attachments/assets/6daf432b-774a-479b-be8f-04dc0f3f7bb8)
![crud-7](https://github.com/user-attachments/assets/c0219694-b51c-423a-86be-49bda84696a0)
---
## Troubleshooting
### Error connecting to the database:

Check your .env file for correct database credentials.
Ensure that PostgreSQL is running.
### Missing libraries:

If you encounter missing module errors, install the required libraries:
```bash
pip install psycopg2 python-dotenv
```
