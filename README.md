## hashtable.py

| Метод            | Опис                                               | Повертає |
|------------------|----------------------------------------------------|----------|
| `insert(key, v)` | Додає/оновлює пару `key-value`.                    | `True`   |
| `get(key)`       | Повертає значення за ключем або `None`, якщо немає | `Any`    |
| `delete(key)`    | **НОВОЕ.** Видаляє пару `key-value` з таблиці.     | `bool`   |

### Приклад використання `delete`

```python
from hashtable import HashTable

H = HashTable(5)
H.insert("apple", 10)
H.delete("apple")     # → True
assert H.get("apple") is None