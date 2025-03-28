# Personal Library Manager 📚

## Overview 🌟

The **Personal Library Manager** is a command-line tool designed to help you manage your book collection. You can easily add, remove, search, display, and analyze your library with a user-friendly menu system. The library is saved to a file, so it persists between sessions.

## Features 🎯

### 1. **Add a Book ➕**
   - Prompts the user for the book's title, author, published year, genre, and read status, and then adds the book to the library.

### 2. **Remove a Book 🗑️**
   - Removes a book from the library based on its title and confirms the action.

### 3. **Search for a Book 🔎**
   - Prompts the user to search by either title or author, and displays matching books.

### 4. **Display All Books 📖**
   - Displays all books in the library, showing details like title, author, genre, and read status.

### 5. **Display Statistics 📊**
   - Displays the total number of books and the percentage of books that have been read.

### 6. **Exit 🚪**
   - Exits the program and saves the library data to the file.

---

## Optional Features ⚙️

### File Handling (Save/Load) 💾

- Saves and loads the library data from a file (`library.txt`), ensuring that the data is preserved between sessions.

---

## Example Usage 🚀

### Menu 📝
When you run the program, you will be presented with a menu that allows you to choose various options like adding a book, removing a book, searching, displaying statistics, and more.

### Add a Book 📝
The program will prompt you to enter the book's title, author, publication year, genre, and whether you have read the book or not. Once added, the book will be stored in your library.

### Remove a Book 🗑️
You can remove a book from the library by providing the title of the book you wish to delete. The program will confirm if the book was removed successfully.

### Search for a Book 🔎
You can search for books either by title or by author. The program will display all the books that match your search criteria.

### Display All Books 📖
This option will show you all the books in your library, along with their details like title, author, genre, and read status.

### Display Statistics 📊
The program will calculate and display the total number of books in your library and the percentage of books you have read.

---

## Requirements 💻

- **Python**: Make sure you have Python installed.
- **Libraries**: Uses the `json` and `os` libraries for file handling and operating system interactions.

---

## Conclusion 🎉

This **Personal Library Manager** helps you organize your book collection efficiently, keeping track of books you've read and books you plan to read, with the ability to add, remove, and search through your library. The optional file handling ensures data persistence between program runs.
