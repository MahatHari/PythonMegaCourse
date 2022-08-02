import difflib
import re


def similartiy_between_text(input1, input2):
    return(difflib.SequenceMatcher(None, input1, input2).ratio())


def similartiy_between_text_matchedsequence(input1, input2):
    return(difflib.SequenceMatcher(None, input1, input2).get_matching_blocks())


print("Ratio", similartiy_between_text("Hello There", "Hello Here"))

print("Longest Match", similartiy_between_text_matchedsequence(
    "Hello There", "Hello Here"))


"""
Genius Robot
Alter the speak method so that it returns the sum of numbers for queries containing the word "sum" and two integers.

Examples of usage:

robot = Robot()
print(robot.speak("what is the sum of 1 and 2"))
print(robot.speak("what is the sum of 8 and 10"))
The output of that would be:

3

18
"""


class Robot():
    def __init__(self) -> None:
        pass

    def speak(self, query):
        if 'sum' in query:
            numbers = re.findall(r"\b\d+\b", query)
            return sum([float(x) for x in numbers])


robot = Robot()
print(robot.speak("what is the sum of 1 and 2"))
print(robot.speak("what is the sum of 8 and 10"))
