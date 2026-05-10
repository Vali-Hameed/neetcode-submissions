class MyHashSet:

    def __init__(self):
        self.hashset=[]
        

    def add(self, key: int) -> None:
        self.hashset.append([key])
        

    def remove(self, key: int) -> None:
        count=0
        if not self.contains(key):
            return 
        while count<len(self.hashset):
            
            if self.hashset[count][0]==key:
                
                del(self.hashset[count])
             
                count-=1
            count+=1
                
                
                
        

    def contains(self, key: int) -> bool:
        if not any(key in k for k in self.hashset):
            return False

        else:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)