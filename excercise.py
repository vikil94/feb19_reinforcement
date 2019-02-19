
# excercise 1

emotions = {'joy' : 3,
            'sadness' : 1,
            'fear' : 2,
            'anger': 3 }


# for emotion, level in emotions.items():
#     print("{} felt at level {}".format(emotion, level))


# excercise 2
class Person:


    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        return "This is your person class: {} and this is my emotions dictionary {}".format(self.name, self.emotions)

# excercise 3
 # going through a loop that looks for the key which is emotion in this case 
 # and the value which is level. It sorts through the emotions dictionary
    def show_emotions(self):
        for emotion, level in emotions.items():
            display_emotion = None
            if level == 1:
                display_emotion = "low"
            elif level == 2:
                display_emotion = "medium"
            elif level == 3:
                display_emotion = "high"
            print("I am feeling {} amount of {}".format(display_emotion, emotion))

person1 = Person("Vikil", emotions)
print(person1)
print("Excercise 3")
person1.show_emotions()
