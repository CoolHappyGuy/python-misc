#This program determines your elf name based on the initial of the user's name as well as their birth month.
FirstInitial = {"a": "Perky", "b": "Nipper", "c": "Bubbles", "d": "Happy", "e": "Squeezy", "f": "Sunny", "g": "Merry",
                "h": "Tootsie", "i": "Kringle", "j": "Puddin", "k": "Cookie", "l": "Tinker", "m": "Twinkle",
                "n": "Buddy", "o": "Elfie", "p": "Jingle", "q": "Snowflake", "r": "Jolly", "s": "Elvis",
                "t": "Sugarplum", "u": "Peaches", "v": "Gingerbread", "w": "Frisbee", "x": "Evergreen", "y": "Pinky",
                "z": "Tinsel"}
BirthMonth = {"jan": "Angel-pants", "feb": "Floppy-feet", "mar": "Plum-pants", "apr": "McJingles", "may": "Peppermint",
              "jun": "Toe-bells", "jul": "Sugarplum", "aug": "Sugar-socks", "sep": "Pickle-pants", "oct": "Sparkly-toes"
              , "nov": "Monkey-buns", "dec": "Pointy-toes"}

#Prompt User for initial of first name and validate.
UserInitial = str(input("Please enter the initial of your first name: ")).lower()
while UserInitial not in FirstInitial:
    print("Invalid!  Please enter the letter (A-Z) of the initial of your first name.")
    UserInitial = str(input("Please enter the initial of your first name: ")).lower()
#Prompt user for birth month and validate.
UserMonth = input("Please enter your birth month (first three letters of month): ").lower()
while UserMonth not in BirthMonth:
    print("Invalid!  Please enter the first 3 letters of your birthmonth (e.g. January = Jan, etc)")
    UserMonth = input("Please enter your birth month (first three letters of month): ").lower()
# print("Your elf name is " + str(UserInitial) + " " + str(UserMonth) + ".")
print("\n" + "Your elf name is " + FirstInitial[UserInitial] + " " + BirthMonth[UserMonth] + ".")

