import json
import requests

def lambda_handler(event, context):
    # Extract parameters from event
    access_token = event.get('access_token')
    start_date = event.get('start_date')
    end_date = event.get('end_date')

    # Validate inputs
    if not access_token or not start_date or not end_date:
        return {
            'statusCode': 400,
            'body': 'Missing required parameters: access_token, startdate, or enddate'
        }

    # Set request headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Fitbit API URL for step count
    fitbit_api_url = f"https://api.fitbit.com/1/user/-/activities/steps/date/{start_date}/{end_date}.json"

    try:
        # Make request to Fitbit API
        response = requests.get(fitbit_api_url, headers=headers)

        # Check for success response
        if response.status_code == 200:
            step_data = response.json()
            return {
                'statusCode': 200,
                'body': json.dumps(step_data)
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': f"Error fetching data: {response.text}"
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Internal Server Error: {str(e)}"
        }
