import pytest
from linked_list import LinkedList 

def test_initialization_empty():
    """Ensure an empty list initializes with correct defaults."""
    ll = LinkedList()
    assert ll.is_empty()
    assert ll.size == 0

def test_initialization_with_array():
    """Ensure parsing an array links elements and hooks up the tail.prev correctly."""
    ll = LinkedList([10, 20, 30])
    assert not ll.is_empty()
    assert ll.size == 3
    assert ll.get(0) == 10
    assert ll.get(1) == 20
    assert ll.get(2) == 30
    
    assert ll.pop() == 30 

def test_append():
    """Test adding elements sequentially to the end."""
    ll = LinkedList()
    ll.append("A")
    ll.append("B")
    assert ll.size == 2
    assert ll.get(0) == "A"
    assert ll.get(1) == "B"

def test_prepend():
    """Test adding elements sequentially to the front."""
    ll = LinkedList()
    ll.prepend("A")
    ll.prepend("B") 
    assert ll.size == 2
    assert ll.get(0) == "B"
    assert ll.get(1) == "A"

def test_insert():
    """Test arbitrary insertion at front, middle, and back boundaries."""
    ll = LinkedList([1, 2, 3])
    
    # Insert in the middle
    ll.insert(1, 99) 
    assert ll.get(1) == 99
    assert ll.get(2) == 2
    assert ll.size == 4

    # Insert at front
    ll.insert(0, 100)
    assert ll.get(0) == 100
    assert ll.get(1) == 1

    # Insert at end
    ll.insert(ll.size, 200)
    assert ll.get(ll.size - 1) == 200

def test_pop():
    """Test removing elements from the end and confirming value returns."""
    ll = LinkedList([10, 20, 30])
    assert ll.pop() == 30
    assert ll.size == 2
    assert ll.get(1) == 20

def test_pop_left():
    """Test removing elements from the front."""
    ll = LinkedList([10, 20, 30])
    assert ll.pop_left() == 10
    assert ll.size == 2
    assert ll.get(0) == 20

def test_remove():
    """Test removing from arbitrary indexes."""
    ll = LinkedList(["A", "B", "C", "D"])
    
    # Remove from the middle
    assert ll.remove(1) == "B" 
    assert ll.size == 3
    assert ll.get(1) == "C"

    # Remove from index 0
    assert ll.remove(0) == "A"

    # Remove from index size-1
    assert ll.remove(ll.size - 1) == "D"

def test_set():
    """Test overwriting existing values."""
    ll = LinkedList([1, 2, 3])
    ll.set(1, 99)
    assert ll.get(1) == 99
    assert ll.size == 3

def test_index_out_of_bounds_errors():
    """Ensure out-of-bounds attempts throw explicit IndexErrors."""
    ll = LinkedList([10, 20])

    # Test get boundaries
    with pytest.raises(IndexError):
        ll.get(2)
    with pytest.raises(IndexError):
        ll.get(-1)

    # Test set boundaries
    with pytest.raises(IndexError):
        ll.set(2, 99)

    # Test remove boundaries
    with pytest.raises(IndexError):
        ll.remove(2)

    # Test insert boundaries
    with pytest.raises(IndexError):
        ll.insert(3, 99)

def test_empty_list_deletion_errors():
    """Ensure popping from a completely empty list safely catches errors."""
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.pop()
    with pytest.raises(IndexError):
        ll.pop_left()


