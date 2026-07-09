# AI WRITTEN

import sys
from array_list import ArrayList  # Ensure array_list.py is in the same folder

def main():
    print("🚀 Welcome to the ArrayList Interactive Tester!")
    print("-" * 50)
    
    # 1. Initialize the array
    raw_input = input("Enter initial elements separated by commas (or press Enter for empty): ")
    
    if raw_input.strip() == "":
        my_list = ArrayList()
    else:
        # Split by comma and strip extra spaces from each element
        items = [x.strip() for x in raw_input.split(',')]
        my_list = ArrayList(items)
    
    my_list.visualize("Initial State")

    # 2. The Interactive Loop
    while True:
        print("\n" + "="*30)
        print("Available Functions:")
        print("1. append(value)")
        print("2. insert(index, value)")
        print("3. pop()")
        print("4. remove_at(index)")
        print("5. get(index)")
        print("6. set(index, value)")
        print("7. visualize()")
        print("8. EXIT")
        print("="*30)
        
        choice = input("Select a function (1-8): ").strip()
        
        try:
            if choice == '1':
                val = input("Enter value to append: ")
                my_list.append(val)
                my_list.visualize(f"Appended '{val}'")
            
            elif choice == '2':
                idx = int(input("Enter index: "))
                val = input("Enter value: ")
                my_list.insert(idx, val)
                my_list.visualize(f"Inserted '{val}' at index {idx}")
                
            elif choice == '3':
                val = my_list.pop()
                my_list.visualize(f"Popped '{val}'")
                
            elif choice == '4':
                idx = int(input("Enter index to remove: "))
                my_list.remove_at(idx)
                my_list.visualize(f"Removed element at index {idx}")
                
            elif choice == '5':
                idx = int(input("Enter index to get: "))
                val = my_list.get(idx)
                print(f"\n--> Value at index {idx} is: [{val}]")
                
            elif choice == '6':
                idx = int(input("Enter index to set: "))
                val = input("Enter new value: ")
                my_list.set(idx, val)
                my_list.visualize(f"Set index {idx} to '{val}'")
                
            elif choice == '7':
                my_list.visualize("Current State")
                
            elif choice == '8' or choice.lower() == 'exit':
                print("\nExiting Interactive Tester. Happy coding! 🚀")
                sys.exit()
                
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 8.")

        # Catch intentional boundary testing so the loop doesn't crash
        except ValueError:
            print("\n❌ Error: Please enter a valid integer for the index.")
        except IndexError as e:
            print(f"\n❌ IndexError Caught: {e}")
        except Exception as e:
            print(f"\n❌ Unexpected Error: {e}")

if __name__ == "__main__":
    main()