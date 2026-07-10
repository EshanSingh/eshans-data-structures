# Linked List

A clean, from-scratch Python implementation of a **LinkedList**.

## Interact

First navigate to this directory, then run

```bash
python playground.py
```

This will allow you to use `LinkedList` and visualize whats happening inside.
NOTE: All code related to playground was AI generated

## Overview

A LinkedList is a modfication of the traditional array that improves on its shortcomings. One of the shortcomings of arrays was that it is unable to insert and remove elements quickly. LinkedLists solved that by using pointers. Instead of having a fixed size or indexing, each node of the linked list remembers its neighbors, since its neighbors are not contiguous in memory, indexing does not work, however it allows for quick changes to be made to any nodes neighbors (as long as you have a reference to the node). This modification allows for quick $O(1)$ insertions and deletions. However this does fall flat once you realize that a reference to the node is needed, and lookup to find the index is $O(n)$. So the most practical use is to quickly append and prepend items to a linked list. since we always keep a head and tail reference, insertion and removal at the head and tail are always $O(1)$, making it a useful underlying datastructure for things like stacks and queues.

---

## Complexity Analysis

| Operation           | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity (Worst) |
| :------------------ | :--------------------- | :------------------------ | :---------------------- | :----------------------- |
| **Insertion**       | $O(1)$                 | $O(1)$ (with reference)   | $O(1)$ (with reference) | $O(1)$                   |
| **Deletion**        | $O(1)$                 | $O(1)$ (with reference)   | $O(1)$ (with reference) | $O(1)$                   |
| **Lookup / Search** | $O(1)$                 | $O(n)$                    | $O(n)$                  | $O(1)$                   |
| **Access by Index** | $O(1)$                 | $O(n)$                    | $O(n)$                  | $O(1)$                   |

### Complexity Notes:

- **Append and Insert Operations:** insertion and deletion are techincally $O(n)$ since gettting the reference in the first place is a lookup task ($O(n)$). I tried optimizing it as much as possible by iterating from the head or tail depending on whether the index is closer to the `head` or `tail` this is still $O(n/2)$ but slightly faster than pure $O(n)$.
- **Memory Buffer Overhead:** Structural mutations happen in-place by adjusting neigbor references and take $O(1)$ auxiliary space. There is always 2 dummy nodes (`head` and `tail`) accounted for, making structural changes simpler even if the collection size is zero.

---

## Key Methods

- `append(value)`: appends `value` to the end of the `LinkedList`
- `prepend(value)`: prepends value to the beginning of the `LinkedList` right after the head sentinel
- `insert(index, value)`: inserts value at `index`
- `pop()`: removes and returns the last data element from the end of the `LinkedList`
- `pop_left()`: removes and returns the first data element from the front of the `LinkedList`
- `remove(index)`: removes and returns the element at `index`
- `get(index)`: traverses to and returns the value located at `index`

---

## Implementation Hurdles & Insights

_A running technical journal of edge cases encountered, logic bugs discovered, or pointer challenges solved during development._

- **Hurdle 1:** In a doubly linked list, changes require updating 4 independent link references (two forward, two backward). Forgetting to reassign any pointers like self.tail.prev or self.head.next during causes broken sequences.
- **Hurdle 2:** I initially wrote the code without using Dummy Nodes, this made me have to consider far more edge cases, and made the code very messy. I decided to refactor the code midway in to instead use Dummy Nodes for a smoother developer expereince and more readable code.
- **Hurdle 3:** When constructing the list from an initial array parameter, linking the final element's forward .next property to the self.tail sentinel is insufficient; the tail's reciprocal .prev link must also explicitly point back to that final node to preserve backward-traversal consistency.

---

## Future Optimizations / Bottlenecks

_Things I might explore later to make this implementation faster, cleaner, or more memory efficient._

- [ ] **Python Magic Methods:** Implement built-in Python methods like `__getitem__(self, index)` and `__setitem__(self, index, value)` so that standard index syntax (`my_list[0] = 5`) works natively instead of requiring manual `.get()` and `.set()` calls.
- [ ] **Iterable Support:** Implement an iterator `__iter__(self)` to allow the custom `ArrayList` to be traversed seamlessly using standard native `for element in my_list:` loops.
