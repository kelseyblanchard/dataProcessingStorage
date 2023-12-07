class InMemoryDB:
    def __init__(self):
        self.initialArray = {}
        self.workingArray = {}
        self.transaction = False

    def get(self, key):
        if self.transaction == False:
            return self.initialArray.get(key)

    def put(self, key, val):
        if self.transaction == False:
            raise Exception("Transaction not in progress.")
        self.workingArray[key] = val

    def begin_transaction(self):
        if self.transaction == True:
            raise Exception("Transaction already in progress.")
        self.transaction = True

    def commit(self):
        if self.transaction == False:
            raise Exception("No transaction in progress to commit.")
        self.initialArray.update(self.workingArray)
        self.transaction = False

    def rollback(self):
        if self.transaction == False:
            raise Exception("No transaction in progress to rollback.")
        self.workingArray.update(self.initialArray)
        self.transaction = False

db = InMemoryDB()

# should return null, because A doesn’t exist in the DB yet
print(db.get('A'))

# should throw an error because a transaction is not in progress
db.put('A', 5)

# starts a new transaction
db.begin_transaction()

# set’s value of A to 5, but its not committed yet
db.put('A', 5)

# should return null, because updates to A are not committed yet
print(db.get('A'))

# update A’s value to 6 within the transaction
db.put('A', 6)

# commits the open transaction
db.commit()

# should return 6, that was the last value of A to be committed
print(db.get('A'))

# throws an error, because there is no open transaction
db.commit()

# throws an error because there is no ongoing transaction
db.rollback()

# should return null because B does not exist in the database
print(db.get('B'))

# starts a new transaction
db.begin_transaction()

# Set key B’s value to 10 within the transaction
db.put('B', 10)

# Rollback the transaction - revert any changes made to B
db.rollback()

# Should return null because changes to B were rolled back
print(db.get('B'))

