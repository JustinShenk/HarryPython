ELDER_THRESHOLD = 70
ADULT_THRESHOLD = 18
CHILD_THRESHOLD = 2


class Human():
    '''Middle-size race.'''

    def __init__(self, age=None, sex=None, name=None, job=None, appearance=[], possesions=[], activities=[], emotions=[], description=[]):
        self.age = age
        try:
            if any(comparer in self.age for comparer in ['<', '>']):
                self.guessAge()
        except:
            pass
        self.sex = sex
        self.name = name
        self.appearance = appearance
        self.job = job
        self.possessions = possesions
        self.activities = activities
        self.emotions = emotions
        self.description = description

    def set_location(self, location):
        self.location = location

    def say(self, content, emotion=None, quoted=False):
        print(self.name, emotion, "says,", '"{}"'.format(content))

    def guessAge(self):
        if eval(ELDER_THRESHOLD + self.age):
            self.age_group = 'Elder'
        elif eval(ADULT_THRESHOLD + self.age):
            self.age_group = 'Adult'
        elif eval(CHILD_THRESHOLD + self.age):
            self.age_group = 'Child'
        else:
            self.age_group = 'Baby'
        self.age = None

    def esteem(self, target, value):
        while True:
            try:
                self.esteems[target] = value
                break
            except AttributeError:
                self.esteems = {}
            except KeyError:
                self.esteems[target] = []
                self.esteems[target].append(value)

    def emotion(self, emotion, content):
        self.emotions.append((emotion, content))

    def relates(self, target, relation):
        while True:
            try:
                self.relations[target] = relation
                break
            except AttributeError:
                self.relations = {}

    def then(self, action='does something'):
        print(self.name, 'then', action)


class Setting():

    def __init__(self, location=None, weather=None, day=None, time=None, contains=[]):
        self.location = location
        self.weather = weather
        self.day = day
        self.time = time
        self.contains = contains
