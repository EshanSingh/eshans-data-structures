# Interactive CLI tester for the HashMap implementation.
# AI WRITTEN

import sys, os

# hash_map/  ->  hash/   (the folder that holds the `lists` package)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hash_map import HashMap, LOAD_CAPACITY

def coerce(raw):
    """Turn a raw input string into an int/float when it looks numeric.

    Typing `5` should store the int 5, not the string "5". put() and get() both
    call this, so as long as they coerce identically, round-trips stay consistent
    (a key put as int 5 is later found by typing 5 again).
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


def visualize(hmap, title="Current State"):
    """Print every bucket and the chain of key=value pairs inside it.

    The HashMap class has no visualize() of its own (unlike ArrayList), so we
    build one here. We walk each bucket LinkedList the exact same way
    HashMap._resize does: start at head.next, stop at tail, and read each
    node's .val (which is a HashNode holding .key and .val).
    """
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
            entries.append(f"{node.key!r}={node.val!r}")
            cur = cur.next
        chain = " -> ".join(entries) if entries else "·"   # · = empty bucket
        print(f"   [{i:>2}] {chain}")
    print("-" * 50)


def main():
    print("🚀 Welcome to the HashMap Interactive Tester!")
    print("-" * 50)

    hmap = HashMap()

    # Optional initial population as key=value pairs (a map needs pairs, not just
    # values, which is why this differs from the ArrayList playground's input).
    raw = input(
        "Enter initial pairs as key=value, separated by commas\n"
        "(e.g.  apple=5, banana=3 ) or press Enter for empty: "
    )
    if raw.strip():
        for pair in raw.split(','):
            if '=' not in pair:
                print(f"   ⚠️  Skipping '{pair.strip()}' (missing '=')")
                continue
            k, v = pair.split('=', 1)
            hmap.put(coerce(k), coerce(v))

    visualize(hmap, "Initial State")

    # The Interactive Loop
    while True:
        print("\n" + "=" * 30)
        print("Available Functions:")
        print("1. put(key, value)")
        print("2. get(key)")
        print("3. remove(key)")
        print("4. visualize()")
        print("5. stats (size / capacity / load)")
        print("6. EXIT")
        print("=" * 30)

        choice = input("Select a function (1-6): ").strip()

        try:
            if choice == '1':
                key = coerce(input("Enter key: "))
                val = coerce(input("Enter value: "))
                hmap.put(key, val)
                visualize(hmap, f"put({key!r}, {val!r})")

            elif choice == '2':
                key = coerce(input("Enter key to get: "))
                # get() reads node.val directly, so a missing key surfaces as an
                # AttributeError on None. We catch that to report "not found".
                try:
                    val = hmap.get(key)
                    print(f"\n--> {key!r} maps to: [{val!r}]")
                except AttributeError:
                    print(f"\n❌ Key {key!r} not found in the map.")

            elif choice == '3':
                key = coerce(input("Enter key to remove: "))
                hmap.remove(key)
                visualize(hmap, f"remove({key!r})")

            elif choice == '4':
                visualize(hmap, "Current State")

            elif choice == '5':
                load = hmap.size / hmap.capacity
                print(f"\n--> size={hmap.size}   capacity={hmap.capacity}   load={load:.2f}")
                print(f"    (a resize doubles capacity once load >= {LOAD_CAPACITY})")

            elif choice == '6' or choice.lower() == 'exit':
                print("\nExiting Interactive Tester. Happy hashing! 🚀")
                sys.exit()

            else:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")

        # Keep the loop alive even when a method raises during boundary testing.
        except Exception as e:
            print(f"\n❌ {type(e).__name__} Caught: {e}")


if __name__ == "__main__":
    main()