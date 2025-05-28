class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    # Delete method to remove a key-value pair
    def delete(self, key):
        """
        Видаляє пару key-value з таблиці.

        Returns
        -------
        bool
            True  — елемент було знайдено й видалено;
            False — такого ключа немає.
        """
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]

        for idx, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[idx]
                return True
        return False
    
if __name__ == "__main__":
    # Тестуємо нашу хеш-таблицю:
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)

    print(H.get("apple"))   # Виведе: 10
    print(H.get("orange"))  # Виведе: 20
    print(H.get("banana"))  # Виведе: 30

    assert H.get("orange") == 20
    assert H.delete("orange") is True
    assert H.get("orange") is None
    assert H.delete("orange") is False  # другого разу вже немає
    print("All tests passed.")

    print(H.get("apple"))   # Виведе: 10
    print(H.get("orange"))  # Виведе: None
    print(H.get("banana"))  # Виведе: 30