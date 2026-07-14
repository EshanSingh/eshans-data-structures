import pytest
from .hash_set import HashSet


@pytest.fixture
def empty_set():
    """Provides a fresh, empty HashSet for each test."""
    return HashSet([])


def test_initialization_empty(empty_set):
    assert empty_set.is_empty()
    assert len(empty_set) == 0

def test_initialization_with_elements():
    hset = HashSet(["a", "b", "c"])
    assert len(hset) == 3
    assert "a" in hset
    assert "b" in hset
    assert "c" in hset

def test_initialization_with_duplicates():
    hset = HashSet(["a", "a", "b"])
    assert len(hset) == 2

def test_add(empty_set):
    empty_set.add("x")
    assert "x" in empty_set
    assert len(empty_set) == 1

def test_add_duplicate_does_not_grow(empty_set):
    empty_set.add("x")
    empty_set.add("x")
    assert len(empty_set) == 1

def test_remove(empty_set):
    empty_set.add("x")
    empty_set.remove("x")
    assert "x" not in empty_set
    assert len(empty_set) == 0

def test_remove_nonexistent_is_noop(empty_set):
    empty_set.add("x")
    empty_set.remove("ghost")
    assert len(empty_set) == 1

def test_discard_existing(empty_set):
    empty_set.add("x")
    empty_set.discard("x")
    assert "x" not in empty_set

def test_discard_nonexistent_does_not_raise(empty_set):
    empty_set.discard("ghost")
    assert empty_set.is_empty()

def test_contains_false_for_missing(empty_set):
    assert "ghost" not in empty_set

def test_is_empty(empty_set):
    assert empty_set.is_empty()
    empty_set.add("x")
    assert not empty_set.is_empty()

def test_len(empty_set):
    assert len(empty_set) == 0
    empty_set.add("a")
    empty_set.add("b")
    assert len(empty_set) == 2

def test_resizing_triggers_correctly(empty_set):
    assert empty_set.map.capacity == 10

    for i in range(6):
        empty_set.add(f"key{i}")
    assert empty_set.map.capacity == 10

    empty_set.add("key6")
    assert empty_set.map.capacity == 20
    assert len(empty_set) == 7

    for i in range(7):
        assert f"key{i}" in empty_set

def test_hash_collisions(empty_set, monkeypatch):
    monkeypatch.setattr(empty_set.map, "_hash", lambda key: 5)

    empty_set.add("a")
    empty_set.add("b")
    empty_set.add("c")

    assert len(empty_set) == 3
    assert "a" in empty_set
    assert "b" in empty_set
    assert "c" in empty_set

    empty_set.remove("b")
    assert "b" not in empty_set
    assert len(empty_set) == 2
