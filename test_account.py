import unittest
import account
class TestAccount(unittest.TestCase):
    def test_get_owner(self):
        # Given
        kowalski_account = account.Account("Jan", "Kowalski")
        # When
        owner = kowalski_account.get_owner()
        # Then
        self.assertTrue(isinstance(owner, str))
        self.assertEqual(owner, "Jan Kowalski")
    def test_get_balance(self):
        # Given
        kowalski_account = account.Account("Jan", "Kowalski")
        # When + Then: account just after creation is always empty
        self.assertEqual(kowalski_account.get_balance(), 0.0)
    def test_deposit(self):
        kowalski_account = account.Account("Jan", "Kowalski")
        kowalski_account.deposit(100.0)
        self.assertTrue(kowalski_account.get_balance(), 100.0)
    def test_deposit_big(self):
        kowalski_account = account.Account("Jan", "Kowalski")
        kowalski_account.deposit(1000000000000000)
        kowalski_account.deposit(0.34)
        kowalski_account.withdraw(1000000000000000)
        self.assertEqual(kowalski_account.get_balance(), 0.34)
    # the negative deposit bug replicator
    @unittest.expectedFailure
    def test_bug_replicator_negative_deposit(self):
        kowalski_account = account.Account("Jan", "Kowalski")
        kowalski_account.deposit(-100.0)
        self.assertEqual(kowalski_account.get_balance(), -100.00)
    def test_withdraw(self):
        kowalski_account = account.Account("Jan", "Kowalski")
        self.assertFalse(kowalski_account.withdraw(500.0))
        kowalski_account.deposit(500.0)
        self.assertTrue(kowalski_account.withdraw(500.00))
        self.assertEqual(kowalski_account.get_balance(), 0.0)

    def test_transfer_to(self):
        # Given
        scr_account = account.Account("Jan", "Kowalski")
        scr_account.deposit(250.0)
        dst_account = account.Account("Piotr", "Wiśniewski")

        # Then
        scr_account.transfer_to(dst_account, 100.0)
        self.assertEqual(scr_account.get_balance(), 150)