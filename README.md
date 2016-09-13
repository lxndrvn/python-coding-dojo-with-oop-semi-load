# python-oop-coding-dojo

Python OOP related exercises for coding dojo

# Contact List

## Step 1

Write a "Contact" class in which you can store contact information with name and email.

## Step 2

Store the Contact objects (which you instantiate) in a list, which is a class attribute, called all_contacts.

## Step 3

Write a reset_contacts class method, which can clean the all_contacts list.

## Step 4

Write a "Supplier" class, which is inherited from the Contact class.

## Step 5

Write an "order" method for the Supplier, which has a single argument - a string.
Store these orders in a class attribute, called all_orders, in a dictionary, where the key is the supplier email (because it's usually unique).

## Step 6

Write a "ContactList" class, which extends the built-in Python "list" (list class, which you use everyday, https://docs.python.org/3.5/library/stdtypes.html#list).
Use this custom ContactList as the storage of all_contacts.

## Step 7

Write a "search" method for the ContactList, which can search in the name of the stored contacts and find the matching names. The input argument is a string (what we search), and the output is a list of all matching Contact objects.

## Step 8

Write a "longest_name" method for the ContactList, which can gives back the longest name from the stored contacts.
