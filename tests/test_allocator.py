import pytest
from quickfit_ui.allocator import QuickFitAllocator

def test_add_free_blocks():
    allocator = QuickFitAllocator(sizes=[50, 100, 200])
    allocator.add_free_blocks(50, 5)
    assert len(allocator.size_specific_lists[50]) == 5

def test_allocate_block():
    allocator = QuickFitAllocator(sizes=[50, 100])
    allocator.add_free_blocks(50, 3)
    block = allocator.allocate(50)
    assert block is not None
    assert block["status"] == "allocated"
    assert len(allocator.size_specific_lists[50]) == 2

def test_allocate_nonexistent_size():
    allocator = QuickFitAllocator(sizes=[50, 100])
    block = allocator.allocate(200)  # Size not in the allocator
    assert block is None

def test_deallocate_block():
    allocator = QuickFitAllocator(sizes=[50, 100])
    block = {"size": 50, "status": "allocated"}
    allocator.deallocate(block)
    assert len(allocator.size_specific_lists[50]) == 1
    assert allocator.size_specific_lists[50][0]["status"] == "free"

def test_invalid_block_deallocation():
    allocator = QuickFitAllocator(sizes=[50, 100])
    block = {"size": 200, "status": "allocated"}  # Invalid size
    with pytest.raises(ValueError):
        allocator.deallocate(block)
