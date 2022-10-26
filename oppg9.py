#A#
class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self. starttidspunkt= starttidspunkt
        self.varighet = varighet

    #B# streng metode for klasse avtale.
    def __str__(self):
        return f"tittel: {self.tittel}, sted: {self.sted}, starttidspunkt:{self.starttidspunkt}"









