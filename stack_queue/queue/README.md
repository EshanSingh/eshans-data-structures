# Queue

A clean, from-scratch Python implementation of a **Queue**.

## Interact

First navigate to this directory, then run

```bash
python playground.py
```

This will let you `enqueue`, `dequeue`, and `peek` items and visualize whats happening inside.
NOTE: All code related to playground was AI generated

## Overview

A Queue is a datastructure with a specialized property: LIFO (Last-In, First-Out). This means that elements are removed in the order that they are most recently added.A Queue typically uses a linked list under the hood due to its fast $(O(1))$ removal and insertion from the head and tail. Because of that I decided to reuse my [`LinkedList`](../../lists/linked_list/) class to do the majority of the under-the-hood logic, since code reusability is a big concept in modern CS.

---

## Complexity Analysis

| Operation           | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity (Aux) |
| :------------------ | :--------------------- | :------------------------ | :---------------------- | :--------------------- |
| **Insertion**       | $O(1)$                 | $O(1)$                    | $O(1)$                  | $O(1)$                 |
| **Deletion**        | $O(1)$                 | $O(1)$                    | $O(1)$                  | $O(1)$                 |
| **Lookup / Search** | $O(1)$                 | $O(n)$                    | $O(n)$                  | $O(1)$                 |
| **Access by Index** | $O(1)$                 | $O(n)$                    | $O(n)$                  | $O(1)$                 |

### Complexity Notes:

- **Every Operation Is Constant Time, No Averaging Needed:** `enqueue` appends onto the tail of the underlying `LinkedList` and `dequeue`/`peek` read from the head, so none of them ever traverse the list. There's no best/average/worst split like a chained hash map has — every case is $O(1)$.
- **No Resizing:** unlike an `ArrayList`-backed structure, a linked list allocates one node per element instead of pre-sized capacity, so there's no load factor or `_resize` pass to amortize. Growing or shrinking the queue is just swapping a head or tail pointer.
- **Auxiliary Space:** `enqueue` and `dequeue` each allocate or free a single node and repoint the head or tail, which is $O(1)$ auxiliary space. The queue as a whole stores $n$ entries, so its total footprint is $O(n)$.

_NOTE:_ Although I included Lookup/Search and Access by Index, those are not supported by my implementation, and are the reflective complexities of the underlying LinkedList.

---

## Key Methods

- `enqueue(item)`: adds `item` to the rear of the queue (uses [`LinkedList`](../../lists/linked_list/)'s `append()` under the hood, since the rear of the queue is the tail of the list)
- `dequeue()`: removes and returns the item at the front of the queue; raises `IndexError` if the queue is empty (uses [`LinkedList`](../../lists/linked_list/)'s `pop_left()` under the hood, since the front of the queue is the head of the list)
- `peek()`: returns the item at the front of the queue without removing it; raises `IndexError` if the queue is empty (uses [`LinkedList`](../../lists/linked_list/)'s `get(0)` under the hood)
- `is_empty()`: checks if the queue has zero elements
- `__len__()`: returns the number of elements currently in the queue

---

## Implementation Hurdles & Insights

_A running technical journal of edge cases encountered, logic bugs discovered, or design decisions made during development._

- **Hurdle 1:** Keeping the front and rear on opposite ends. Unlike a `Stack`, where `push`/`pop`/`peek` all operate on the same end, a `Queue` needs `enqueue` on the tail and `dequeue`/`peek` on the head, since insertion and removal happen at different sides. Because `append` and `pop_left` map directly onto those ends, there was no ambiguity here the way there was with `Stack.peek()`.

_(These are written from the code's design decisions, swap in your own real notes wherever your experience differed.)_

---

## Future Optimizations / Bottlenecks

_Things I might explore later to make this implementation faster, cleaner, or more usable._

- [ ] Logic handled by [`LinkedList`](../../lists/linked_list/), so most improvements would happen there
