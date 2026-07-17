import pytest
from .queue import Queue


@pytest.fixture
def empty_queue():
    """Provides a fresh, empty Queue for each test."""
    return Queue()


def test_initialization_empty(empty_queue):
    assert empty_queue.is_empty()
    assert len(empty_queue) == 0

def test_enqueue(empty_queue):
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    assert len(empty_queue) == 2
    assert not empty_queue.is_empty()

def test_dequeue_is_fifo(empty_queue):
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    empty_queue.enqueue(3)

    assert empty_queue.dequeue() == 1
    assert empty_queue.dequeue() == 2
    assert empty_queue.dequeue() == 3
    assert empty_queue.is_empty()

def test_dequeue_empty_raises(empty_queue):
    with pytest.raises(IndexError, match='dequeueing from empty queue'):
        empty_queue.dequeue()

def test_peek_does_not_remove(empty_queue):
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)

    assert empty_queue.peek() == 1
    assert len(empty_queue) == 2
    assert empty_queue.peek() == 1

def test_peek_empty_raises(empty_queue):
    with pytest.raises(IndexError, match='peeking from empty queue'):
        empty_queue.peek()

def test_len(empty_queue):
    assert len(empty_queue) == 0
    empty_queue.enqueue('a')
    empty_queue.enqueue('b')
    assert len(empty_queue) == 2

def test_is_empty(empty_queue):
    assert empty_queue.is_empty()
    empty_queue.enqueue(1)
    assert not empty_queue.is_empty()
    empty_queue.dequeue()
    assert empty_queue.is_empty()
