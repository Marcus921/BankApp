class Customer:
    def __init__(self, first_name, last_name, SSN_list):
        self.first_name = first_name
        self.last_name = last_name
        self.SSN_list = SSN_list

    def __str__(self):
        return f"First name: {self.first_name}, Lastname: {self.last_name} - SSN: {self.SSN_list}"

if __name__ == "__main__":
    print("This python script is not meant to be run directly, please import in another class!")
    quit()