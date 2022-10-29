# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:09:10 2022

@author: Vincent Medrano
"""

class book(dict):
    
    def __init__(self):
        self.key = "key"
        self.author = "author"
        self.length = 0
        self.genre = "genre"
        self.sel = "selection"
    
    
    def getChoice(self):
        print("Book options are...\n")
        print("Add, Lookup, Exit\n")
        
        choice = 0
        
        while choice not in ("Add", "Lookup", "Exit"):
            choice = input("Make your selection\n")
        
        if choice == "Add":
            self.add_book()
        elif choice == "Lookup":
            self.lookup()
        else:
            print("Bye bye for now")
        
    def add_book(self):
        self.key = input("Enter Title of Book...\n")
        self.author = input("Enter the name of Author...\n")
        self.length = int(input("Enter number of pages...\n"))
        self.genre = input("What genre: 'Rap', 'HipHop', 'Classical', 'Alternative'")
        
        if self.genre == "":
            self[self.key] = self.author, self.length
        else:
            self[self.key] = self.author, self.length, self.genre
            
            
        print("You added:\n", book_obj)
        
        book.getChoice(book_obj)
    
    def lookup(self):
        print(book_obj)
        #book.getChoice(book_obj)
        print("Add genre to existing book?\n,Note: if you select Y you will reenter book.\n Y or N?")
        
        choice = 0
        
        while choice not in ("Y", "N"):
            choice = input("Make your selection\n")
        
            if choice == "Y":
                self.add_book()
            else:
               book.getChoice(book_obj)
        
        
        
###############################################################################

book_obj = book()
book_obj.getChoice()

