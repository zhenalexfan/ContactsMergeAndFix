class ContactUtils:
    @staticmethod
    def to_str(contact: object, verbose=False):
        string = str()
        for key, value in contact.items():
            if not verbose and not value.strip():
                continue
            string += "{0:<20} {1}\n".format(key + ': ', value)
        return string