import json

# import requests


def lambda_handler(event, context):
    print(event)
    print("End of Message - New Feature - Dev Branch")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
