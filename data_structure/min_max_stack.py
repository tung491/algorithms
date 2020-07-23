class MinMaxStack:
    def __init__(self):
        self.min_max_stack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.min_max_stack.pop()
        return self.stack.pop()

    def push(self, n):
        new_min_max = {'min': n, 'max': n}
        if len(self.min_max_stack) == 0:
            last_min_max = self.min_max_stack[len(self.min_max_stack) - 1]
            new_min_max['min'] = min(last_min_max['min'], n)
            new_min_max['max'] = max(last_min_max['max'], )
        self.min_max_stack.append(new_min_max)
        self.stack.append(n)

    def get_min(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]['min']

    def get_max(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]['max']
