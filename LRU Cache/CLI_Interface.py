from LRUCache import LRUCache

def main():
    print("=== WELCOME TO LRU CACHE CLI ===\n")

#-------------------------------------------------------------------------------------------------------------------------

    while True:
        init = input("Do you want to initialize the cache (y/n): ").strip()

        if init.lower() == "y":
            capacity = input("Enter the capacity of the cache (max 50): ").strip()
            try:
                if not capacity.isdigit() or int(capacity) <= 0 or int(capacity) > 50:
                    raise ValueError("Capacity must be a positive integer less than or equal to 50.")
                capacity = int(capacity)
                cache = LRUCache(capacity)
                print(f"Cache initialized with capacity: {capacity}\n")
                break
            except ValueError as ve:
                print(f"⚠️ {ve}\n")
                continue
            except Exception as e:
                print("❌ An unknown error occurred while initializing the cache:", e)
                continue

        elif init.lower() == "n":
            print("Exiting Interface...")
            return
        
        else:
            print("⚠️ Please enter a valid choice (y/n).\n")
            continue

#-------------------------------------------------------------------------------------------------------------------------

    while True:
        print("\n--- LRU Cache CLI Interface ---")
        print("Available Commands:")
        print("(1) -> Put something into the Cache.")
        print("(2) -> Get something from the Cache.")
        print("(3) -> Show all the Cache items.")
        print("(4) -> Get the current miss rate.")
        print("(5) -> Resize Cache.")
        print("(6) -> Exit Interface.")
        
        command = input("Enter the command number: ").strip()

#-------------------------------------------------------------------------------------------------------------------------

        if command == "1":
            try:
                key = int(input("Enter the key (integer between 0 and 100): "))
                value = int(input("Enter the value (integer between 0 and 100): "))

                if key < 0 or key > 100 or value < 0 or value > 100:
                    raise ValueError("Key and Value must be between 0 and 100.")

                cache.put(key, value)
                print("✅ Item pushed into cache successfully.")
            except ValueError as ve:
                print(f"⚠️ {ve}")
            except Exception as e:
                print("❌ An unknown error occurred while putting the item into the cache:", e)

#------------------------------------------------------------------------------------------------------------------------

        elif command == "2":
            try:
                key = int(input("Enter the key (integer) to get its value: "))
                value = cache.get(key)
                if value != -1:
                    print(f"✅ Value for key {key}: {value}")
                else:
                    print(f"⚠️ Key {key} not found in cache.")
            except ValueError:
                print("⚠️ Please enter a valid integer for the key.")
            except Exception as e:
                print("❌ An unknown error occurred while getting the item from the cache:", e)

#------------------------------------------------------------------------------------------------------------------------

        elif command == "3":
            try:
                if len(cache._cache) == 0:
                    print("⚠️ The cache is empty.")
                else:
                    cache_contents = {k: v.value for k, v in cache._cache.items()}
                    print("Current Cache Contents:")
                    for k, v in cache_contents.items():
                        print(f"  - Key: {k}, Value: {v}")
            except Exception as e:
                print("❌ An unknown error occurred while showing the cache contents:", e)

#------------------------------------------------------------------------------------------------------------------------

        elif command == "4":
            try:
                miss_rate = cache.miss_rate()
                print(f"Current miss rate: {miss_rate * 100}%")
            except Exception as e:
                print("❌ An unknown error occurred while calculating the miss rate:", e)

#------------------------------------------------------------------------------------------------------------------------

        elif command == "5":
            try:
                new_capacity = input("Enter the new capacity for the cache (max 50): ").strip()
                if not new_capacity.isdigit() or int(new_capacity) <= 0 or int(new_capacity) > 50:
                    raise ValueError("Capacity must be a positive integer less than or equal to 50.")
                new_capacity = int(new_capacity)
                cache.resize(new_capacity)
                print(f"✅ Cache resized to capacity: {new_capacity}")
            except ValueError as ve:
                print(f"⚠️ {ve}")
            except Exception as e:
                print("❌ An unknown error occurred while resizing the cache:", e)

        elif command == "6":
            print("Exiting Interface. Goodbye!")
            break

        else:
            print("⚠️ Invalid command. Please enter a number between 1 and 6.\n")

#========================================================================================================================
