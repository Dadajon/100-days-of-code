class Person:
    """
    Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter.
    The constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative;
    if a negative argument is passed as initialAge, the constructor should set age to 0 and print "Age is not valid, setting age to 0.".
    In addition, you must write the following instance methods:
    """

    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        if self.initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.initialAge = 0
        else:
            self.initialAge = initialAge

    def amIOld(self):
        """
        If age < 13, print "You are young."
        If age ≥ 13 and age < 18, print "You are a teenager."
        Otherwise, print "You are old."

        :return: string
        """
        # Do some computations in here and print out the correct statement to the console
        if 13 <= self.initialAge < 18:
            print("You are a teenager.")
        elif self.initialAge < 13:
            print("You are young.")
        else:
            print("You are old.")

    def yearPasses(self):
        """
        Increase the age instance variable by 1.

        :return: age++
        """
        # Increment the age of the person in here
        self.initialAge += 1

t = int(input())
for i in range(0, t):
    age = int(input())
    print(age)
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("="*50)