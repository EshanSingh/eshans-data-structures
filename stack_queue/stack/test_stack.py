import pytest
from .stack import Stack


@pytest.fixture
def empty_stack():
    """Provides a fresh, empty Stack for each test."""
    return Stack()


def test_initialization_empty(empty_stack):
    assert empty_stack.is_empty()
    assert len(empty_stack) == 0

def test_push(empty_stack):
    empty_stack.push(1)
    empty_stack.push(2)
    assert len(empty_stack) == 2
    assert not empty_stack.is_empty()

def test_pop_is_lifo(empty_stack):
    empty_stack.push(1)
    empty_stack.push(2)
    empty_stack.push(3)

    assert empty_stack.pop() == 3
    assert empty_stack.pop() == 2
    assert empty_stack.pop() == 1
    assert empty_stack.is_empty()

def test_pop_empty_raises(empty_stack):
    with pytest.raises(IndexError, match='popping from empty stack'):
        empty_stack.pop()

def test_peek_does_not_remove(empty_stack):
    empty_stack.push(1)
    empty_stack.push(2)

    assert empty_stack.peek() == 2
    assert len(empty_stack) == 2
    assert empty_stack.peek() == 2

def test_peek_empty_raises(empty_stack):
    with pytest.raises(IndexError, match='peeking from empty stack'):
        empty_stack.peek()

def test_len(empty_stack):
    assert len(empty_stack) == 0
    empty_stack.push('a')
    empty_stack.push('b')
    assert len(empty_stack) == 2

def test_is_empty(empty_stack):
    assert empty_stack.is_empty()
    empty_stack.push(1)
    assert not empty_stack.is_empty()
    empty_stack.pop()
    assert empty_stack.is_empty()
