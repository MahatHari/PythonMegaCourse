import re


class Mind():
    def __init__(self) -> None:
        pass

    def think(self, query):
        if 'sum' in query:
            numbers = re.findall(r"\b\d+\b", query)
            float_numbers_list = [float(num) for num in numbers]
            return sum(float_numbers_list)


class Robot():
    def __init__(self) -> None:
        self.mind = Mind()  # Roboto initilization also initializes Mind

    def print_out(self, query):
        print(self.mind.think(query))

    def write_down(self, query):
        with open('sum.txt', 'w') as f:
            f.write(str(self.mind.think(query)))


robot = Robot()
print(robot.write_down("what is the sum of 8 and 10"))
