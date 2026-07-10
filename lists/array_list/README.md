# ArrayList

A clean, from-scratch Python implementation of an **ArrayList**.

## Interact

First navigate to this directory, then run

```bash
python playground.py
```

This will allow you to use `ArrayList` and visualize whats happening inside.
NOTE: All code related to playground was AI generated

## Overview

An ArrayList is a modfication of the traditional array that improves on its shortcomings. One of the shortcomings of arrays was that it is unable to dynamically resize. ArrayList solved that by creating a copy of the array and doubling it's size once it reaches max capacity ($O(n)$). This is a costly one-time cost that becomes ammortized to $O(1)$ since it does not occur very often. This single optimization allows for a much more streamlined developer appraoch, since there is no longer any need for manual array resizing.

---

## Complexity Analysis

| Operation           | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity (Worst) |
| :------------------ | :--------------------- | :------------------------ | :---------------------- | :----------------------- |
| **Insertion**       | $O(1)$                 | $O(n)$                    | $O(n)$                  | $O(n)$                   |
| **Deletion**        | $O(1)$                 | $O(n)$                    | $O(n)$                  | $O(1)$                   |
| **Lookup / Search** | $O(1)$                 | $O(n)$                    | $O(n)$                  | $O(1)$                   |
| **Access by Index** | $O(1)$                 | $O(1)$                    | $O(1)$                  | $O(1)$                   |

### Complexity Notes:

- **Append and Insert Operations:** Appending to the end of the array (Best Case) is $O(1)$ operation on average. However, if the operation fills the `capacity`, it triggers an $O(n)$ internal memory resize. Inserting at the beginning or middle requires an $O(n)$ shifting loop to make room for the new element.
- **Memory Buffer Overhead:** The space complexity of the array operations is $O(1)$ auxiliary space because modifications happen in-place. However, the total space footprint of the data structure itself takes up $O(\text{capacity})$ memory slots rather than $O(\text{size})$, meaning there is a small memory overhead dedicated to unused slots waiting for future elements.

---

## Key Methods

- `append(value)`: appends `value` to the end of the `ArrayList`
- `insert(value, index)`: inserts `value` at `index`, shifts elements at indexes >= `index` to the right
- `pop()`: removes last element from the `ArrayList`
- `remove_at(index)`: removes elemnt at `index` from `ArrayList`,
- `get(index)`: returns element at `index`
- `set(index, value)`: sets element at `index` to `value`

---

## Implementation Hurdles & Insights

_A running technical journal of edge cases encountered, logic bugs discovered, or pointer challenges solved during development._

- **Hurdle 1:** Python method overloading limitation in the constructor required a single initialization path using `starting_array=None` and evaluating via `starting_array is not None` to prevent empty initializations `[]` from incorrectly triggering the fallback `else` block.
- **Hurdle 2:** The shift-left logic in `remove_at` caused a native `IndexError` when the buffer was full because the boundary index extended past `size - 1`, attempting to reference a non-existent element outside the internal capacity.
- **Hurdle 3:** Index boundary validation rules must check for negative numbers and strict edge inequalities (`index >= self.size` instead of `index > self.size`) to prevent users from bypassing restrictions and corrupting or reading internal `None` slots within the private raw allocation.

---

## Future Optimizations / Bottlenecks

_Things I might explore later to make this implementation faster, cleaner, or more memory efficient._

- [ ] **Dynamic Shrinking:** Implement dynamic memory shrinking when array size drops below x% of overall capacity to reclaim memory buffer space and prevent memory leaks after major deletions.
- [ ] **Python Magic Methods:** Implement built-in Python methods like `__getitem__(self, index)` and `__setitem__(self, index, value)` so that standard index syntax (`my_list[0] = 5`) works natively instead of requiring manual `.get()` and `.set()` calls.
- [ ] **Iterable Support:** Implement an iterator `__iter__(self)` to allow the custom `ArrayList` to be traversed seamlessly using standard native `for element in my_list:` loops.
