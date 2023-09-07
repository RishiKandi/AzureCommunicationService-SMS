from azure.identity import DefaultAzureCredential
from azure.communication.sms import SmsClient

# Replace with your Azure Communication Service endpoint and the name of your resource
communication_service_endpoint = "YOUR_COMMUNICATION_SERVICE_ENDPOINT"
resource_name = "YOUR_RESOURCE_NAME"

credential = DefaultAzureCredential()

sms_client = SmsClient(communication_service_endpoint, credential)
try:
    # Replace with the recipient phone number (in E.164 format) and the message
    recipient_phone_number = "+1234567890"
    message = "Hello from Azure Communication Services!"

    sms_response = sms_client.send(
        from_=resource_name,
        to=recipient_phone_number,
        message=message
    )

    print(f"Message sent with message ID: {sms_response.message_id}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
