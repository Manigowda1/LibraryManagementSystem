import datetime,os

# print(os.getcwd())

class LMS:
    '''
    This class is to keep records of library,
    Has 4 Modules - Display, issue, add, returt books.

    '''
    def __init__(self,list_of_books,library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101

        with open(self.list_of_books) as bk:
            content = bk.readlines()
            # print(content)
        for line in content:

            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
                                             "lender_name":"","issue_date":"","status":"Available"}})
            Id+=1

    def display_books(self):
        print("Book ID"+ "\t\t" + "Title")
        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title")," - [",value.get("status"), "]")

    def issue_books(self):
        book_id = input("Enter Book ID : ")
        current_date = datetime.datetime.now().strftime("%y - %m - %d  %H:%M:%S")
        if book_id in self.books_dict.keys():
            if not self.books_dict[book_id]["status"] == "Available":
                print(f"This book is already issued to {self.books_dict[book_id]['lender_name']}"
                      f"on {self.books_dict[book_id]['issue_date']}")
                return self.issue_books()
            elif self.books_dict[book_id]["status"] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[book_id]['lender_name']= your_name
                self.books_dict[book_id]['issue_date'] = current_date
                self.books_dict[book_id]['status'] = "Not available"
                print("Book issued successfully\n")
        else:
            print("Book not found")

    def add_book(self):
        new_book = input("Enter book title: ")
        if new_book == "":
            return self.add_book()
        elif len(new_book)> 25:
            print("Books title is too long")
            return self.add_book()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_book}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_book,'lender_name':"",'issue_date':"",'status':"Available"}})
                print(f"New book {new_book} has been added successfully")



    def return_book(self):
        book_id = input("Enter book ID: ")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["status"] == "Available":
                print("This book is already available in library")
                # return self.return_book()
            elif not self.books_dict[book_id]["status"] == "Available":
                self.books_dict[book_id]['lender_name'] = ""
                self.books_dict[book_id]['issue_date'] = ""
                self.books_dict[book_id]['status'] = "Available"
                print("Book return successful!!")
        else:
            print("Book Id not found")


try:
    myLMS = LMS("List_of_books.txt","Mani's Library")
    press_key_list = {'D':"Display Books",'I':"Isssue Books",'A':"Add Books",'R':"return Books ",'Q':"To quit"}
    key_press = False
    while not (key_press=="q"):
        print(f"\n-----------------Welcome--to-----{myLMS.library_name}\n")
        for key,value in press_key_list.items():
            print("Press",key, "to", value)
        key_press = input("press key: ").lower()
        if key_press == "i":
            print("\n Current selection : issue Books")
            myLMS.issue_books()
        elif key_press == 'a':
            print("\n Current selection : Add Books")
            myLMS.add_book()
        elif key_press == 'd':
            print("\n Current selection : Display Books")
            myLMS.display_books()
        elif key_press == 'r':
            print("\n Current selection : Return Books")
            myLMS.return_book()
        elif key_press == 'q':
            break
        else:
            continue

except Exception as e:
    print("Something went wrong , Please check")


# l = LMS("List_of_books","Python Library")
#
# l.display_books()

