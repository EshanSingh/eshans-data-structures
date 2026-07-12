import pytest
from .hash_map import HashMap

@pytest.fixture
def empty_map():
    """Provides a fresh, empty HashMap for each test."""
    return HashMap(capacity=10)


def test_initialization(empty_map):
    assert empty_map.size == 0
    assert empty_map.capacity == 10
    assert empty_map._calculate_load() == 0.0

def test_put_and_get(empty_map):
    empty_map.put("name", "Eshan")
    empty_map.put("age", 25)
    
    assert empty_map.size == 2
    assert empty_map.get("name") == "Eshan"
    assert empty_map.get("age") == 25

def test_update_existing_key(empty_map):
    empty_map.put("role", "Developer")
    assert empty_map.get("role") == "Developer"
    empty_map.put("role", "Senior Developer")
    assert empty_map.size == 1 
    assert empty_map.get("role") == "Senior Developer"

def test_remove_key(empty_map):
    empty_map.put("city", "Boston")
    assert empty_map.size == 1
    
    empty_map.remove("city")
    assert empty_map.size == 0
    
    with pytest.raises(ValueError, match='value does not exist'):
        empty_map.get("city")



def test_get_nonexistent_key(empty_map):
    with pytest.raises(ValueError, match='value does not exist'):
        empty_map.get("ghost_key")

def test_remove_nonexistent_key(empty_map):
    empty_map.put("a", 1)
    
    empty_map.remove("b") 
    
    assert empty_map.size == 1 


def test_resizing_triggers_correctly(empty_map):
    assert empty_map.capacity == 10
    
    for i in range(6):
        empty_map.put(f"key{i}", i)
    assert empty_map.capacity == 10
    
    empty_map.put("key6", 6)
    
    assert empty_map.capacity == 20
    assert empty_map.size == 7
    
    for i in range(7):
        assert empty_map.get(f"key{i}") == i

def test_hash_collisions(empty_map, monkeypatch):

    monkeypatch.setattr(empty_map, "_hash", lambda key: 5)
    
    empty_map.put("key1", "val1")
    empty_map.put("key2", "val2")
    empty_map.put("key3", "val3")
    
    assert empty_map.size == 3
    assert empty_map.get("key1") == "val1"
    assert empty_map.get("key2") == "val2"
    assert empty_map.get("key3") == "val3"