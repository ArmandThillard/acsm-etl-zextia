# Result file service
class Results:

    results = []

    def __init__(self, results):
        self.results = results['results']

    def get_last(self):
        return self.results[0]