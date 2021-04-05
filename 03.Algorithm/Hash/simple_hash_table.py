class SHT:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, table_size):
        self.ht = [0] * table_size #list(key value)
        self.table_size = len(self.ht)

    def get_address(self, key): #Division Method
        return key % self.table_size
        
    def get_address_df(self, key): #Digits Folding
        if type(key) != str:
            str_key = str(key)
        else : 
            str_key = key

        key_length = len(str_key)
        hash_value = 0

        for i in range(0, key_length):
            hash_value = (hash_value << 3) + ord(str_key[i])
            print(hash_value)
             
        return hash_value % self.table_size


    def set(self, key, value):
        address = self.get_address(key)
        node = self.Node(key, value)
        self.ht[address] = node

    def get(self, key):
        address = self.get_address(key)
        value = self.ht[address].value
        return value

    def print(self):
        for i in range(0, len(self.ht)):
            if (type(self.ht[i]) == SHT.Node):
                print( "(" + str(self.ht[i].key) + ":" + str(self.ht[i].value) + ")", end=", ")
            else : 
                print( self.ht[i], sep=":", end=", ")

        print("\b\b ")

    def destory(self):
        self.ht = None


sht = SHT(10)

