class CustomQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, element):
        self.enqueue_stack.append(element)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            return None
        return self.dequeue_stack.pop()

    def print_front(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            return None
        return self.dequeue_stack[-1]


def process_queries(queries):
    custom_queue = CustomQueue()
    for query in queries:
        query_type, *args = map(int, query.split())
        if query_type == 1:
            custom_queue.enqueue(args[0])
        elif query_type == 2:
            custom_queue.dequeue()
        elif query_type == 3:
            front_element = custom_queue.print_front()
            if front_element is not None:
                print(front_element)


input = "1 42,2,1 14,3"
process_queries(input.split(','))

