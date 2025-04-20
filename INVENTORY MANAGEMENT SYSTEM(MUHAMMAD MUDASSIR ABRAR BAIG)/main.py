import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
from product import Product
from inventory import Inventory
from theme_manager import ThemeManager
from undo_redo import UndoRedoManager
from report_generator import ReportGenerator

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1540x800+0+0")
        self.root.resizable(False, False)
        self.root.configure(bg="#1C1F2E")
        
        title_icon = tk.PhotoImage(file ="inventory-management.png").subsample(10, 10)
        
        # Header
        header = tk.Label(
            self.root, text="Inventory Management System",
            font=("Segoe UI", 35, "bold"),
            bg="#1C1F2E", 
            fg="#E3B04B", 
            pady=40,
            image = title_icon,
            compound = tk.LEFT,
            background="#1C1F2E",
        )
        header.image = title_icon  
        header.pack(fill="x")
        footer = tk.Label(
            self.root, text="Developed by Muhammad Mudassir Abrar Baig", font=("Segoe UI", 10), bg="#1C1F2E", fg="white", pady=10
        )
        footer.pack(side="bottom", fill="x")

        self.inventory = Inventory()
        self.undo_redo_mgr = UndoRedoManager()
        self.theme_manager = ThemeManager(self.root)
        self.report_generator = ReportGenerator(self.inventory)

        self.setup_gui()
        self.inventory.load_from_file()
        self.check_low_stock()
    def setup_gui(self):
        self.theme_manager.apply_theme()

        # Entry Form Frame
        form_frame = tk.Frame(self.root, bg="#1C1F2E")
        form_frame.pack(pady=10)

        label_font = ("Segoe UI", 11, "bold")
        entry_font = ("Segoe UI", 11)

        def make_label(text, row):
            tk.Label(form_frame, text=text, font=label_font, fg="white", bg="#1C1F2E").grid(row=row, column=0, sticky="e", padx=8, pady=8)

        def make_entry(row):
            entry = tk.Entry(form_frame, font=entry_font, bg="#F0F0F0", width=30)
            entry.grid(row=row, column=1, padx=8, pady=8)
            return entry

        make_label("ID", 0)
        self.id_entry = make_entry(0)

        make_label("Name", 1)
        self.name_entry = make_entry(1)

        make_label("Quantity", 2)
        self.quantity_entry = make_entry(2)

        make_label("Price", 3)
        self.price_entry = make_entry(3)

        make_label("Category", 4)
        self.category_entry = make_entry(4)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#2E3A59", padx=20, pady=30, relief="raised", borderwidth=6)
        btn_frame.pack(fill="x", padx=20, pady=10)

        # Configure custom button style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton",
                        font=("Segoe UI", 11, "bold"),
                        padding=12,
                        background="#E3B04B",
                        foreground="#2E3A59")
        style.map("TButton",
                background=[("active", "#FFD369")],
                foreground=[("active", "#1C1F2E")])

        def add_button(text, cmd, row, col):
            btn = ttk.Button(btn_frame, text=text, command=cmd, style="TButton")
            btn.grid(row=row, column=col, padx=12, pady=12, ipadx=10, ipady=5, sticky="nsew")

        # Allow grid columns to expand
        for col in range(5):
            btn_frame.grid_columnconfigure(col, weight=1)

        # First row of buttons
        add_button("Add Product", self.add_product, 0, 0)
        add_button("Export CSV", self.inventory.export_to_csv, 0, 1)
        add_button("View Inventory", self.view_inventory, 0, 2)
        add_button("Sort by Quantity", self.sort_quantity, 0, 3)
        add_button("Sort by Category", self.sort_category, 0, 4)

        # Second row of buttons
        add_button("Toggle Theme", self.toggle_theme, 1, 0)
        add_button("Undo", self.undo, 1, 1)
        add_button("Redo", self.redo, 1, 2)
        add_button("View Report", self.show_report, 1, 3)
        add_button("Update Product", self.update_product, 1, 4)


    def add_product(self):
        try:
            product = Product(
                self.id_entry.get(),
                self.name_entry.get(),
                int(self.quantity_entry.get()),
                float(self.price_entry.get()),
                self.category_entry.get()
            )
            self.undo_redo_mgr.save_state(self.inventory)
            self.inventory.add_product(product)
            self.inventory.save_to_file()
            messagebox.showinfo("Success", "Product added!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_product(self):
        prod_id = self.id_entry.get()
        name = self.name_entry.get()
        new_qty = self.quantity_entry.get()
        new_price = self.price_entry.get()

        updated = False
        for product in self.inventory.products:
            if product.product_id == prod_id and product.name.lower() == name.lower():
                self.undo_redo_mgr.save_state(self.inventory)
                if new_qty:
                    product.quantity = int(new_qty)
                if new_price:
                    product.price = float(new_price)
                updated = True
                break

        if updated:
            self.inventory.save_to_file()
            messagebox.showinfo("Updated", f"Product '{name}' updated successfully!")
        else:
            messagebox.showwarning("Not Found", "Product with this ID and Name not found.")

    def view_inventory(self):
        win = tk.Toplevel(self.root)
        win.title("Inventory List")
        win.geometry("1200x700")
        win.configure(bg="#1C1F2E")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"), background="#2E3A59", foreground="white")
        style.configure("Treeview", font=("Segoe UI", 11), background="#F0F0F0", rowheight=28)

        tree = ttk.Treeview(win, columns=("ID", "Name", "Qty", "Price", "Category"), show='headings')
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        for p in self.inventory.products:
            tree.insert('', 'end', values=(p.product_id, p.name, p.quantity, p.price, p.category))

        tree.pack(fill="both", expand=True, padx=10, pady=10)

    def sort_quantity(self):
        self.inventory.products = self.inventory.sort_by_quantity()
        self.view_inventory()

    def sort_category(self):
        self.inventory.products = self.inventory.sort_by_category()
        self.view_inventory()

    def check_low_stock(self, threshold=5):
        low = [p.name for p in self.inventory.products if p.quantity < threshold]
        if low:
            messagebox.showwarning("Low Stock", f"Low stock items: {', '.join(low)}")

    def toggle_theme(self):
        self.theme_manager.toggle_theme()

    def undo(self):
        self.undo_redo_mgr.undo(self.inventory)
        self.inventory.save_to_file()

    def redo(self):
        self.undo_redo_mgr.redo(self.inventory)
        self.inventory.save_to_file()

    def show_report(self):
        self.report_generator.show_report()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
