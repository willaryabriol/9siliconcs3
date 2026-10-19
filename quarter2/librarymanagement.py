# initializing the Publication class (parent class)
class Publication:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @property
    def get_title(self): #this function returns the title of the material
        return self.title

    @property
    def get_author(self): #this function returns the name of the author
        return self.author

    def set_title(self, title): #this function alters the title
        self.title = title

    def set_author(self, author): #this function alters the author
        self.author = author

    @property
    def display_info(self): #this function prints the title and author
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

#initializing the Book class, which inherits from the Publication class
class Book(Publication):

    def __init__(self, title, author, number_pages):
        super().__init__(title, author) #super() is used because our Book class inherits some of its attributes
        self.number_pages = number_pages

    @property
    def get_number_of_pages(self): #this function returns the number of pages
        return self.number_pages

    def set_number_of_pages(self, number_pages): #this function alters the number of pages

        #note: we must check first if the number of pages is positive
        if number_pages < 0:
            print("Number of pages must be positive.")
        else:
            self.number_pages = number_pages

#initializing the Magazine class, which inherits from the Publication class
class Magazine(Publication):

    def __init__(self, title, author, issue_number):
        super().__init__(title, author) #super() is used because our Magazine class inherits some of its attributes
        self.issue_number = issue_number

    @property
    def get_issue_number(self): #this function returns the issue number
        return self.issue_number

    def set_issue_number(self, issue_number): #this function alters the issue number

        #note: we must check first if the issue number is positive
        if issue_number < 0:
            print("Issue number must be positive.")
        else:
            self.issue_number = issue_number

# note: @property is used so that we can call the functions with this decorator like a normal variable, with no parentheses needed