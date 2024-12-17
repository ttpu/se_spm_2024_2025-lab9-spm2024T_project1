[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Z2qKazcY)
## Team N:

* _(ID, Name, Surname)_
* Student N1:
* Student N2:
* Student N3:
* Student N4:

# Expense Tracker: Project Description

## Overview

The **Expense Tracker** is a simple, publicly accessible web application designed to allow users to track and manage expenses. It does not require user accounts or logins, making it ideal for quick demonstrations and practice in developing web-based applications.

The website provides a clean and intuitive interface where users can view, add, edit, delete, and sort expenses. All users share the same expense list, so changes made by one user are immediately visible to others. 

The application is lightweight, built using Flask, HTML, CSS, and a simple database (SQLite or JSON) for data persistence.

---

## Key Features

### 1. Expense List
- Displays all expenses in a tabular format.
- Columns:
  - **Date**: The date of the expense.
  - **Title**: A short description of the expense (e.g., "Groceries", "Internet Bill").
  - **Category**: The category of the expense (e.g., Food, Utilities, Transportation).
  - **Amount**: The cost of the expense.
  - **Actions**: Buttons for editing and deleting each expense.
- The table header includes clickable buttons/links for sorting expenses by:
  - **Category**: Groups expenses by their categories (e.g., all "Food" expenses together, all "Utilities" expenses together).
  - **Date**: Sorts expenses in ascending or descending order by date.
  - **Amount**: Sorts expenses by amount, from smallest to largest or vice versa.
  - **Title**: Alphabetically sorts expenses by title.

---

### 2. Add Expense
- A simple form with the following fields:
  - **Date**: Pre-filled with the current date but can be adjusted by the user.
  - **Title**: Text input for the name/description of the expense.
  - **Category**: Dropdown menu with predefined categories (e.g., Food, Utilities, Transportation, Miscellaneous).
  - **Amount**: Number input for the expense amount.
- A "Submit" button to add the expense to the list.

---

### 3. Edit Expense
- Clicking the "Edit" button on an expense row opens a pre-filled form with the existing details of the expense.
- The form allows users to:
  - Modify the date, title, category, or amount.
- A "Save Changes" button to update the expense in the list.

---

### 4. Delete Expense
- Clicking the "Delete" button removes the selected expense from the list after confirmation.
- Simple confirmation message: “Are you sure you want to delete this expense?”

---

### 5. Summary Section
- A simple textual summary displayed above or below the table:
  - Total number of expenses.
  - Total amount spent.
  - Total amount spent per category (e.g., Food: $50, Utilities: $30).
- Updated dynamically whenever an expense is added, edited, or deleted.

---

### 6. Sorting Functionality
- The expense list includes a **Sort By** dropdown menu with the following options:
  - **Category**: Groups all expenses by their category.
  - **Date (Ascending/Descending)**: Sorts by expense date.
  - **Amount (Low to High/High to Low)**: Sorts expenses numerically by amount.
  - **Title (A-Z/Z-A)**: Alphabetical sorting of expense titles.
- Clicking the table header or using the dropdown triggers the sorting feature.
- Sorting persists across page reloads by updating the database or session-based state.

---

### 7. Data Persistence
- All expenses are stored in a **JSON file** or **SQLite database**.
- Changes to the list (add/edit/delete/sort) are immediately saved, ensuring persistence across server restarts.

---

### 8. No User Authentication
- No login or user accounts are required.
- The application is fully open for anyone accessing the site.

---
