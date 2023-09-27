import tkinter as tk
import tkinter.messagebox as tkmb
from tkinter import ttk

search_entry = None
search_placeholder = "🔍 Enter keyword"  # Unicode search icon
user_entry = None
user_pass = None
login_window = None

def login():
    global login_window

    username = "admin"
    password = "12345"

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
        if login_window:
            login_window.destroy()
            login_window = None
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password', message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username', message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid username and password")

def open_search_page():
    global search_entry, login_window

    search_window = tk.Tk()
    search_window.geometry("800x400")
    search_window.title("Search Page")

    # Create the main frames
    sidebar_frame = tk.Frame(search_window, width=200, bg="lightgray")
    sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

    main_frame = tk.Frame(search_window)
    main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Create the sidebar
    sidebar = Sidebar(sidebar_frame)
    sidebar.pack(fill=tk.Y, pady=20, padx=10)

    # Main content
    label = tk.Label(main_frame, text="Search Page", font=("Arial", 16, "bold"))
    label.pack(pady=20)

    category_frame = tk.Frame(main_frame)
    category_frame.pack(pady=10)

    categories = ["Location", "Ads Company", "Category 3", "Category 4"]  # Replace with your own categories
    category_combobox = ttk.Combobox(category_frame, values=categories, font=("Arial", 12))
    category_combobox.pack(side=tk.LEFT, padx=5)

    search_frame = tk.Frame(main_frame)
    search_frame.pack(pady=20)

    search_entry = PlaceholderEntry(search_frame, width=30, placeholder_text=search_placeholder, font=("Arial", 12))
    search_entry.pack(side=tk.LEFT, padx=5)

    search_button = tk.Button(search_frame, text="Search", command=perform_web_scraping, font=("Arial", 12), width=10)
    search_button.pack(side=tk.LEFT)

    search_window.mainloop()

def perform_web_scraping():
    keyword = search_entry.get()
    if keyword:
        tkmb.showinfo(title="Search Result", message=f"Performing web scraping with keyword: {keyword}")
    else:
        tkmb.showwarning(title="No Keyword", message="Please enter a keyword to search")

def open_login_page():
    global login_window, user_entry, user_pass

    if login_window and login_window.winfo_exists():
        login_window.lift()
        return

    login_window = tk.Toplevel()
    login_window.geometry("400x400")
    login_window.title("Facebook Login Page")

    label = tk.Label(login_window, text="Facebook UI Page", font=("Arial", 16, "bold"))
    label.pack(pady=20)

    frame = tk.Frame(login_window)
    frame.pack(pady=20, padx=40)

    label = tk.Label(frame, text='Facebook Login Page', font=("Arial", 12))
    label.pack(pady=12, padx=10)

    user_entry = PlaceholderEntry(frame, placeholder_text="Username", font=("Arial", 12))
    user_entry.pack(pady=12, padx=10)

    user_pass = PlaceholderEntry(frame, placeholder_text="Password", show="*", font=("Arial", 12))
    user_pass.pack(pady=12, padx=10)

    button = tk.Button(frame, text='Login', command=login, font=("Arial", 12), width=10)
    button.pack(pady=12, padx=10)

    login_window.mainloop()

class Sidebar(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(background="lightgray")

        # Sidebar content
        label = tk.Label(self, text="Sidebar", font=("Arial", 14, "bold"), bg="lightgray")
        label.pack(pady=10)

        # Settings button
        settings_button = tk.Button(self, text="Settings", command=self.show_settings)
        settings_button.pack(pady=10)

        # Additional buttons
        self.login_button = None
        self.delete_cookies_button = None

    def show_settings(self):
        # Remove previous buttons if they exist
        if self.login_button:
            self.login_button.destroy()
        if self.delete_cookies_button:
            self.delete_cookies_button.destroy()

        # Create new buttons
        self.login_button = tk.Button(self, text="Login", command=open_login_page)
        self.login_button.pack(pady=5)

        self.delete_cookies_button = tk.Button(self, text="Delete Cookies", command=self.delete_cookies)
        self.delete_cookies_button.pack(pady=5)

    def delete_cookies(self):
        # Implement the functionality to delete cookies here
        tkmb.showinfo(title="Cookies Deleted", message="Cookies have been deleted")

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder_text="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder_text = placeholder_text
        self.placeholder_color = "gray"
        self.default_color = self.cget("fg")

        self.bind("<FocusIn>", self.remove_placeholder)
        self.bind("<FocusOut>", self.set_placeholder)

        self.set_placeholder()

    def remove_placeholder(self, event=None):
        if self.get() == self.placeholder_text:
            self.delete(0, tk.END)
            self.config(fg=self.default_color)

    def set_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder_text)
            self.config(fg=self.placeholder_color)

open_search_page()

