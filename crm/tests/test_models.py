import unittest
from applications.models import Application


class TestApplicationClass(unittest.TestCase):
    def test_payments_property(self):
        """
        Test payments property for Application class.
        """
        application = Application()
        application.name = "Test"
        application.agreement_id = "2"
        self.assertEqual( application.payments,
        "Payment ID: 1\nAmount: 24.00\nDate: 03-12-2017\n\nPayment ID: 5\n" +
        "Amount: 27.00\nDate: 01-12-2017\n\n")
