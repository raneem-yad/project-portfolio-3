class User:
    def __init__(self,id,username,fullname, email, password):
        self.id = id
        self.username= username
        self.fullname = fullname
        self.email = email
        self.password = password
        
    def login(self,username, password):
        print("login")