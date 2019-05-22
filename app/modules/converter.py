"""
    Converter
    _______________
"""
class Converter:

    buy = 627000 # 22 may 2019
    sell = 598880 # 22 may 2019

    def __init__(self, types):
        self.types = types
    # end def

    def gram_to_idr(self, amount):
        if amount <= 0:
            raise ValueError

        return getattr(self, self.types) * amount
