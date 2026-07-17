# Interactive CLI tester for the Queue implementation.
# AI WRITTEN

import sys, os

sys.stdout.reconfigure(encoding="utf-8")

# queue/  ->  stack_queue/  ->  Projects/  (the folder that holds the `lists` package)
_stack_queue_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_projects_dir = os.path.dirname(_stack_queue_dir)
sys.path.insert(0, _stack_queue_dir)
sys.path.insert(0, _projects_dir)

from queue.queue import Queue


def coerce(raw):
    """Turn a raw input string into an int/float when it looks numeric.

    Typing `5` should enqueue the int 5, not the string "5".
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


def visualize(queue, title="Current State"):
    """Print the queue from front to rear.

    enqueue() appends and dequeue() pops from the left, so the front of the
    queue is the head of the underlying LinkedList and the rear is the tail.
    """
    print(f"\n📊 {title}")
    print(f"   size={len(queue)}")
    print("-" * 50)
    if queue.is_empty():
        print("   (empty)")
    else:
        entries = []
        cur = queue.queue.head.next
        while cur != queue.queue.tail:
            entries.append(f"{cur.val!r}")
            cur = cur.next
        print(f"   FRONT -> {' -> '.join(entries)} -> REAR")
    print("-" * 50)


def main():
    print("🚀 Welcome to the Queue Interactive Tester!")
    print("-" * 50)

    queue = Queue()

    raw = input("Enter initial items separated by commas (front to rear), or press Enter for empty: ")
    if raw.strip():
        for item in raw.split(','):
            queue.enqueue(coerce(item))

    visualize(queue, "Initial State")

    while True:
        print("\n" + "=" * 30)
        print("Available Functions:")
        print("1. enqueue(item)")
        print("2. dequeue()")
        print("3. peek()")
        print("4. visualize()")
        print("5. stats (size / is_empty)")
        print("6. EXIT")
        print("=" * 30)

        choice = input("Select a function (1-6): ").strip()

        try:
            if choice == '1':
                item = coerce(input("Enter item to enqueue: "))
                queue.enqueue(item)
                visualize(queue, f"enqueue({item!r})")

            elif choice == '2':
                item = queue.dequeue()
                print(f"\n--> dequeued: {item!r}")
                visualize(queue, "dequeue()")

            elif choice == '3':
                print(f"\n--> peek: {queue.peek()!r}")

            elif choice == '4':
                visualize(queue, "Current State")

            elif choice == '5':
                print(f"\n--> size={len(queue)}   is_empty={queue.is_empty()}")

            elif choice == '6' or choice.lower() == 'exit':
                print("\nExiting Interactive Tester. Happy queueing! 🚀")
                sys.exit()

            else:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")

        # Keep the loop alive even when a method raises during boundary testing.
        except Exception as e:
            print(f"\n❌ {type(e).__name__} Caught: {e}")


if __name__ == "__main__":
    main()
