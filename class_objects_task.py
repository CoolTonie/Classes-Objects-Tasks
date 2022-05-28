
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name=str(name)
        self.age= int(age)
        self.tracks= list(tracks)
        self.score= float(score)

    def change_name(self, new_name):
        self.name= new_name
        new_name= "peter"
        print(f'My name is name to {new_name}')

    def change_age (self, new_age):
        self.age= new_age
        new_age= 34
        print(f'I am {new_age} years old')

    def add_tracks(self, new_tracks):
        self.tracks= new_tracks
        new_tracks= ("UI/UX")
        print(f'My current track is {new_tracks}')

    def get_score(self, new_score):
        self.score=new_score
        new_score=2.5
        print(f'I have a score of {new_score}')

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score(2.5)

print('THE END!!!')
