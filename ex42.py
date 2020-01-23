## Animal is-a object
class Animal(object):
  pass

## Dog is-a Animal
class Dog(Animal):
  def __init__(self, name):
    ## Dog has-a name
    self.name = name

## Cat is-a Animal
class Cat(Animal):
  def __init__(self, name):
    ## Cat has-a name
    self.name = name

## Person is-a object
class Person(object):
  def __init__(self, name):
    ## Person has-a name
    self.name = name

    ## Person has-a pet
    self.pet = None

## Employee is-a Person
class Employee(Person):

  def __init__(self, name, salary):
    ## Super-constructor
    super(Employee, self).__init__(name)

    ## Employee has-a salary
    self.salary = salary

## Fish is-a object
class Fish(object):
  pass

## Salmon is-a Fish
class Salmon(Fish):
  pass

## Halibut is-a Fish
class Halibut(Fish):
  pass

## rover is-a Dog which is-a Animal
rover = Dog("Rover")

## satan is-a Cat which is-a Animal
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## frank is-a Emplyee which is-a Person, and has-a name and salary
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon which is-a Fish
crouse = Salmon()

## harry is a halibut which is-a Fish
harry = Halibut()