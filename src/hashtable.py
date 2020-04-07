# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        #step1:
        #make a function to map the "insert method" to the array "capacity".
        #take the key value, turn it into a string, then for each character in the string,
        #return the unicode value of it. use that unicode number to make an equation.
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for character in str(key):
            hash = (hash * 33) + ord(character)
        return hash

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        #get function
        hash_func = self._hash_mod(key)
        #case1: look for key
        if not self.retrieve(key):
            self.remove(key)
        #case2 if empty, use linked_list to insert (key, value)
        if self.storage[hash_func] == None:
            self.storage[hash_func] = LinkedPair(key,value)
        #case3 if collsion, then use a node pointer to point to first index, then insert at Null, then make a pointer point at null
        # headA -Next> , B -next> C -Next> Null
        #nodeA -nodeA.next> Null
        else:
            node=self.storage[hash_func]
            while node.next: #iterator until node.next is null, then assign to node.
                node=node.next
            node.next=LinkedPair(key,value) #insert at




    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        #nodeA-next> nodeB -next> null
        hash_func = self._hash_mod(key)
        #if empty, return Empty
        if self.storage[hash_func]:
            return print('Empty')
        else:
            node=self.storage[hash_func] #how do we get node?
            previous_node = None #use this variable to assign node.next
            #iterator to look for key
            #case1: find key in middle or end of LL, set previous node to next
            #case2: if key is at first, remove node
            while node:
                if node.key == key:
                    if previous_node:
                        previous_node.next = node.next
                    else:
                        self.storage[hash_func]
                previous_node = node
                node = node.next




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        #use the hash_func to go striaght to index
        hash_function = self._hash_mod(key)
        #case1: if storage[index] is empty, then return.
        #case2: iterator thought node until we find. then retrieve
        if self.storage[hash_function]==None:
            return None
        else:
            node=self.storage[hash_function]
            while node:
                if node.key==key:
                    return node.value #return value if fond
                node=node.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        #copy capacity into a new temp variable
        #then recopy the key value back to the double size array
        temp = []
        for thisNode in self.storage:
            if not thisNode == None:
                node=thisNode
                while node:
                    temp.append((node.key, node.value))
                    node=node.next
        #make new storage
        self.storage = [None] * (self.capacity*2)
        for keyValue in temp:
            self.insert(keyValue[0],keyValue[1])


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
