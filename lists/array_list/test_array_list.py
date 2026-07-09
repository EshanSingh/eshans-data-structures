import pytest
from array_list import ArrayList

def test_initialization_empty():
    """Verify that an empty ArrayList initializes with size 0."""
    custom_list = ArrayList()
    assert custom_list.size == 0
    assert custom_list.capacity == 1

def test_initialization_with_array():
    """Verify initialization with an existing array."""
    items = [10, 20, 30]
    custom_list = ArrayList(items)
    assert custom_list.size == 3
    assert custom_list.capacity == 3
    assert custom_list.get(0) == 10
    assert custom_list.get(2) == 30

def test_append_and_resize():
    """Verify appending items triggers internal resizing correctly."""
    custom_list = ArrayList()
    custom_list.append("A")
    custom_list.append("B") 
    custom_list.append("C") 
    
    assert custom_list.size == 3
    assert custom_list.get(0) == "A"
    assert custom_list.get(1) == "B"
    assert custom_list.get(2) == "C"

def test_insert_middle():
    """Verify shifting logic when inserting into the middle of the list."""
    custom_list = ArrayList([1, 2, 4])
    custom_list.insert(2, 3)
    
    assert custom_list.size == 4
    assert custom_list.get(2) == 3
    assert custom_list.get(3) == 4

def test_insert_bounds_error():
    """Verify that out-of-bounds insertions throw an IndexError."""
    custom_list = ArrayList([1, 2])
    with pytest.raises(IndexError):
        custom_list.insert(5, 99)
    with pytest.raises(IndexError):
        custom_list.insert(-1, 99)

def test_pop():
    """Verify elements are removed from the end and returned properly."""
    custom_list = ArrayList([10, 20])
    assert custom_list.pop() == 20
    assert custom_list.size == 1
    assert custom_list.pop() == 10
    assert custom_list.size == 0
    
    
    with pytest.raises(IndexError):
        custom_list.pop()

def test_remove_at():
    """Verify elements shift left on removal and bounds are enforced."""
    custom_list = ArrayList(["apple", "banana", "cherry"])
    custom_list.remove_at(1) 
    
    assert custom_list.size == 2
    assert custom_list.get(0) == "apple"
    assert custom_list.get(1) == "cherry"
    
    with pytest.raises(IndexError):
        custom_list.remove_at(5)

def test_get_and_set():
    """Verify basic mutation and retrieval rules."""
    custom_list = ArrayList([5, 10, 15])
    custom_list.set(1, 99)
    
    assert custom_list.get(1) == 99
    with pytest.raises(IndexError):
        custom_list.get(3)