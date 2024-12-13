#Christopher Robles Serrano
#Module 12 Lab 
#12/12/2024
#This program using OOP techinques to create Pet classes with 3 attributes. It takes user input to instantiate our object(Pet).



#Pet class.
class Pet():
    #Custom constructors for the Pet class. Using default values.
    def __init__(self, name = 'Butters', type = 'Dog', age = 1):
        self.__name = name
        self.__type = type
        self.__age = age

    #Setters for our attributes.
    def setName(self, name):
        self.__name = name
   
    def setType(self, type):
        self.__type = type
    
    def setAge(self, age):
        self.__age = age
    

    #Getters for our attributes.
    def getName(self):
        return self.__name
    
    def getType(self):
        return self.__type
    
    def getAge(self):
        return self.__age
    

    #Custom method to print our object as a string.
    def __str__(self):
        return f'Your pet is called {self.getName()}, it is a {self.getType()} who is {self.getAge()} years old'


#Main method.      
def main():
    #Empty list to house all of our pet names.
    myPets = []

    #Variable and loop keep our program running until user decides to quit.
    continue_input = 'yes'
    while continue_input == 'yes':
        try: 
            #Variable to house our Pet name and Pet type.
            myPetName = input('Enter your pet name: ').capitalize()
            myPetType = input(f'\nWhat kind of animal is {myPetName}: ')

            #Variable to house our Pet age as an integer.
            myPetAge = int(input(f'\nHow old is {myPetName}(in years): '))
            
            #Instantiation using our variables as the arguments.  
            myPet = Pet(myPetName, myPetType, myPetAge)

            #Printing our pet using the __str__ method.
            print(myPet)

            #Using the continue_input variable to loop over if the user wants to.
            continue_input = input("\nDo you want to add another pet? (yes/no): ").strip().lower()

            #Input validation for the continue_input variable.
            while continue_input not in ['yes', 'no']:
                print('ERROR: Input must be in (yes or no)\n')
                continue_input = input("Do you want to add another pet? (yes/no): ").strip().lower()
            
            #Appending myPet name to the our list of names(myPets).
            myPets.append(myPet.getName())
            
            #Break the loop if the user says 'no'.
            if continue_input == 'no':
                break
        
        #Print statement for ValueError
        except ValueError:
            print(f'Age must be a numerical value!')
    
    #Printing all of our pets using the join method to convert from a list to a string.
    print(f'Bye bye: {", ".join(myPets)}!') 


#Calling main method.
main()