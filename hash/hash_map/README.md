# Hash Map

A clean, from-scratch Python implementation of a **HashMap**.

## Interact

First navigate to this directory, then run

```bash
python playground.py
```

This will let you `put`, `get`, and `remove` keys and visualize whats happening inside each bucket.
NOTE: All code related to playground was AI generated

## Overview

A HashMap is a modification of the traditional array that fixes a with $O(1)$ access, without needing to know the exact numeric index. Unlike arrays and linked lists, where if you want to look something up by an arbitrary key (a word, a name, an id) instead of a position, you must scan the whole array until you find it, which is $O(n)$. A HashMap solves this by putting a **hash function** in front of the array. The hash function deterministically turns any key into a number, and after taking that number `% capacity` we get a slot to jump straight to. So "look up by key" collapses into "compute a number, index into the array" which is $O(1)$ on average.

The complication is **collisions**: two different keys can hash to the same slot. This implementation handles that with **separate chaining**, where every slot (a "bucket") holds a `LinkedList`, and any keys that land on the same slot just get appended to that bucket's list. A lookup then means "hash to the right bucket, then walk its short list." As long as the lists stay short, that walk is effectively constant time. Notably this means the HashMap is built directly on top of an `ArrayList` of buckets, each bucket a `LinkedList` of entries.

The **load factor** ($\text{size} / \text{capacity}$) ensures the hashmaps buckets never get too long. Once it crosses `0.7`, the map doubles its capacity and rehashes every entry into the larger array. This trades a rare, expensive $O(n)$ resize for keeping the operations $O(1)$ on average.

---

## Complexity Analysis

| Operation        | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity (Aux) |
| :--------------- | :--------------------- | :------------------------ | :---------------------- | :--------------------- |
| **Put / Update** | $O(1)$                 | $O(1)$                    | $O(n)$                  | $O(1)$                 |
| **Remove**       | $O(1)$                 | $O(1)$                    | $O(n)$                  | $O(1)$                 |
| **Get / Lookup** | $O(1)$                 | $O(1)$                    | $O(n)$                  | $O(1)$                 |

### Complexity Notes:

- **The Worst Case Is a Single Chain:** every operation is $O(n)$ in the worst case, which happens when every key hashes into the same bucket. At that point the hash map is just a `LinkedList`. In the average case, with keys spread across buckets and a load factor kept below `0.7`, each chain is short and constant-length, which is where the $O(1)$ average comes from.
- **Resizing is $O(n)$ but Amortized $O(1)$:** when the load factor hits `0.7`, `_resize` doubles the capacity and re-inserts every existing entry, which is an $O(n)$ pass. But because the map doubles (rather than growing by a fixed amount), a resize happens rarely enough that its cost spread across all the insertions leading up to it works out to $O(1)$ per `put` on average. This is the same concept as in an ArrayList.
- **Rehashing, Not Copying:** on resize the entries cannot simply be copied slot-for-slot, because a key's bucket is `hash(key) % capacity` and the capacity just changed. Every entry has to be re-hashed against the new capacity to land in its correct new bucket.
- **Auxiliary Space:** individual `put` / `get` / `remove` calls mutate a bucket in place and use $O(1)$ auxiliary space. The one exception is a resize, which briefly builds a new backing array and is $O(n)$. The map as a whole stores $n$ entries, so its total footprint is $O(n)$.

---

## Key Methods

- `put(key, value)`: inserts `key` with `value`, or overwrites the value if `key` already exists
- `get(key)`: hashes to the correct bucket and returns the value stored under `key`
- `remove(key)`: hashes to the correct bucket and removes the entry for `key` if present
- `is_empty()`: checks if map is empty

Internal helpers:

- `_hash(key)`: wraps Python's built-in `hash()` in `abs()` to guarantee a non-negative number before the modulo
- `_resize()`: doubles capacity and rehashes every entry into the new backing array
- `_calculate_load()`: returns the current load factor ($\text{size} / \text{capacity}$)

---

## Implementation Hurdles & Insights

_A running technical journal of edge cases encountered, logic bugs discovered, or design decisions made during development._

- **Hurdle 1:** Comparing entries by key alone. Each entry is wrapped in a `HashNode`, and I overrode `__eq__` so two `HashNode`s are considered equal when their **keys** match, ignoring value. This is what lets me reuse the `LinkedList`'s `remove_val` and `get_by_val`: I build a throwaway probe node `HashNode(key, None)` and hand it to the list, and equality matches on the key even though I never knew the stored value.
- **Hurdle 2:** Making `put` handle inserts and updates in one path. Rather than branching on "does this key already exist," `put` always calls `remove_val` first and then `append`s the fresh entry. The return of `remove_val` tells me whether something was actually there, so I only bump `size` when the key was genuinely new. This keeps updates from silently inflating the size and breaking the load factor math.
- **Hurdle 3:** Negative hashes. Python's built-in `hash()` can return negative numbers, so I wrap it in `abs()` before the modulo to keep bucket indices clean and non-negative. (Python's `%` is already non-negative for a positive divisor, but the `abs()` makes the intent obvious and removes any doubt.)
- **Hurdle 4:** Remembering to rehash on resize. My first instinct on growing the map was to move the buckets over as-is, but a bucket index is meaningless once `capacity` changes. Every entry has to be recomputed with `hash(key) % new_capacity`, or lookups silently start missing keys that are still physically in the map.

_(These are written from the code's design decisions, swap in your own real notes wherever your experience differed.)_

---

## Future Optimizations / Bottlenecks

_Things I might explore later to make this implementation faster, cleaner, or more usable._

- [ ] **Membership Testing:** implement `__contains__(self, key)` so `key in my_map` works, and make `get` on a missing key raise a clean `KeyError` (or return a default) instead of surfacing an `AttributeError` on `None`.
- [ ] **Iterable Support:** add `keys()`, `values()`, `items()`, and an `__iter__` so the map can be traversed with a standard `for key in my_map:` loop.
- [ ] **Shrink on Removal:** the map currently only ever grows. Halving capacity when the load factor drops low enough would reclaim memory after lots of deletions.
- [ ] **Open Addressing:** experiment with a chaining-free collision strategy (linear or quadratic probing) to compare cache behavior and memory overhead against the current separate-chaining approach.
