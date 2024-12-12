class QuickFitAllocator:
    def __init__(self, sizes):
        self.size_specific_lists = {size: [] for size in sizes}

    def add_free_blocks(self, size, count):
        if size in self.size_specific_lists:
            self.size_specific_lists[size].extend([{"size": size, "status": "free"} for _ in range(count)])
        else:
            raise ValueError(f"Size {size} not supported by allocator.")

    def allocate(self, size):
        if size in self.size_specific_lists and self.size_specific_lists[size]:
            block = self.size_specific_lists[size].pop(0)
            block["status"] = "allocated"
            return block
        else:
            return None  # No available blocks of the requested size

    def deallocate(self, block):
        size = block["size"]
        if size in self.size_specific_lists:
            block["status"] = "free"
            self.size_specific_lists[size].append(block)
        else:
            raise ValueError(f"Block of size {size} cannot be deallocated.")

    def get_status(self):
        return self.size_specific_lists
