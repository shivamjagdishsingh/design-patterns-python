from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    
    @abstractmethod
    def clone(self):
        pass


class Email(Prototype):
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
    
    def clone(self):
        return copy.deepcopy(self)


class Letter(Prototype):
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
    
    def clone(self):
        return copy.deepcopy(self)

email = Email("Water crisis", "Hey there, Hope you are doing fine.....")
letter = Letter("Road issues", "Hello, I am writing this letter to......")

email_copy = email.clone()
letter_copy = letter.clone()

print(email_copy.subject, email_copy.body)
print(letter_copy.subject, letter_copy.body)
