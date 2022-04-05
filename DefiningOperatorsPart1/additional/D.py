class Queue:
    queue = []

    def add(self, elem):
        self.queue.append(elem)
        return "done"

    def remove(self):
        if len(self.queue) == 0:
            return None
        elem = self.queue[0]
        del self.queue[0]
        return elem

    def len(self):
        return len(self.queue)

    def last(self):
        if len(self.queue) == 0:
            return None
        return self.queue[-1]

    def first(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def clear(self):
        self.queue = []
        return "done"
