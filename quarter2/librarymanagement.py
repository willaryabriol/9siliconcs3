class Publication:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @property
    def get_title(self):
        return self.title

    @property
    def get_author(self):
        return self.author

    def set_title(self, title):
        pass

    def set_author(self, author):
        pass

    @property
    def display_info(self):
        pass

class Book(Publication):

    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.number_pages = number_pages


    @property
    def get_number_of_pages(self):
        return self.number_pages

    def set_number_of_pages(self, number_pages):
        if number_pages < 0:
            print("Number of pages must be positive.")
        else:
            self.number_pages = number_pages

class Magazine(Publication):

    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    @property
    def get_issue_number(self):
        return self.issue_number

    def set_issue_number(self, issue_number):
        if issue_number < 0:
            print("Issue number must be positive.")
        else:
            self.issue_number = issue_number