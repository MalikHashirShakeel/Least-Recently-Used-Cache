Here's a `README.md` file for your LRU Cache Command-Line Interface (CLI) application:

---

# **LRU Cache CLI**

Welcome to the **Least Recently Used (LRU) Cache CLI**! This application implements an interactive interface to manage and experiment with an LRU Cache. 

---

## **Features**

- **Initialize Cache**: Set the initial capacity of the cache.
- **Put Items**: Insert key-value pairs into the cache.
- **Get Items**: Retrieve values by key.
- **Show Cache Contents**: View all key-value pairs currently in the cache.
- **Miss Rate Calculation**: Get the current miss rate for cache accesses.
- **Resize Cache**: Adjust the cache capacity dynamically.
- **Exit**: Gracefully exit the CLI interface.

---

## **Requirements**

- Python 3.6 or higher
- `LRUCache` class from `LRUCache.py`
- A terminal or command-line environment to run the script.

---

## **How to Use**

### **1. Running the Application**

1. Clone or download the repository containing the CLI and `LRUCache` implementation.
2. Open a terminal in the project directory.
3. Run the application:
   ```bash
   python main.py
   ```

### **2. Commands Overview**

#### **Initialize Cache**
- When prompted, enter the desired capacity of the cache.
- Example:
  ```text
  Do you want to initialize the cache (y/n): y
  Enter the capacity of the cache: 3
  Cache initialized with capacity: 3
  ```

#### **Command Menu**
- After initialization, the following options are available:

| Command | Description                                         |
|---------|-----------------------------------------------------|
| `1`     | Add a key-value pair to the cache.                 |
| `2`     | Retrieve the value for a given key.                |
| `3`     | Display all key-value pairs currently in the cache.|
| `4`     | Calculate and display the cache miss rate.         |
| `5`     | Resize the cache to a new capacity.                |
| `6`     | Exit the application.                              |

#### **Examples**
- **Put Items**:
  ```text
  Enter the command number: 1
  Enter the key (integer) here: 1
  Enter the value here: apple
  ✅ Item pushed into cache successfully.
  ```
  
- **Get Items**:
  ```text
  Enter the command number: 2
  Enter the key (integer) to get its value: 1
  ✅ Value for key 1: apple
  ```
  
- **Show Cache**:
  ```text
  Enter the command number: 3
  Current Cache Contents:
    - Key: 1, Value: apple
  ```

- **Resize Cache**:
  ```text
  Enter the command number: 5
  Enter the new capacity for the cache: 2
  ✅ Cache resized to capacity: 2
  ```

---

## **Error Handling**
- **Invalid Input**: The application ensures robust handling of non-integer or invalid inputs.
- **Key Not Found**: Returns an appropriate message if the requested key does not exist.
- **Exceptions**: Any unexpected errors are logged with a descriptive message.

---

## **Notes**
- This CLI is an interactive way to test the functionality of the LRU Cache implementation.
- For advanced usage, import the `LRUCache` class directly into your Python scripts.

---

## **Acknowledgments**
Developed as a simple demonstration of **Data Structures** and their real-world applications, this project highlights the power of caching and its impact on performance optimization.