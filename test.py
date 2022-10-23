import uuid
import random
import datetime
import json
import unittest
from worker import insert_event


@unittest.skip
def test_trigger(event, context):
    for data in event["Records"]:
        try:
            event_data = data["body"]
            print(event_data)
        except Exception as e:
            raise e
    return None


class TestWorker(unittest.TestCase):
    def make_dummy_event(self):
        new_event = {"event_id": str(uuid.uuid1()), "user_id": "khs" + str(random.randint(0, 5)), "event": "purchase",
                     "parameters": {
                         "order_id": str(uuid.uuid1()),
                         "currency": "krw",
                         "price": random.randint(0, 99) * 100
                     }, "event_datetime": datetime.datetime.utcnow().isoformat(timespec='milliseconds')}
        return new_event

    # https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html
    def make_dummy_sqs_message(self):
        dummy_data = {
            "Records": [
                {
                    "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
                    "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
                    "body": json.dumps(self.make_dummy_event()),
                    "attributes": {
                        "ApproximateReceiveCount": "1",
                        "SentTimestamp": "1545082649183",
                        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                        "ApproximateFirstReceiveTimestamp": "1545082649185"
                    },
                    "messageAttributes": {},
                    "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
                    "eventSource": "aws:sqs",
                    "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
                    "awsRegion": "us-east-2"
                },
                {
                    "messageId": "2e1424d4-f796-459a-8184-9c92662be6da",
                    "receiptHandle": "AQEBzWwaftRI0KuVm4tP+/7q1rGgNqicHq...",
                    "body": json.dumps(self.make_dummy_event()),
                    "attributes": {
                        "ApproximateReceiveCount": "1",
                        "SentTimestamp": "1545082650636",
                        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                        "ApproximateFirstReceiveTimestamp": "1545082650649"
                    },
                    "messageAttributes": {},
                    "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
                    "eventSource": "aws:sqs",
                    "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
                    "awsRegion": "us-east-2"
                }
            ]
        }
        return dummy_data

    def test_worker(self):
        dummy_data = self.make_dummy_sqs_message()
        for record in dummy_data["Records"]:
            print(record["body"])
        print()
        result = insert_event(dummy_data, None)
        print(result)
        unittest.TestCase().assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
