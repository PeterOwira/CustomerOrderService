import africastalking
from django.conf import settings

def send_sms(phone_number, message):
    username = settings.AT_USERNAME
    api_key = settings.AT_API_KEY
    
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    
    try:
        response = sms.send(message, [phone_number])
        print(response)
    except Exception as e:
        print(f"Error sending SMS: {e}")