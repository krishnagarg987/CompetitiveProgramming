class mapnode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class dict:
    def __init__(self):
        self.bucketsize=10
        self.bucket=[None for i in range(self.bucketsize)]
        self.count=0

    def hashkeytoindex(self,hashedValue):
        return abs(hashedValue)%(self.bucketsize)

    def insert(self,key,value):
        hashedValue=hash(key)
        index=self.hashkeytoindex(hashedValue)
        data=self.bucket[index]
        while data is not None:
            if data.key==key:
                data.value=value
                return
            data=data.next
        data=self.bucket[index]
        node=mapnode(key,value)
        node.next=data
        self.bucket[index]=node
        self.count+=1
        loadFactor=self.count/self.bucketsize
        if loadFactor>=0.7:
            self.rehash()

    def getValue(self,key):
        hashedValue=hash(key)
        index=self.hashkeytoindex(hashedValue)
        data=self.bucket[index]
        while data is not None:
            if data.key==key:
                return data.value
            data=data.next
        return None

    def delete(self,key):
        hashedValue=hash(key)
        index=self.hashkeytoindex(hashedValue)
        data=self.bucket[index]
        prev=None
        while data is not None:
            if data.key==key:
                if prev==None:
                    self.bucket[index]=data.next
                    self.count-=1
                    return data.value
                prev.next=data.next
                self.count-=1
                return data.value
            prev=data
            data=data.next
        return False

    def rehash(self):
        temp=self.bucket
        self.bucket=[None for i in range(2*self.bucketsize)]
        self.bucketsize=2*self.bucketsize
        self.count=0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head=head.next

d=dict()
d.insert(5,25)
print(d.count)
d.insert(15,225)
print(d.count)
d.delete(5)
print(d.count)
print(d.delete(15))
print(d.count)





