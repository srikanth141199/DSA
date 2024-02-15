"""
insert(key,value)
get(key) -> value
delete(key)
"""
class HashTable:

    def __init__(self,size) -> None:
        self.size = size
        self.create_hash_table()

    def create_hash_table(self):
        self.hash_table = [[] for _ in range(self.size)]

    """
    Insert key and value pair into hash table, If key already exists update it's value
    """

    def insert(self, key, value):
        hash_val = hash(key) % self.size

        bucket = self.hash_table[hash_val]

        isFound = False
        idx = -1
        for i in range(len(bucket)):
            stored_key, stored_val = bucket[i]
            if stored_key == key:
                isFound = True
                idx = i
                break

        if isFound:
            self.hash_table[hash_val][idx] = (key,value)
        else:
            self.hash_table[hash_val].append((key,value))
        
    """
    Given a key return it's value else return error message
    """

    def get(self,key):
        hash_val = hash(key) % self.size

        bucket = self.hash_table[hash_val]

        for i in range(len(bucket)):
            stored_key, stored_val = bucket[i]
            if stored_key == key:
                return stored_key, stored_val
            
        return 'Not Found the key : '+ key
    
    """
    Takes key as input and delets it from hashTable, if not present gives error response
    """

    def delete(self,key):
        hash_val = hash(key) % self.size

        bucket = self.hash_table[hash_val]

        isFound = False
        idx = -1 #Index is idx

        for i in range(len(bucket)):
            stored_key, stored_val = bucket[i]

            if stored_key == key:
                isFound = True
                idx = i
                break
        
        if isFound:
            self.hash_table[hash_val].pop(idx)
        else:
            print('Entered key is not available in hashTable : '+ key)



if __name__ == "__main__":
    hash_table = HashTable(10)

    hash_table.insert('Sam',93)
    hash_table.insert('Srikanth',24)

    print(hash_table.get('Srikanth'))
    print(hash_table.get('Harry'))

    hash_table.insert('Harry',82)
    print(hash_table.get('Harry'))

    hash_table.delete('Deyam')

    hash_table.delete('Harry')
    print(hash_table.get('Harry'))