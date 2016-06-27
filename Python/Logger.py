import os
import datetime

script_directory = os.path.dirname(__file__)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def main():
    addLogCommands = set(["add log", "+log", "+ log", "continue log", '+'])
    editProgramCommands = set(["edit last", "edit last line", "recall"])
    exitProgramCommands = set(["exit", "quit", 'bye'])

    while True:
        task = input(">")
        if task.lower() == "push":
            push()
        elif task.lower() in addLogCommands:
            addNewLogEntry()
        elif task.lower() in exitProgramCommands:
            break
        elif task.lower() in editProgramCommands:
            retrieveLastLineForEditing()
        elif task.lower()[0] == '+':
            addNewLogEntry(task[1:])
        else:
            print("sorry, command '", task, "' not recognized")


def push():
    print("Saving...")
    month = months[datetime.datetime.now().month - 1]
    currentDate = "{} {}, {}".format(month, datetime.datetime.now().day, datetime.datetime.now().year)
    tempFile = open(os.path.join(script_directory, "temp_files/tempLog.txt"), 'r+')
    date = (months[datetime.datetime.now().month + 1], datetime.datetime.now().day, datetime.datetime.now().year, datetime.datetime.now().hour, datetime.datetime.now().minute, 'AM' if isAM(datetime.datetime.now().minute) else 'PM')
    deepRecord = open(os.path.join(script_directory, "deepStorage/{} {}, {} at {}-{}{}.txt".format(*date)), 'a+')
    oldData = tempFile.read().splitlines()
    newData = ["{} {},{} at {}:{}{}".format(*date)] + oldData
    for line in newData:
        deepRecord.write(line + "\n")
    tempFile.close()
    tempFile = open(os.path.join(script_directory, "temp_files/tempLog.txt"), 'w+')
    tempFile.write("")
    tempFile.close()
    print("Saved")

def getUserInput(prompt):
    return input(promptString)

def addNewLogEntry(*args):
    promptString = "{}:{}{}>".format(datetime.datetime.now().hour, datetime.datetime.now().minute, 'AM' if isAM(datetime.datetime.now().hour) else 'PM')
    if args:
        newEntry = args[0]
    else:
        newEntry = getUserInput(promptString)
    tempFile = open(os.path.join(script_directory, "temp_files/tempLog.txt"), 'a+')
    tempFile.write('{}{}\n'.format(promptString, newEntry))
    #tempFileData = tempFile.read().splitlines()
    #tempFileData.append(newEntry)
    #print(tempFileData)
    #tempFile.close()
    #tempFile = open(os.path.join(script_directory, "temp_files/tempLog.txt"), 'w+')
    #tempFile.write("{}\n".format(line for line in tempFileData))
    tempFile.close()

def retrieveLastLineForEditing():
    tempFile = open(os.path.join(script_directory, "temp_files/tempLog.txt"), 'r+')
    print(tempFile.read().splitlines())
    lastLine = tempFile.read().splitlines()[-1:]
    editedLine = input(lastLine)
    #save logic here

#add option to edit last line

def isAM(hour):
    if hour < 12:
        return True
    return False

main()