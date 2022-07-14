class Node:
    def __init__(self,key,val):
        self.key, self.val, self.next, self.prev = key, val, None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.d ={}
        self.l, self.r = Node(0,0), Node(0,0)
        self.cap = capacity
        self.l.next, self.r.prev = self.r, self.l
    
    def insert(self, node):
        pre = self.r.prev
        pre.next, node.prev = node, pre
        node.next, self.r.prev = self.r, node
    
    def printl(self):
        temp = self.l
        while temp:
            print(temp.key,temp.val)
            temp =temp.next
        
    def delete(self, node):
        pre, nxt = node.prev, node.next
        pre.next ,nxt.prev = nxt, pre
        
        
    def get(self, key: int) -> int:
        # self.printl()
        # print("")
        if key in self.d:
            self.delete(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        # self.printl()
        # print("")
        if key in self.d:
            self.delete(self.d[key])
            self.insert(self.d[key])
            self.d[key].val = value
        else:
            newnode = Node(key,value)
            self.d[key] = newnode
            if  len(self.d) <= self.cap:
                self.insert(newnode)
            else:
                del self.d[self.l.next.key]
                self.delete(self.l.next)
                self.insert(newnode)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)