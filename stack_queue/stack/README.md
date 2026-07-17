# Stack

A clean, from-scratch Python implementation of a **Stack**.

## Interact

First navigate to this directory, then run

```bash
python playground.py
```

This will let you `push`, `pop`, and `peek` items and visualize whats happening inside.
NOTE: All code related to playground was AI generated

## Overview

A Stack is a datastructure with a specialized property: FIFO (First-In, First-Out). This means that elements are removed in the order that they are most recently added.A Stack typically uses a linked list under the hood due to its fast $(O(1))$ insertion and deletion from the head. Because of that I decided to reuse my [`LinkedList`](../../lists/linked_list/) class to do the majority of the under-the-hood logic, since code reusability is a big concept in modern CS.

---

## Complexity Analysis

| Operation           | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity (Aux) |
| :------------------ | :--------------------- | :------------------------ | :---------------------- | :--------------------- |
| **Insertion**       | $O(1)$                 | $O(1)$                    | $O(1)$                  | $O(1)$                 |
| **Deletion**        | $O(1)$                 | $O(1)$                    | $O(1)$                  | $O(1)$                 |
| **Lookup / Search** | $O(1)$                 | $O(n)$                    | $O(n)$                  | $O(1)$                 |
| **Access by Index** | $O(1)$                 | $O(n)$                    | $O(n)$                  | $O(1)$                 |

### Complexity Notes:

- **Every Operation Is Constant Time, No Averaging Needed:** `push` prepends onto the head of the underlying `LinkedList` and `pop`/`peek` read from that same head, so none of them ever traverse the list. There's no best/average/worst split like a chained hash map has — every case is $O(1)$.
- **No Resizing:** unlike an `ArrayList`-backed structure, a linked list allocates one node per element instead of pre-sized capacity, so there's no load factor or `_resize` pass to amortize. Growing or shrinking the stack is just swapping a node pointer.
- **Auxiliary Space:** `push` and `pop` each allocate or free a single node and repoint the head, which is $O(1)$ auxiliary space. The stack as a whole stores $n$ entries, so its total footprint is $O(n)$.

_NOTE:_ Although I included Lookup/Search and Access by Index, those are not supported by my implementation, and are the reflective complexities of the underlying LinkedList.

---

## Key Methods

- `push(item)`: adds `item` to the top of the stack (uses [`LinkedList`](../../lists/linked_list/)'s `prepend()` under the hood, since the top of the stack is the head of the list)
- `pop()`: removes and returns the item at the top of the stack; raises `IndexError` if the stack is empty (uses [`LinkedList`](../../lists/linked_list/)'s `pop_left()` under the hood)
- `peek()`: returns the item at the top of the stack without removing it; raises `IndexError` if the stack is empty (uses [`LinkedList`](../../lists/linked_list/)'s `get(0)` under the hood)
- `is_empty()`: checks if the stack has zero elements
- `__len__()`: returns the number of elements currently in the stack

---

## Implementation Hurdles & Insights

_A running technical journal of edge cases encountered, logic bugs discovered, or design decisions made during development._

- **Hurdle 1:** Keeping `peek` consistent with `push`/`pop`. `push` adds to the **head** (`prepend`) and `pop` removes from the **head** (`pop_left`), so `peek` has to read the same end. My first version of `peek` read `get(size-1)` (the tail) instead of `get(0)` (the head) — it ran without error, but silently returned the bottom of the stack instead of the top whenever the stack held more than one item.

_(These are written from the code's design decisions, swap in your own real notes wherever your experience differed.)_

---

## Future Optimizations / Bottlenecks

_Things I might explore later to make this implementation faster, cleaner, or more usable._

- [ ] Logic handled by [`LinkedList`](../../lists/linked_list/), so most improvements would happen there
