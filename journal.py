""" The Grand Budapest Journal """

# Importing helper functions
import helper

# Importing Colorama for cross-platform colored text
import colorama
from colorama import Fore


def main():
    introduce()
    entry = writeJournal()
    writeToFile(entry)
    

def introduce():
    helper.print_intro()
    helper.print_datetime()


def writeJournal():
    colorama.init(autoreset=True)
    print(Fore.YELLOW + '\nWhat would you like to add to today\'s journal, Monsieur?')
    activities = list()
    while True:
        item = input('>>> ')
        if item == '':
            confirm = input(Fore.YELLOW + 'Is there anything else you\'d like to add? ')
            if confirm not in ('y', 'Y', 'yes', 'Yes', 'yeah', 'sure'):
                break
        activities.append(item)
    colorama.deinit()
    return activities


def writeToFile(entry):
    filename = helper.get_iso_date() + '.txt'
    with open(filename, 'w') as file:
        file.write('======================\n')
        file.write('Date: ' + helper.get_date() + '\n')
        file.write('======================\n')
        for activity in entry:
            file.write('\n* ' + activity + '\n')
        file.write('\n- - - - -\n')
        file.write(helper.get_time() + '\n')
        file.write('- - - - -')

    print('Journal entry saved successfully!')


if __name__ == '__main__':
    main()
