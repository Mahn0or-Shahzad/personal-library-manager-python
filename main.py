import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file,'r') as file:
            return json.load(file)
    return[]

def save_library(library):
    with open(data_file,'w') as file:
        json.dump(library,file,indent=4)

def add_book(library):
    title = input("📝 Enter the title of the book: ")
    author = input("👤 Enter the author of the book: ")
    published_year = input("📅 Enter the published_year of the book: ")
    genre = input("📁 Enter the genre of the book: ")
    read = input("📖 Have you read this book? (yes/no): ").lower() == 'yes'
    
    new_book = {
        'title' : title,
        'author' : author,
        'published_year': published_year,
        'genre' : genre,
        'read' : read 
     }
    library.append(new_book)
    save_library(library)
    print(f"📖 Book {title} added successfully! 🎉")

def remove_book(library):
    title =input("🗑️ Enter the title book to remove from the library: ")
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_length:
        print(f"✅ Book {title} removed successfully!")
    else:
        print(f"❌ Book {title} not found in the library!")

def search_book(library):
    search_by = input("🔎 Search by title or author: ").lower()
    search_term = input("✎ Enter the {search_by} ").lower()
    result = [book for book in library if search_term in book[search_by].lower()]

    if result:
        for book in result:
            status = '✅Read' if book ['read'] else "📌 Unread"
            print(f"📚 {book['title']} by {book['author']} - 📅 {book['published_year']} - 📁 {book['genre']} - {status}")
    else:
        print(f"⚠️ No book found matching!")

def display_all_book(library):
    if library:
        for book in library:
            status = '✅ Read' if book ['read'] else "📌 Unread"
            print(f"📖 {book['title']} by {book['author']} - 📅 {book['published_year']} - 📁 {book['genre']} - {status}")
    else:
        print("🚫 The library is empty!")

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book ['read']])
    percentage_read = (total_books / read_books) * 100 if total_books > 0 else 0
    print(f"📚 total_books: {total_books}")
    print(f"📖 percentage_read: {percentage_read}%")
    
def main():
    library = load_library()
    while True:
        print("📚 Welcome to your Personal Library Manager!")
        print("📌 Menu:")
        print(" 1️⃣  Add a book ➕")
        print(" 2️⃣  Remove a book 🗑️")
        print(" 3️⃣  Search for a book 🔎")  
        print(" 4️⃣  Display all books 📖") 
        print(" 5️⃣  Display statistics 📊")  
        print(" 6️⃣  Exit 🚪")  

        choice = input("🔢 Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':    
            display_all_book(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("✅ Library saved to file. Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == '__main__':
    main()