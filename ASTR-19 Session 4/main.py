class FavoriteAnimal:
    def __init__(self, name, animalType, armLength, legLength, numOfEyes, tail, furry):
        self.name = name
        self.animalType = animalType
        self.armLength = armLength
        self.legLength = legLength
        self.numOfEyes = numOfEyes
        self.tail = tail
        self.furry = furry

    def Description(self):
        print("This animal's name is " + self.name + ". They are a " + self.animalType + ".")
        print("This animals arms are " + str(self.armLength) + " feet long, and it's legs are " + str(self.legLength) + " feet long.")
        print("This animal has " + str(self.numOfEyes) + " eyes.")

        if (self.tail):
            print("This animal has a tail.")
        else:
            print("This animal does not have a tail.")

        if (self.furry):
            print("This animal is furry.")
        else:
            print("This animal is not furry.")

        return

myDog = FavoriteAnimal("Bernie", "Dog", 0.0, 0.8, 2, True, False)
myDog.Description()