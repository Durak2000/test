class Animal:
    def __init__(self, name):
        self.name = name

        def speak(self):
            raise NotImplementedError('Siskasti')


class Dog(Animal):
    def speak(self):
        return f'{self.name} говорит Раф на кокосовом!'


class Cat(Animal):
    def speak(self):
        return f'{self.name} говорит иди отсюда сиськастый!'


dog = Dog('Влад будочник')
cat = Cat('Улетаю на гаити')

print(dog.speak())
print(cat.speak())
