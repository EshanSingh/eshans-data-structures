# Interactive CLI tester for the Stack implementation.
# AI WRITTEN

import sys, os

sys.stdout.reconfigure(encoding="utf-8")

# stack/  ->  stack_queue/  ->  Projects/  (the folder that holds the `lists` package)
_stack_queue_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_projects_dir = os.path.dirname(_stack_queue_dir)
sys.path.insert(0, _stack_queue_dir)
sys.path.insert(0, _projects_dir)

from stack.stack import Stack


def coerce(raw):
    """Turn a raw input string into an int/float when it looks numeric.

    Typing `5` should push the int 5, not the string "5".
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


def visualize(stack, title="Current State"):
    """Print the stack from top to bottom.

    push() prepends and pop() pops from the left, so the top of the stack is
    the head of the underlying LinkedList.
    """
    print(f"\n📊 {title}")
    print(f"   size={len(stack)}")
    print("-" * 50)
    if stack.is_empty():
        print("   (empty)")
    else:
        cur = stack.stack.head.next
        idx = 0
        while cur != stack.stack.tail:
            label = "TOP -> " if idx == 0 else "        "
            print(f"   {label}{cur.val!r}")
            cur = cur.next
            idx += 1
    print("-" * 50)


def main():
    print("🚀 Welcome to the Stack Interactive Tester!")
    print("-" * 50)

    stack = Stack()

    raw = input("Enter initial items separated by commas (bottom to top), or press Enter for empty: ")
    if raw.strip():
        for item in raw.split(','):
            stack.push(coerce(item))

    visualize(stack, "Initial State")

    while True:
        print("\n" + "=" * 30)
        print("Available Functions:")
        print("1. push(item)")
        print("2. pop()")
        print("3. peek()")
        print("4. visualize()")
        print("5. stats (size / is_empty)")
        print("6. EXIT")
        print("=" * 30)

        choice = input("Select a function (1-6): ").strip()

        try:
            if choice == '1':
                item = coerce(input("Enter item to push: "))
                stack.push(item)
                visualize(stack, f"push({item!r})")

            elif choice == '2':
                item = stack.pop()
                print(f"\n--> popped: {item!r}")
                visualize(stack, "pop()")

            elif choice == '3':
                print(f"\n--> peek: {stack.peek()!r}")

            elif choice == '4':
                visualize(stack, "Current State")

            elif choice == '5':
                print(f"\n--> size={len(stack)}   is_empty={stack.is_empty()}")

            elif choice == '6' or choice.lower() == 'exit':
                print("\nExiting Interactive Tester. Happy stacking! 🚀")
                sys.exit()

            else:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")

        # Keep the loop alive even when a method raises during boundary testing.
        except Exception as e:
            print(f"\n❌ {type(e).__name__} Caught: {e}")


if __name__ == "__main__":
    main()
