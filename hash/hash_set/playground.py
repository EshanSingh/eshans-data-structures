# Interactive CLI tester for the HashSet implementation.
# AI WRITTEN

import sys, os

sys.stdout.reconfigure(encoding="utf-8")

# hash_set/  ->  hash/  ->  Projects/  (the folder that holds the `hash` and `lists` packages)
_hash_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_projects_dir = os.path.dirname(_hash_dir)
sys.path.insert(0, _projects_dir)

# hash_set.py uses a relative import (`from ..hash_map.hash_map import ...`), so it
# must be imported through the `hash` package rather than as a standalone module.
from hash.hash_set.hash_set import HashSet


def coerce(raw):
    """Turn a raw input string into an int/float when it looks numeric.

    Typing `5` should store the int 5, not the string "5", so that a set
    populated with 5 is later found by typing 5 again.
    """
    raw = raw.strip()
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        return raw


def visualize(hset, title="Current State"):
    """Print every bucket and the chain of items inside it.

    A HashSet stores its items as HashNode(key, None) inside the underlying
    HashMap, so we walk each bucket LinkedList the same way the HashMap
    playground does, but only print the key since the value is unused.
    """
    hmap = hset.map
    load = hmap.size / hmap.capacity
    print(f"\n📊 {title}")
    print(f"   size={hmap.size}   capacity={hmap.capacity}   load={load:.2f}")
    print("-" * 50)
    for i in range(hmap.map.size):
        bucket = hmap.map.get(i)
        entries = []
        cur = bucket.head.next
        while cur != bucket.tail:
            node = cur.val  # HashNode(key, val)
            entries.append(f"{node.key!r}")
            cur = cur.next
        chain = " -> ".join(entries) if entries else "·"   # · = empty bucket
        print(f"   [{i:>2}] {chain}")
    print("-" * 50)


def main():
    print("🚀 Welcome to the HashSet Interactive Tester!")
    print("-" * 50)

    raw = input(
        "Enter initial items separated by commas\n"
        "(e.g.  apple, banana, 5 ) or press Enter for empty: "
    )
    initial = [coerce(item) for item in raw.split(',')] if raw.strip() else []
    hset = HashSet(initial)

    visualize(hset, "Initial State")

    # The Interactive Loop
    while True:
        print("\n" + "=" * 30)
        print("Available Functions:")
        print("1. add(item)")
        print("2. remove(item)")
        print("3. discard(item)")
        print("4. contains(item)")
        print("5. visualize()")
        print("6. stats (size / capacity / load / is_empty)")
        print("7. EXIT")
        print("=" * 30)

        choice = input("Select a function (1-7): ").strip()

        try:
            if choice == '1':
                item = coerce(input("Enter item to add: "))
                hset.add(item)
                visualize(hset, f"add({item!r})")

            elif choice == '2':
                item = coerce(input("Enter item to remove: "))
                hset.remove(item)
                visualize(hset, f"remove({item!r})")

            elif choice == '3':
                item = coerce(input("Enter item to discard: "))
                hset.discard(item)
                visualize(hset, f"discard({item!r})")

            elif choice == '4':
                item = coerce(input("Enter item to check: "))
                if item in hset:
                    print(f"\n--> {item!r} is in the set.")
                else:
                    print(f"\n--> {item!r} is NOT in the set.")

            elif choice == '5':
                visualize(hset, "Current State")

            elif choice == '6':
                load = hset.map.size / hset.map.capacity
                print(f"\n--> size={len(hset)}   capacity={hset.map.capacity}   load={load:.2f}")
                print(f"    is_empty={hset.is_empty()}")

            elif choice == '7' or choice.lower() == 'exit':
                print("\nExiting Interactive Tester. Happy hashing! 🚀")
                sys.exit()

            else:
                print("❌ Invalid choice. Please enter a number between 1 and 7.")

        # Keep the loop alive even when a method raises during boundary testing.
        except Exception as e:
            print(f"\n❌ {type(e).__name__} Caught: {e}")


if __name__ == "__main__":
    main()
