import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

def fetch_listing():
    api_url = entry_api_url.get()
    api_key = entry_api_key.get()

    headers = {
        "api_key": api_key,
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        try:
            listing = response.json()
            listing_info = f"Listing ID: {listing.get('id', '')}\n"
            listing_info += f"Float Value: {listing.get('item', {}).get('float_value', '')}\n"
            listing_info += f"Price: {listing.get('price', '')}\n"
            listing_info += f"Description: {listing.get('description', '')}\n"
            listing_info += f"Market Hash Name: {listing.get('item', {}).get('market_hash_name', '')}\n"

            listing_text.delete(1.0, tk.END)  # Clear previous content
            listing_text.insert(tk.END, listing_info)

            messagebox.showinfo("Extraction Completed", "Extraction completed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showerror("Error", f"Failed to grab listing. Error: {response.status_code}")

# Create the main window
root = tk.Tk()
root.title("Listing Extractor")

# Create labels and entry widgets
label_api_url = tk.Label(root, text="API URL:")
entry_api_url = tk.Entry(root)
label_api_key = tk.Label(root, text="API Key:")
entry_api_key = tk.Entry(root)
button_fetch = tk.Button(root, text="Fetch Listing", command=fetch_listing)
listing_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)

# Arrange widgets using grid layout
label_api_url.grid(row=0, column=0, padx=10, pady=10)
entry_api_url.grid(row=0, column=1, padx=10, pady=10)
label_api_key.grid(row=1, column=0, padx=10, pady=10)
entry_api_key.grid(row=1, column=1, padx=10, pady=10)
button_fetch.grid(row=2, columnspan=2, padx=10, pady=10)
listing_text.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
