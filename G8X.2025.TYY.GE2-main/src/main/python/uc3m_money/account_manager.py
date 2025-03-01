"""Module """

class AccountManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_iban(iban: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        if len(iban) != 24:
            return False
        elif iban[0:2] != "ES":
            return False
        end_of_iban = iban[4:]
        int_iban = int(end_of_iban + "1518" + iban[2:4])
        if int_iban % 97 != 1:
            return False
        return True


