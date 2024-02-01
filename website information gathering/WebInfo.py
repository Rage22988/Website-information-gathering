import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

# Function to gather website data
def gather_website_data():
    # Get the URL from the entry widget
    url = url_entry.get()

    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for unsuccessful requests

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant data from the HTML
        links = soup.find_all('a')
        paragraphs = soup.find_all('p')
        title = soup.title.text

        # Display the gathered data in the text widget
        data_text.delete('1.0', tk.END)
        data_text.insert(tk.END, f"Title: {title}\n\n")
        data_text.insert(tk.END, "Links:\n")
        for link in links:
            data_text.insert(tk.END, f"- {link.get('href')}\n")
        data_text.insert(tk.END, "\nParagraphs:\n")
        for paragraph in paragraphs:
            data_text.insert(tk.END, f"- {paragraph.text.strip()}\n")
    except requests.RequestException as e:
        # Show error message if there is an issue with fetching data
        messagebox.showerror("Error", f"Failed to retrieve data from {url}: {e}")

# Create the main window
root = tk.Tk()
root.title("WebInfo Gathering")
root.geometry("800x600")

# Create URL entry
url_label = ttk.Label(root, text="Enter URL:")
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=60)
url_entry.pack(pady=5)

# Create fetch data button
fetch_button = ttk.Button(root, text="Fetch Data", command=gather_website_data)
fetch_button.pack(pady=10)

# Create text widget to display gathered data
data_text = tk.Text(root, width=80, height=20)
data_text.pack(padx=10, pady=10)

# Run the main event loop
root.mainloop()

