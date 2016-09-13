import unittest
from main import *


class ContactListTestCases(unittest.TestCase):

    def setUp(self):
        if "reset_contacts" in dir(Contact):
            Contact.reset_contacts()

    def test_contact_entries(self):
        contact = Contact("Some Body", "somebody@example.net")
        self.assertEqual(hasattr(contact, 'name'), True)
        self.assertEqual(hasattr(contact, 'email'), True)
        self.assertEqual(contact.name, "Some Body")
        self.assertEqual(contact.email, "somebody@example.net")

    def test_all_contacts(self):
        contact1 = Contact("Some Body", "somebody@example.net")
        self.assertEqual(len(contact1.all_contacts), 1)
        contact2 = Contact("Sandor Brody", "sandor.brody@example.net")
        self.assertEqual(len(Contact.all_contacts), 2)
        contact3 = Contact("Elek Benedek", "elek.benedek@example.net")
        self.assertEqual(len(Contact.all_contacts), 3)

    def test_supplier_entries(self):
        supplier = Supplier("Supp Lier", "suplier@example.net")
        self.assertEqual(supplier.__class__.__bases__[0].__name__, "Contact")
        self.assertEqual(supplier.name, "Supp Lier")
        self.assertEqual(supplier.email, "suplier@example.net")

    def test_all_contacts_with_suppliers(self):
        supplier1 = Supplier("Supp Lier", "suplier@example.net")
        contact1 = Contact("Some Body", "somebody@example.net")
        self.assertEqual(len(Contact.all_contacts), 2)

    def test_supplier_order(self):
        supplier1 = Supplier("Supp Lier", "suplier@example.net")
        supplier1.order("CD Player")
        self.assertEqual(len(Supplier.all_orders.keys()), 1)
        self.assertEqual(len(Supplier.all_orders[supplier1.email]), 1)
        supplier1.order("DVD Player")
        self.assertEqual(len(Supplier.all_orders.keys()), 1)
        self.assertEqual(len(Supplier.all_orders[supplier1.email]), 2)

    def test_contactlist_search(self):
        self.assertEqual(len(Contact.all_contacts.search('John')), 0)
        contact1 = Contact("Some Body", "somebody@example.net")
        contact2 = Contact("Sandor Brody", "sandor.brody@example.net")
        contact3 = Contact("Elek Benedek", "elek.benedek@example.net")
        self.assertEqual(len(Contact.all_contacts.search('John')), 0)
        self.assertEqual(len(Contact.all_contacts.search('Benedek')), 1)

    def test_contactlist_longest_name(self):
        self.assertEqual(Contact.all_contacts.longest_name(), None)
        contact1 = Contact("Some", "somebody@example.net")
        contact2 = Contact("Sandor", "sandor.brody@example.net")
        contact3 = Contact("Elek Benedek", "elek.benedek@example.net")
        self.assertEqual(Contact.all_contacts.longest_name(), "Elek Benedek")


if __name__ == '__main__':
    unittest.main()
