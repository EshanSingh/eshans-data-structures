# AI WRITTEN

import sys
from linked_list import LinkedList  # Ensure your code is in linked_list.py

def visualize_list(my_list, title="Current State"):
    """
    Traverses the linked list node by node to print an ASCII map 
    of the internal node chain and sentinels.
    """
    print(f"\n📊 {title}:")
    
    # Start assembling the chain representation
    chain = ["[HEAD]"]
    
    # Traverse from the node right after head sentinel up to the tail sentinel
    cur = my_list.head.next
    while cur != my_list.tail and cur is not None:
        chain.append(f"[ {cur.val} ]")
        cur = cur.next
        
    chain.append("[TAIL]")
    
    # Join with bidirectional pointer arrows
    print("  <->  ".join(chain))
    print(f"🔢 Size: {my_list.size}")


def main():
    print("🚀 Welcome to the LinkedList Interactive Tester!")
    print("-" * 50)
    
    # 1. Initialize the LinkedList
    raw_input = input("Enter initial elements separated by commas (or press Enter for empty): ")
    
    if raw_input.strip() == "":
        my_list = LinkedList()
    else:
        items = [x.strip() for x in raw_input.split(',')]
        my_list = LinkedList(items)
    
    visualize_list(my_list, "Initial State")

    # 2. The Interactive Loop
    while True:
        print("\n" + "="*35)
        print("Available Functions:")
        print("1. append(value)")
        print("2. prepend(value)")
        print("3. insert(index, value)")
        print("4. pop()")
        print("5. pop_left()")
        print("6. remove(index)")
        print("7. get(index)")
        print("8. set(index, value)")
        print("9. EXIT")
        print("="*35)
        
        choice = input("Select a function (1-10): ").strip()
        
        try:
            if choice == '1':
                val = input("Enter value to append: ")
                my_list.append(val)
                visualize_list(my_list, f"Appended '{val}'")
            
            elif choice == '2':
                val = input("Enter value to prepend: ")
                my_list.prepend(val)
                visualize_list(my_list, f"Prepended '{val}'")
            
            elif choice == '3':
                idx = int(input("Enter index: "))
                val = input("Enter value: ")
                my_list.insert(idx, val)
                visualize_list(my_list, f"Inserted '{val}' at index {idx}")
                
            elif choice == '4':
                val = my_list.pop()
                visualize_list(my_list, f"Popped '{val}' from the end")
                
            elif choice == '5':
                val = my_list.pop_left()
                visualize_list(my_list, f"Popped '{val}' from the left")
                
            elif choice == '6':
                idx = int(input("Enter index to remove: "))
                val = my_list.remove(idx)
                visualize_list(my_list, f"Removed '{val}' at index {idx}")
                
            elif choice == '7':
                idx = int(input("Enter index to get: "))
                val = my_list.get(idx)
                print(f"\n--> Value at index {idx} is: [{val}]")
                
            elif choice == '8':
                idx = int(input("Enter index to set: "))
                val = input("Enter new value: ")
                my_list.set(idx, val)
                visualize_list(my_list, f"Set index {idx} to '{val}'")
                
            elif choice == '9' or choice.lower() == 'exit':
                print("\nExiting Interactive Tester. Happy coding! 🚀")
                sys.exit()
                
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 9.")

        # Catch testing edge cases so the interface loop doesn't crash
        except ValueError:
            print("\n❌ Error: Please enter a valid integer for the index.")
        except IndexError as e:
            print(f"\n❌ IndexError Caught: {e}")
        except Exception as e:
            print(f"\n❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()