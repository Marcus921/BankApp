from account import *
from customer import *

class Bank(Account, Customer):
    def __init__(self):
        self