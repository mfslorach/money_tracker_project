import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    
    def setUp(self):
        self.transaction = Transaction(4.50, "Falafel To Go", "Takeaway")
    
    def test_transaction_has_amount(self):
        self.assertEqual(4.50, self.transaction.amount)

    def test_transaction_has_merchant(self):
        self.assertEqual("Falafel To Go", self.transaction.merchant)

    def test_transaction_has_tag(self):
        self.assertEqual("Takeaway", self.transaction.tag)

    def test_transaction_has_id(self):
        self.assertEqual(None, self.transaction.id)
    