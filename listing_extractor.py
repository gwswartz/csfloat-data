import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

def fetch_listings():
    api_key = entry_api_key.get()
    market_hash_name = entry_market_hash_name.get()

    headers = {
        "api_key": api_key,
    }

    api_endpoint = "https://csfloat.com/api/v1/listings"  # Update with the correct API endpoint

    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        try:
            listings = response.json()

            matching_listings = []
            for listing in listings:
                item = listing.get('item', {})
                if item.get('market_hash_name') == market_hash_name:
                    matching_listings.append(listing)

            listing_text.delete(1.0, tk.END)  # Clear previous content

            if matching_listings:
                for listing in matching_listings:
                    listing_info = f"Listing ID: {listing.get('id', '')}\n"
                    listing_info += f"Float Value: {listing.get('item', {}).get('float_value', '')}\n"
                    listing_info += f"Price: {listing.get('price', '')}\n"
                    listing_info += f"Description: {listing.get('description', '')}\n"
                    listing_info += f"Market Hash Name: {listing.get('item', {}).get('market_hash_name', '')}\n"
                    listing_info += "\n"

                    listing_text.insert(tk.END, listing_info)
                
                messagebox.showinfo("Extraction Completed", "Extraction completed successfully")
            else:
                messagebox.showinfo("No Listings", "No listings found for the specified market_hash_name.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showerror("Error", f"Failed to grab listings. Error: {response.status_code}")

# Create the main window
root = tk.Tk()
root.title("CSFloat Listing Extractor")

# Add labels and entries for API Key and market_hash_name
label_api_key = tk.Label(root, text="API Key:")
entry_api_key = tk.Entry(root)
label_api_key.grid(row=0, column=0, padx=10, pady=10)
entry_api_key.grid(row=0, column=1, padx=10, pady=10)

label_market_hash_name = tk.Label(root, text="Market Hash Name:")
entry_market_hash_name = tk.Entry(root)
label_market_hash_name.grid(row=1, column=0, padx=10, pady=10)
entry_market_hash_name.grid(row=1, column=1, padx=10, pady=10)

# Add the "Fetch Listings" button
button_fetch = tk.Button(root, text="Fetch Listings", command=fetch_listings)
button_fetch.grid(row=2, columnspan=2, padx=10, pady=10)

# Add the listing_text area
listing_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
listing_text.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
