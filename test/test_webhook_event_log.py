# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cobo_waas2.models.webhook_event_log import WebhookEventLog


class TestWebhookEventLog(unittest.TestCase):
    """WebhookEventLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookEventLog:
        """Test WebhookEventLog
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookEventLog`
        """
        model = WebhookEventLog()
        if include_optional:
            return WebhookEventLog(
                id = '8f2e919a-6a7b-4a9b-8c1a-4c0b3f5b8b1f',
                created_timestamp = 1701396866000,
                request_headers = {"Content-Type": "application/json"},
                request_body = cobo_waas2.models.webhook_event.WebhookEvent(
                    event_id = '8f2e919a-6a7b-4a9b-8c1a-4c0b3f5b8b1f', 
                    url = 'https://example.com/webhook', 
                    created_timestamp = 1701396866000, 
                    type = 'wallets.transaction.created', 
                    data = null, 
                    status = 'Success', 
                    next_retry_timestamp = 1701396866000, 
                    retries_left = 3, ),
                response_body = '',
                response_status_code = 200,
                response_time = 100,
                success = True,
                failure_reason = 'Connect Timeout'
            )
        else:
            return WebhookEventLog(
                id = '8f2e919a-6a7b-4a9b-8c1a-4c0b3f5b8b1f',
                created_timestamp = 1701396866000,
                request_headers = {"Content-Type": "application/json"},
                request_body = cobo_waas2.models.webhook_event.WebhookEvent(
                    event_id = '8f2e919a-6a7b-4a9b-8c1a-4c0b3f5b8b1f', 
                    url = 'https://example.com/webhook', 
                    created_timestamp = 1701396866000, 
                    type = 'wallets.transaction.created', 
                    data = null, 
                    status = 'Success', 
                    next_retry_timestamp = 1701396866000, 
                    retries_left = 3, ),
                success = True,
        )
        """

    def testWebhookEventLog(self):
        """Test WebhookEventLog"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
