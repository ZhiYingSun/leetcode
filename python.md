### Strings
F-Strings are more efficent - but when I am using it, remember to explain to interviewer a bit (or ask if they are familiar with it)

- `print(f"The band for {name} is {band} out of 10")`


### Set
Implemented internally like a dictionary (with a hash table)
- `x in s` - O(1)
- `s.add()` - O(1)
- `s.remove()` - O(1)

### List
- `l.append()` - O(1)
- `l.pop(2)` - O(n) (O(1) if from the end)
- `l.insert(1, "orange")` - O(n)
- Get Item/Set Item - O(1)

### Heap
 
        heap = []       # Creating empty heap
        heapify(heap)   # transforms list into a heap, in-place, in linear time
        
        for num in nums:
            heappush(heap, num)  # push element O(Logk)
            if len(heap) > k:
                heappop(heap)  #  remove element O(Logk)
        
        return heappop(heap)


### Dictionary
- `k in d` - O(1)
- Get Item/Set Item/ Delete Item - O(10

### collections.deque
If you need to add/remove at both ends, consider using a collections.deque instead.
- `from collections import deque `
- `de = collections.deque([1,2,3])` 
- `de.append(4)` - O(1)
- `de.appendleft(6)` - O(1)
- `de.pop()` - O(1)
- `de.popleft()` - O(1)


### Functions

Enumerate - useful to get the item and the index at the same time `for i, char in enumerate(shortest):`

Heapq - heaps in python

Sort by Key: intervals.sort(key=lambda interval: interval[0])  

Min by Key: shortest = min(strs, key=len)
