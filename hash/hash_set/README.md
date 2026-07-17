# Hash Set

A clean, from-scratch Python implementation of a **HashSet**.

## Interact

First navigate to this directory, then run

```bash
python playground.py
```

This will let you `put`, `get`, and `remove` items and visualize whats happening inside each bucket.
NOTE: All code related to playground was AI generated

## Overview

A HashSet is fundamentally a HashMap/HashTable, without using the values. it has all the same time complexities, and solves the same problem of accesssing by element in $O(1)$ time. I decided to reuse my [`HashMap`](../hash_map/) class to do the majority of the under-the-hood logic, since I didn't want to reinvent the wheel.

---

## Complexity Analysis

| Operation        | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity (Aux) |
| :--------------- | :--------------------- | :------------------------ | :---------------------- | :--------------------- |
| **Put / Update** | $O(1)$                 | $O(1)$                    | $O(n)$                  | $O(1)$                 |
| **Remove**       | $O(1)$                 | $O(1)$                    | $O(n)$                  | $O(1)$                 |
| **Get / Lookup** | $O(1)$                 | $O(1)$                    | $O(n)$                  | $O(1)$                 |

### Complexity Notes:

- **The Worst Case Is a Single Chain:** every operation is $O(n)$ in the worst case, which happens when every item hashes into the same bucket. At that point the hash map is just a `LinkedList`. In the average case, with items spread across buckets and a load factor kept below `0.7`, each chain is short and constant-length, which is where the $O(1)$ average comes from.
- **Resizing is $O(n)$ but Amortized $O(1)$:** when the load factor hits `0.7`, `_resize` doubles the capacity and re-inserts every existing entry, which is an $O(n)$ pass. But because the map doubles (rather than growing by a fixed amount), a resize happens rarely enough that its cost spread across all the insertions leading up to it works out to $O(1)$ per `put` on average. This is the same concept as in an ArrayList.
- **Rehashing, Not Copying:** on resize the entries cannot simply be copied slot-for-slot, because a item's bucket is `hash(item) % capacity` and the capacity just changed. Every entry has to be re-hashed against the new capacity to land in its correct new bucket.
- **Auxiliary Space:** individual `add` / `get` / `remove` calls mutate a bucket in place and use $O(1)$ auxiliary space. The one exception is a resize, which briefly builds a new backing array and is $O(n)$. The map as a whole stores $n$ entries, so its total footprint is $O(n)$.

---

## Key Methods

- `add(item, value)`: inserts `item` or overwrites it if `item` already exists (uses [`HashMap`](../hash_map/)'s `put()` under the hood)
- `get(item)`: hashes to the correct bucket and returns the value stored under `item` (uses [`HashMap`](../hash_map/)'s `get()` under the hood)
- `remove(item)`: hashes to the correct bucket and removes the entry for `item` if present (uses [`HashMap`](../hash_map/)'s `remove()` under the hood)
- `discard(item)`:same as `remove()` but does not throw an error if key isnt found
- `is_empty()` checks if set is empty (uses [`HashMap`](../hash_map/)'s `is_empty()` under the hood)

---

## Implementation Hurdles & Insights

_A running technical journal of edge cases encountered, logic bugs discovered, or design decisions made during development._

- Not any hurdles here, since [`HashMap`](../hash_map/) handles the vast majority of the logic

_(These are written from the code's design decisions, swap in your own real notes wherever your experience differed.)_

---

## Future Optimizations / Bottlenecks

_Things I might explore later to make this implementation faster, cleaner, or more usable._

- [ ] Logic handled by [`HashMap`](../hash_map/), so most improvements would happen there
