from fileinput import filename
from sys import orig_argv


class FataJopa3000:
    def __init__(self, filename, original):
        self.filename = filename
        self.original = None
        self.change = list()

    def print_info(self):
        print(self.filename)

class doks:

    def __init__(self, Data, Imya, Familiya, Strana, Gorod):

        self.Data = "09/03/12"
        self.Imya = "Danya"
        self.Familiya = "Romanchenko"
        self.Strana = "Ukraine"
        self.Gorod = "Nejin"

