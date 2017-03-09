class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

    def longest_name(self):
        longest = ""
        for contact in self:
            if len(contact.name) > len(longest):
                longest = contact.name
                if longest:
                    return longest


class Contact(object):
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        return cls.all_contacts.clear()


class Supplier(Contact):
    all_orders = {}

    def order(self, order):
        key = self.email
        value = [order]
        if key in self.all_orders:
            self.all_orders[key].append(value)
        else:
            self.all_orders[key] = value
