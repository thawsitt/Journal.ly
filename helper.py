""" This module contains helper functions for journal.py """

# For current date and time
import datetime

# Importing Colorama for cross-platform colored text
import colorama
from colorama import Fore


def print_intro():
    """ Prints a welcome message to the user. """
    colorama.init(autoreset=True)
    print('\n=====================================')
    print(Fore.YELLOW + 'Welcome to The Grand Budapest Journal')
    print('=====================================\n')
    colorama.deinit()


def print_datetime():
    """ Prints current date and time. """
    colorama.reinit()
    print('Date: ' + Fore.CYAN + get_date())
    print('Time: ' + Fore.GREEN + get_time())
    colorama.deinit()


def get_date():
    """ Returns today's date in the following format.
    e.g. 'Tue, Jan 03 2017'
    """
    days = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun')
    today = datetime.datetime.now().strftime("%b %d %Y")
    date = days[datetime.datetime.today().weekday()]
    return date + ', ' + today


def get_iso_date():
    """ Returns today's date in ISO format: YYYY_MM_DD """
    return datetime.date.today().isoformat()


def get_time():
    """ Returns current time in the following format.
    e.g. '10:30 PM'
    """
    return datetime.datetime.now().strftime("%I:%M %p")
