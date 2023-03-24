import json

# import requests


def lambda_handler(event, context):
    print(event)
    print("End of Message - New Feature 2")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
