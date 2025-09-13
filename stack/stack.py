class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)  # Apila un elemento

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Desapila el último
        return None  # Si está vacía

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Muestra el tope sin sacar
        return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Pila (top -> bottom): " + " -> ".join(map(str, reversed(self.items)))
    
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack)  # Pila (top -> bottom): 30 -> 20 -> 10

print("Top element:", stack.peek())  # 30

print("Popped:", stack.pop())  # 30
print("After pop:", stack)  # 20 -> 10

print("Is empty?", stack.is_empty())  # False
print("Size:", stack.size())  # 2




from queue import Queue, LifoQueue, PriorityQueue
from collections import deque

# Crear una pila con capacidad opcional (máxima)
stack = LifoQueue()

# Apilar elementos
stack.put(10)
stack.put(20)
stack.put(30)

# Ver el tamaño actual
print("Tamaño de la pila:", stack.qsize())  # 3 

# Desapilar elementos
print("Elemento desapilado:", stack.get())  # 30
print("Elemento desapilado:", stack.get())  # 20

# Verificar si está vacía
print("¿Está vacía?", stack.empty())  # False


print("=== Queue (FIFO) ===")
fifo = Queue()
fifo.put('A')
fifo.put('B')
fifo.put('C')

print(fifo.get())  # A
print(fifo.get())  # B
print(fifo.get())  # C

print("\n=== LifoQueue (Pila - LIFO) ===")
lifo = LifoQueue()
lifo.put('A')
lifo.put('B')
lifo.put('C')

print(lifo.get())  # C
print(lifo.get())  # B
print(lifo.get())  # A

print("\n=== PriorityQueue ===")
pq = PriorityQueue()
pq.put((2, "Tarea media"))
pq.put((1, "Tarea urgente"))
pq.put((3, "Tarea menos urgente"))

print(pq.get())  # (1, "Tarea urgente")
print(pq.get())  # (2, "Tarea media")
print(pq.get())  # (3, "Tarea menos urgente")

print("\n=== deque (FIFO) ===")
dq_fifo = deque()
dq_fifo.append('A')
dq_fifo.append('B')
dq_fifo.append('C')

print(dq_fifo.popleft())  # A
print(dq_fifo.popleft())  # B
print(dq_fifo.popleft())  # C

print("\n=== deque (LIFO / Pila) ===")
dq_lifo = deque()
dq_lifo.append('X')
dq_lifo.append('Y')
dq_lifo.append('Z')

print(dq_lifo.pop())  # Z
print(dq_lifo.pop())  # Y
print(dq_lifo.pop())  # X



