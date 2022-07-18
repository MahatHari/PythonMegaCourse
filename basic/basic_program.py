
def sentence_maker(phrase):
    interrogatives = ("how", "what", "why", )
    captilized = phrase.capitalize()
    if phrase.lower().startswith(interrogatives):
        return "{}?".format(captilized)
    else:
        return "{}.".format(captilized)


input_array = []
while True:
    user_input = input("Say something: ")
    if user_input == 'end':
        break
    else:
        input_array.append(sentence_maker(user_input))
        continue


print(" ".join(input_array))
