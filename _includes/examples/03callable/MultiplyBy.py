class MultiplyBy:
    def __init__(self, factor: int):
        self.factor = factor
    def __call__(self, x):
        return self.factor * x