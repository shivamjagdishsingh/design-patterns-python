class Database:
    __instance = None
    access_count = 0
    
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        cls.access_count += 1
        return cls.__instance

# First call
Database()
print(Database.access_count)
# output: 1

# Second call
Database()
print(Database.access_count)
# output: 2