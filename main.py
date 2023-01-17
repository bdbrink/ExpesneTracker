#!/usr/bin/env python3

import sqlite3
import datetime

conn = sqlite3.connect("database/expenses.db")
cur = conn.cursor()

while True:
    print("Select and option:")
    print("1. Enter a new expense")
    print("2. view expenses")

    choice = int(input())

    if choice == 1:
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        date = input("Enter the description: ")

        cur.execute("SELECT DISTINCT category FROM expenses")

        categories = cur.fetchall()
        print("select a category by number")

        for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category[0]}")
        print(f"{len(categories) + 1}. Create a new category")

        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("enter new name of category: ")
        else:
            category = categories[category_choice - 1][0]

        price = input("enter price for expense: ")
        
        cur.execute("INSERT INTO expenses (Date, description, category, price) VALUES (?, ?, ?, ?)", (date, description, category, price))

        conn.commit()

    elif choice == 2:
        print("select and option:")
        print("1. view all expenses")
        print("2. view monthly expenses by category")

        view_choice = int(input())
        if view_choice == 1:
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall

            for expense in expenses:
                print(expense)
        elif view_choice == 2:
            month = input("enter the month (MM): ")
            year = input("enter the year (YYYY): ")
            cur.execute("""SELECT category, SUM(price) FROM expenses 
                        WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ?
                        GROUP BY category""", (month, year))
            expenses = cur.fetchall()

            for expense in expenses:
                print(f"Category: {expense[0]}, Total: {expense[1]}")
        else:
            exit()
    else:
        exit()

    repeat = input("Would you like to do something else (y/n) ? \n")
    if repeat.lower() != "y":
        break

conn.close()
