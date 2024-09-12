# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.lock_utxos_request_utxos_inner import LockUtxosRequestUtxosInner


class TestLockUtxosRequestUtxosInner(unittest.TestCase):
    """LockUtxosRequestUtxosInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LockUtxosRequestUtxosInner:
        """Test LockUtxosRequestUtxosInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LockUtxosRequestUtxosInner`
        """
        model = LockUtxosRequestUtxosInner()
        if include_optional:
            return LockUtxosRequestUtxosInner(
                token_id = 'BTC',
                tx_hash = '9bdf8e7ae03c237e115f09543fbdb40f8efa600106e78b67ce4d5adfadda2dbb',
                vout_n = 0
            )
        else:
            return LockUtxosRequestUtxosInner(
                token_id = 'BTC',
                tx_hash = '9bdf8e7ae03c237e115f09543fbdb40f8efa600106e78b67ce4d5adfadda2dbb',
                vout_n = 0,
        )
        """

    def testLockUtxosRequestUtxosInner(self):
        """Test LockUtxosRequestUtxosInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
