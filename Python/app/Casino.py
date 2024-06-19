class Casino:
    
    def __init__(self):
        self._persons = []

    def accept(self, person):
        self._persons.append(person)

    def contains(self, person):
        return person in self._persons

    def get_persons_count(self):
        return len(self._persons)

    def kickout(self, person):
        self._persons.remove(person)
