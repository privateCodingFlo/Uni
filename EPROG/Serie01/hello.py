# Übung 2
print("Hello, World!", end=" ")
print("I am Florian Kainrath and I study technical mathematics at TU Wien")

# Übung 3
# "" weglassen => Programm kann nicht aufgeführt werden, da es so als Befehle gehandhabt werden, anstelle eines Strings/Textes

# Übung 4


def checkInput(text):
    # Warnung: keine Überprüfung eingebaut, ob die Eingabe keine Zahl ist
    userInput = float(input(text+":\t"))

    if userInput > 100:
        userInput = 100
    elif userInput < 0:
        userInput = 0

    return userInput


final_exam = checkInput("Final exam grade")
weekly_exam = checkInput("Weekly exam grade")
exercise = checkInput("Exercise grade\t")

grade = 0.4 * final_exam + 0.4 * weekly_exam + 0.2 * exercise

# gewollte Ausgabe
print("Your final grade is:", grade)
# formatierte Ausgabe mit Einheit
print("Your final grade is: {0}%".format(grade))
