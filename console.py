import pdb
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

# delete all merchants
merchant_repository.delete_all()

# Inital merchants
merchant_1 = Merchant("Falafel To Go")
merchant_2 = Merchant("Tesco")
merchant_3 = Merchant("Halfords")
merchant_4 = Merchant("The Merchant")
merchant_5 = Merchant("MacTassos")

# Save merchants to database
merchant_repository.save(merchant_1)
merchant_repository.save(merchant_2)
merchant_repository.save(merchant_3)
merchant_repository.save(merchant_4)
merchant_repository.save(merchant_5)

# Inital transactions
transaction_1 = Transaction(4.50, merchant_1, "Takeaway")
transaction_2 = Transaction(12.50, merchant_2, "Groceries")
transaction_3 = Transaction(25.00, merchant_3, "Autocare")
transaction_4 = Transaction(15.00, merchant_4, "Entertainment")
transaction_5 = Transaction(5.50, merchant_5, "Takeaway")

# Save transactions to database
transaction_repository.save(transaction_1)
transaction_repository.save(transaction_2)
transaction_repository.save(transaction_3)
transaction_repository.save(transaction_4)
transaction_repository.save(transaction_5)

# merchants = merchant_repository.select_all()
transactions = transaction_repository.select_all()

print(transactions)