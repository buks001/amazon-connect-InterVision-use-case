# This Lambda function tracks customer calls and updating their records in DynamoDB
# Processes incoming events triggered by Amazon Connect,extracts relevant information 
# queries DynamoDB for customer data, updates records, and generates appropriate responses.


import json
import boto3
from datetime import datetime

# Initialize AWS SDK clients
dynamodb = boto3.resource('dynamodb')
table_name = 'connectDemo'  # Replace with your DynamoDB table name
table = dynamodb.Table(table_name)

def build_response_failed():
    results = {
        'lambdaResult': 'Error'
    }
    print(f"Lambda's Response to Amazon Connect is: {json.dumps(results)}")
    return results

def build_response_number_found(customer_first_name, customer_last_name, last_called_date, last_called_time, customer_first_call):
    results = {
        'firstName': customer_first_name,
        'lastName': customer_last_name,
        'lastCalledDate': last_called_date,
        'lastCalledTime': last_called_time,
        'firstCall': customer_first_call,
        'phoneNumberFound': True,
        'lambdaResult': 'Success'
    }
    print(f"Lambda's Response to Amazon Connect is: {json.dumps(results)}")
    return results

def build_response_number_not_found(customer_first_call):
    results = {
        'firstCall': customer_first_call,
        'phoneNumberFound': False,
        'lambdaResult': 'Success'
    }
    print(f"Lambda's Response to Amazon Connect is: {json.dumps(results)}")
    return results

def lambda_handler(event, context):
    try:
        # Set the timezone for the Lambda function
        import os
        os.environ['TZ'] = 'America/New_York'

        # Set the options for the date format
        date_options = {
            'weekday': 'short',
            'year': 'numeric',
            'month': 'short',
            'day': 'numeric'
        }

        # Set the variables to record the current local date and time
        current_short_date = datetime.now().strftime('%Y-%m-%d')
        current_long_date = datetime.now().strftime('%a, %d %b %Y')
        current_time = datetime.now().strftime('%H:%M:%S')
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Log the incoming event from Amazon Connect for troubleshooting purposes
        print(f"Received event from Amazon Connect at: {current_timestamp}")
        print(f"Amazon Connect Event Details: {json.dumps(event)}")

        # Set the variables for the customer ANI and unique contact ID
        source_phone_number = event.get('Details', {}).get('ContactData', {}).get('CustomerEndpoint', {}).get('Address')
        current_contact_id = event.get('Details', {}).get('ContactData', {}).get('ContactId')

        if source_phone_number is None or current_contact_id is None:
            # If essential information is missing, log an error and return a failure response
            print("Error: 'Details' key or essential information not found in the event")
            return build_response_failed()

        # Set up the database query to be used to lookup customer information from DynamoDB
        params_query = {
            # DynamoDB Table Name. Replace with your table name
            'TableName': 'connectDemo',
            'KeyConditionExpression': 'phoneNumber = :varNumber',
            'ExpressionAttributeValues': {
                ':varNumber': source_phone_number
            }
        }

        # Set up the database query to be used to update the customer information record in DynamoDB
        params_update = {
            # DynamoDB Table Name. Replace with your table name
            'TableName': 'connectDemo',
            'Key': {
                'phoneNumber': source_phone_number
            },
            'ExpressionAttributeValues': {
                ':var1': current_timestamp,
                ':var2': current_long_date,
                ':var3': current_time,
                ':var4': current_contact_id,
            },
            'UpdateExpression': 'SET lastCalledTimeStamp = :var1, lastCalledDate = :var2, lastCalledTime = :var3, lastCalledCallId = :var4'
        }

        # Use the lookup query (params_query) we set up to lookup the customer data based on the source phone number from DynamoDB 
        response = table.query(**params_query)

        # Check to make sure the query executed correctly, if not, error out the lambda function
        if 'Items' not in response:
            print(f"Error in DynamoDB query response: {json.dumps(response)}")
            return build_response_failed()

        # Log the results from the DynamoDB query
        print(f"DynamoDB Query Results: {json.dumps(response)}")

        # Check to ensure only 1 record came back for the customer phone number
        if len(response['Items']) == 1:
            # Set variables for the pertinent information from the returned database record
            customer_last_called_date = response['Items'][0].get('lastCalledDate', '')
            customer_last_called_time = response['Items'][0].get('lastCalledTime', '')
            customer_first_name = response['Items'][0].get('firstName', '')
            customer_last_name = response['Items'][0].get('lastName', '')

            # Check to see if there is a record of a previous call and set the previous call variable accordingly
            customer_first_call = not bool(customer_last_called_date)

            # Update the customer record in the database with the new call information using the params_update query we set up above
            table.update_item(**params_update)

            # Callback with a successful response for found phone number
            return build_response_number_found(
                customer_first_name,
                customer_last_name,
                customer_last_called_date,
                customer_last_called_time,
                customer_first_call
            )
        else:
            # Customer record not found, update the record with new contact ID
            customer_first_call = True
            table.update_item(**params_update)

            # Callback with a successful response for not found phone number
            return build_response_number_not_found(customer_first_call)

    except Exception as e:
        # Log and handle any errors
        print(f"Error: {e}")
        return build_response_failed()
