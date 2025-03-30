class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1

    @staticmethod
    def get_count():
        return Counter.count


obj_1 = Counter()
obj_2 = Counter()
obj_3 = Counter()

print(Counter.get_count())
