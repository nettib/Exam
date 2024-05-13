1.
class Hello:
    def __init__(self):
        self.arr=[]
    def append(self,data):
        self.arr.append(data)
    def searching(self,target):
        c=0
        if target not in self.arr:
            return -1
        for i in range(0,len(self.arr)):
            if self.arr[i]==target:
                c=c+1
        return c

myqueue=Hello()
myqueue.append(5)
myqueue.append(7)
myqueue.append(2)
myqueue.append(7)
print(myqueue.searching(8))
2.
class Stack:
    def __init__(self):
        self.s1=[]
    def push(self,data):
        self.s1.append(data)
    def pop(self):
        if len(self.s1)!=0:
            return self.s1.pop()
        return -1
    def peek(self):
        if len(self.s1)!=0:
            return self.s1[len(self.s1)-1]
        return -1
    def isEmpty(self):
        if len(self.s1)==0:
            return True
myqueue=Stack()
myqueue.push(5)
myqueue.push(7)
myqueue.pop()
print(myqueue.peek())
print(myqueue.s1)
3.
class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,data):
        self.s1.append(data)
    def dequeue(self):
        if len(self.s1)==0 and len(self.s2)==0:
            return -1
        elif len(self.s2)==0 and len(self.s1)>0:
            while len(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()
    def peek(self):
        if len(self.s1)==0 and len(self.s2)==0:
            return -1
        elif len(self.s2)==0 and len(self.s1)>0:
            while len(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2[0]
        else:
            return self.s2[0]


q=Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(7)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())
print(q.peek())
4.
def bubblesort(word):
    A=1
    C=2
    I=3
    S=4
    for i in word:
        if i is "A":
            i=1
        elif i is "C":
            i=2
        elif i is "I":
            i=3
        else:
            i=4
        for j in range(len(word);)
5.
def merge(s1,s2,s):
    i=j=0
    while i+j<len(s):
        if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
            s[i+j]=s1[i]
            i=i+1
        else:
            s[i+j]=s2[j]
            j+=1
def mergesort(s):
    n=len(s)
    if n<2:
        return
    m= n//2
    s1=[0:m]
    s2=[m:n]
    mergesort(s1)
    mergesort(s2)
merge(s1,s2,s)
6.
l1=[3,7,1,9,4]
def delete_element(arr,index):
    if index < 0 or index >= len(arr):
        return "Invalid Index", l1
    else:
        arr.remove(arr[index])
        return arr

print(delete_element(l1,-1))




