import sys
from typing import Any

#함수정의
class FixedStack:

    def __init__(self, capacity: int=256)->None:
        self.stk=[None]*capacity
        self.capacity=capacity
        self.ptr=0

    def push(self,value:Any)->None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr]=value
        self.ptr+=1

    def is_full(self) -> bool:
        return self.ptr >= self.capacity
    
    def pop(self)->Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr-=1
        return self.stk[self.ptr]
    
    def size(self)->int:
        return self.ptr
    
    def is_empty(self)->bool:
        return self.ptr == 0
    
    def top(self)->Any:
        if self.is_empty():
            return -1
        return self.stk[self.ptr-1]

#########################################################################

#함수호출
n = int(sys.stdin.readline().strip()) 

result=[]

stack = FixedStack(10000)

for i in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push":
        stack.push(int(command[1])) 

    elif command[0] == "pop":
        if stack.is_empty() == 0:   
            result.append(stack.pop())
        else:
            result.append(-1)

    elif command[0] == "size":
        result.append(stack.size())

    elif command[0] == "empty":
        result.append(1 if stack.is_empty() else 0)

    elif command[0] == "top":
        result.append(stack.top())

sys.stdout.write("\n".join(map(str, result)) + "\n")