import random
import time
import sys

# DATA TO BE MANIPULATED
Data1 = [5004, 2008, 9003, 4000, 4017, 5026, 3431]
Data2 = [7896, 5328, 4810, 5551, 8024, 9055, 6117]
Data3 = [3347, 4490, 6632, 8932, 4567, 8096, 7865]

ADMINPASSWORD = Data1[5] + Data2[5] + Data3[5]

CorrectData = {
    Data1[2]: 1,  # default = 9003
    Data2[5]: 2,  # default = 9055 (CHANGING THIS ONE AFFECTS ADMIN PASSWORD)
    Data3[3]: 3,  # default = 8932
    ADMINPASSWORD: 4
}


# Functions of this program

def Intro(stage):
    counter = 6
    while stage < counter:  # prints out all the lists for a cool title
        rotator = random.choice([Data1, Data2, Data3])
        print(rotator)
        time.sleep(0.1)
        stage += 1

    def title(title):
        for char in title:  # loops over each character in the title
            print(char)
            time.sleep(0.075)
        print('')

    print('')
    title('password\nchecker')
    print('')
    print('---------------\n---------------\n---------------')
Intro(0)


def AffectAdmin(DI, Dataset):
    if DI < Dataset:
        Difference = Dataset - DI
        print(f'ADMIN PASSWORD CHANGED BY -{Difference}')
        Datasetsum = ADMINPASSWORD - Difference
        CorrectData[Datasetsum] = 4
    elif DI > Dataset:
        Difference = DI - Dataset
        print(f'ADMIN PASSWORD DEFAULT IS +{Difference}')
        Datasetsum = ADMINPASSWORD + Difference
        CorrectData[Datasetsum] = 4


def Incorrect_Input_Handler(text, type): #Text = What the input says   Type = What type the input needs
    while True:
        try:
            user_input = input(text).strip() #What makes this function recognised as an input when called 
            if type == int:
                return int(user_input)
            elif type == str:
                if user_input.isdigit():
                    raise ValueError("That is not a string. We need strings")
                return user_input  # return the string as it is
        except ValueError as ValErr:
            print(ValErr) #Shows the value error along with input
        except TypeError as TyErr:
            print(TyErr) #Same as value error except


def SeeAdmin():
    checkAge = Incorrect_Input_Handler('How old are you?: ', int)
    if checkAge == 18: #(my age as of writing this program)
        print('Write this down... You have 10 seconds')
        time.sleep(2)
        print(f'The admin password is {ADMINPASSWORD}')
        time.sleep(10)
        passwdchecker()
    else:
        print('Bet you thought you were slick.')
        skull = """
          @@@@@@@                                      @@@@@@@
        @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
         @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
             @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
               @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
                 @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
                    @@@@@@@    @@@@@@    @@@@@@
                    @@@@@@      @@@@      @@@@@
                    @@@@@@      @@@@      @@@@@
                     @@@@@@    @@@@@@    @@@@@
                      @@@@@@@@@@@  @@@@@@@@@@
                       @@@@@@@@@@  @@@@@@@@@
                   @@   @@@@@@@@@@@@@@@@@   @@
                   @@@@  @@@@ @ @ @ @ @@@@  @@@@
                  @@@@@   @@@ @ @ @ @ @@@   @@@@@
                @@@@@      @@@@@@@@@@@@@      @@@@@
              @@@@          @@@@@@@@@@@          @@@@
           @@@@@              @@@@@@@              @@@@@
          @@@@@@@                                 @@@@@@@
           @@@@@                                   @@@@@
        """ #Skull found on https://ascii.co.uk/art/skulls
        for char in skull:
            print(char, end='', flush=True)
            time.sleep(0.01) #Prints the skull in a cool way
        sys.exit(3)


def recover():
    global ADMINPASSWORD #In the event of Agent 2 being changed (Data2[5]) the ADMINPASSWORD must be changed globally as well
    Q = Incorrect_Input_Handler('Have you forgotten your password? (Y/N): ', str).lower()
    if Q == 'y':
        EnterName = Incorrect_Input_Handler('Please enter your user name: ', str)
        if EnterName == 'Agent 1':
            DI1 = Incorrect_Input_Handler('Enter new password: ', int)
            Data1.pop(2)
            Data1.insert(2, DI1)
            CorrectData[DI1] = 1
            print('Password successfully changed.')
            passwdchecker()
        elif EnterName == 'Agent 2':
            DI2 = Incorrect_Input_Handler('Enter your new password: ', int)
            AffectAdmin(DI2, Data2[5])
            Data2.pop(5)
            Data2.insert(5, DI2)
            CorrectData[DI2] = 2
            ADMINPASSWORD = Data1[5] + Data2[5] + Data3[5]
            print('Password successfully changed.')
            passwdchecker()
        elif EnterName == 'Agent 3':
            DI3 = Incorrect_Input_Handler('Enter your new password: ', int)
            Data3.pop(3)
            Data3.insert(3, DI3)
            CorrectData[DI3] = 3
            print('Password successfully changed.')
            passwdchecker()
        elif EnterName == 'I AM THE ADMIN':
            SeeAdmin()
        else:
            print('Invalid user name.')
            recover()
    elif Q == 'n':
        passwdchecker()
    else:
        print('Invalid input.')
        recover()


def paa():  # If ADMIN ACCESS is "given"
    for i in range(10):
        print('ADMIN ACCESS GRANTED ' * i)


def passwdchecker():
    user_input = Incorrect_Input_Handler('Please enter your password: ', int)
    Find = CorrectData.get(user_input)
    if Find is None or user_input is None:
        recover()
    elif user_input == ADMINPASSWORD:
        paa()
    else:
        print(f'Hello Agent {Find}')
passwdchecker()
