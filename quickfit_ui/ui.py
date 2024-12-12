import tkinter as tk
from tkinter import messagebox
from quickfit_ui.allocator import QuickFitAllocator

class QuickFitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Fit Memory Allocator")
        self.allocator = QuickFitAllocator(sizes=[50, 100, 200, 400])

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Header
        tk.Label(self.root, text="Quick Fit Memory Allocator", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        # Add Free Blocks
        tk.Label(self.root, text="Add Free Blocks").grid(row=1, column=0, sticky="w")
        self.block_size_entry = tk.Entry(self.root)
        self.block_size_entry.grid(row=1, column=1)
        self.block_count_entry = tk.Entry(self.root)
        self.block_count_entry.grid(row=1, column=2)
        tk.Button(self.root, text="Add", command=self.add_blocks).grid(row=1, column=3, padx=10)

        # Allocate Memory
        tk.Label(self.root, text="Allocate Memory").grid(row=2, column=0, sticky="w")
        self.allocate_size_entry = tk.Entry(self.root)
        self.allocate_size_entry.grid(row=2, column=1)
        tk.Button(self.root, text="Allocate", command=self.allocate_memory).grid(row=2, column=3, padx=10)

        # Deallocate Memory
        tk.Label(self.root, text="Deallocate Memory").grid(row=3, column=0, sticky="w")
        self.deallocate_size_entry = tk.Entry(self.root)
        self.deallocate_size_entry.grid(row=3, column=1)
        tk.Button(self.root, text="Deallocate", command=self.deallocate_memory).grid(row=3, column=3, padx=10)

        # Status Display
        tk.Button(self.root, text="Show Status", command=self.show_status).grid(row=4, column=0, columnspan=4, pady=10)

        # Output Box
        self.output_box = tk.Text(self.root, width=60, height=10, state="disabled")
        self.output_box.grid(row=5, column=0, columnspan=4, pady=10)

    def add_blocks(self):
        try:
            size = int(self.block_size_entry.get())
            count = int(self.block_count_entry.get())
            self.allocator.add_free_blocks(size, count)
            self.show_message("Blocks added successfully.")
        except Exception as e:
            self.show_message(f"Error: {e}")

    def allocate_memory(self):
        try:
            size = int(self.allocate_size_entry.get())
            block = self.allocator.allocate(size)
            if block:
                self.show_message(f"Block allocated: {block}")
            else:
                self.show_message("No blocks available for allocation.")
        except Exception as e:
            self.show_message(f"Error: {e}")

    def deallocate_memory(self):
        try:
            size = int(self.deallocate_size_entry.get())
            block = {"size": size, "status": "allocated"}  # Simulated block
            self.allocator.deallocate(block)
            self.show_message("Block deallocated successfully.")
        except Exception as e:
            self.show_message(f"Error: {e}")

    def show_status(self):
        status = self.allocator.get_status()
        output = "\n".join([f"Size {size}: {len(blocks)} blocks available" for size, blocks in status.items()])
        self.show_message(output)

    def show_message(self, message):
        self.output_box.configure(state="normal")
        self.output_box.insert(tk.END, f"{message}\n")
        self.output_box.configure(state="disabled")
