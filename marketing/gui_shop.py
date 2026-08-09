import tkinter as tk
from tkinter import ttk, messagebox

class KalanantiShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalananti Shop (Python Level 3)")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        # --- Header ---
        header_frame = tk.Frame(root, bg="#2c3e50", pady=10)
        header_frame.pack(fill="x")
        
        # Try to load logo
        try:
            import os
            script_dir = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(script_dir, "kalananti_logo.png")
            
            if os.path.exists(logo_path):
                self.logo_original = tk.PhotoImage(file=logo_path)
                # Subsample to make it smaller (User requested smaller)
                self.logo_img = self.logo_original.subsample(6, 6) 
                logo_label = tk.Label(header_frame, image=self.logo_img, bg="#2c3e50")
                logo_label.pack(pady=5)
        except Exception as e:
            print(f"Error loading logo: {e}")

        # Removed text headers as requested ("warung" style)

        # --- Input Section ---
        input_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
        input_frame.pack()

        tk.Label(input_frame, text="Product Name:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_name = tk.Entry(input_frame, width=25)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Price (IDR):", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_price = tk.Entry(input_frame, width=25)
        self.entry_price.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Quantity:", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_qty = tk.Entry(input_frame, width=25)
        self.entry_qty.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        btn_add = tk.Button(input_frame, text="Add to Cart", command=self.add_to_cart, bg="#27ae60", fg="black", width=15)
        btn_add.grid(row=3, column=0, columnspan=2, pady=10)

        # --- Cart/Output Section ---
        self.cart_text = tk.Text(root, height=15, width=55)
        self.cart_text.pack(padx=20, pady=10)
        self.cart_text.insert(tk.END, "Item Name\t\tQty\tPrice\t\tTotal\n")
        self.cart_text.insert(tk.END, "-"*65 + "\n")
        
        # --- Total Section ---
        self.total_price = 0
        self.lbl_total = tk.Label(root, text="Total: IDR 0", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#c0392b")
        self.lbl_total.pack(pady=10)

        # --- Footer ---
        footer_label = tk.Label(root, text="Designed for Python Level 3 Marketing", font=("Arial", 8), bg="#f0f0f0", fg="gray")
        footer_label.pack(side="bottom", pady=5)

    def add_to_cart(self):
        name = self.entry_name.get()
        price = self.entry_price.get()
        qty = self.entry_qty.get()

        if not name or not price or not qty:
            messagebox.showwarning("Input Error", "Please fill all fields!")
            return

        try:
            price = int(price)
            qty = int(qty)
            total = price * qty
            
            line = f"{name}\t\t{qty}\t{price:,}\t\t{total:,}\n"
            self.cart_text.insert(tk.END, line)
            
            self.total_price += total
            self.lbl_total.config(text=f"Total: IDR {self.total_price:,}")
            
            # Clear inputs
            self.entry_name.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
            self.entry_qty.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Input Error", "Price and Quantity must be numbers!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KalanantiShopApp(root)
    root.mainloop()
