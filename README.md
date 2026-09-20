# Personal Finance Manager

A personal finance management system developed in Python with SQL Server integration.

## 📌 About the Project

**Personal Finance Manager** is a simple application for managing financial transactions. It allows users to register and view income and expenses, list transactions, and calculate their current balance.

The project was developed to practice the integration between a Python application and a SQL Server database, including database operations such as insertion, querying, updating, and deletion.

## 🛠️ Technologies

* Python
* SQL Server
* pyodbc
* Git
* GitHub
* VS Code

## 📂 Project Structure

```text
personal-finance-manager/
│
├── src/
│   ├── main.py
│   └── database.py
│
├── sql/
│   └── database.sql
│
├── .gitignore
└── README.md
```

## ⚙️ Features

* Add income transactions
* Add expense transactions
* List financial transactions
* Calculate the current balance
* Store financial data in SQL Server
* Retrieve data from the database
* Perform financial calculations using database queries

## 🗄️ Database

The project uses a SQL Server database named **PersonalFinanceManager**.

### Categories

The `categorias` table stores the categories used by financial transactions:

* Salary
* Food
* Housing
* Transportation
* Leisure

### Transactions

The `transacoes` table stores financial transactions with the following information:

* ID
* Description
* Amount
* Type
* Date
* Category

## 🔌 Python + SQL Server Integration

The application communicates with SQL Server using the **pyodbc** library.

The database connection is used to perform operations such as:

* inserting new transactions;
* retrieving transactions;
* calculating the financial balance;
* accessing stored database information.

## ▶️ How to Run

1. Make sure SQL Server is installed and running.
2. Create the `PersonalFinanceManager` database.
3. Execute the SQL script located at:

```text
sql/database.sql
```

4. Install the required Python dependency:

```bash
pip install pyodbc
```

5. Run the application:

```bash
python src/main.py
```

## 📋 Application Menu

```text
===== PERSONAL FINANCE MANAGER =====
1. Add income
2. Add expense
3. List transactions
4. Check balance
0. Exit
```

## 🎯 Learning Objectives

This project was developed to practice:

* Python
* SQL
* SQL Server
* Basic database modeling
* Python and database integration
* CRUD operations
* Git and GitHub
* Project organization

## 📈 Future Improvements

Possible future improvements include:

* Input validation
* Category selection by name
* Improved transaction display
* Financial reports
* Graphical interface
* Additional database features

## ✅ Status

**Completed**

Developed as part of my Software Engineering studies.
