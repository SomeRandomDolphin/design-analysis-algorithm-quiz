import heapq

class Stack:
    def __init__(self, items=None):
        self._items = []
        
        if items:
            for item in items:
                self.push(item)
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        try:
            item = self._items.pop()
            return item
        except:
            print('ERROR! trying to pop an element from an empty stack.')
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __repr__(self):
        return f'Stack(items={self._items})'
    
    def __str__(self):
        return f"[{', '.join(self._items)}]"
    

class Queue:
    def __init__(self, items=None):
        self._items = []
        
        if items:
            for item in items:
                self.push(item)
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        try:
            item = self._items[0]
            self._items = self._items[1:]
            return item
        except:
            print('ERROR! trying to pop an element from an empty queue.')
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __repr__(self):
        return f'Queue(items={self._items})'
    
    def __str__(self):
        return f"[{', '.join(self._items)}]"
    

class PriorityQueue:
    def __init__(self, items=None):
        self._items = []
        self.index = 0
        
        if items:
            for item, priority in items:
                self.push(item, priority)
        
    def push(self, item, priority):
        entry = (priority, self.index, item)
        heapq.heappush(self._items, entry)
        self.index += 1
    
    def pop(self):
        try:
            _, _, item = heapq.heappop(self._items)
            return item
        except:
            print('ERROR! trying to pop an element from an empty priority queue.')
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __repr__(self):
        return f'PriorityQueue(items={self._items})'
    
    def __str__(self):
        res = '['
        for priority, _, item in self._items:
            res += f' {item}({priority}) '
        res += ']'
        return res