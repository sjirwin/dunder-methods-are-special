class Swallow:
    def __init__(self, state: str):
        self.state = state.lower()
    def __bool__(self):
        return self.state == 'unladen'