from collections import OrderedDict  # To order dictionary entries
from utility.printable import Printable  # Make screen output user-friendly


class Transaction(Printable):
    def __init__(self, sender, recipient, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])
