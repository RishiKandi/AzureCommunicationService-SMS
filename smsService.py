import os
from azure.communication.sms import SmsClient
try:
    sms_client = SmsClient.from_connection_string("endpoint=https://smsservi.communication.azure.com/;accesskey=zzREl8BMkcTwZNfkOvbyTx3BWpol3hxzU+XXd9nzQJlLWezF8Np2+RJEvXKzTU99rZO5vh8ZmU2QeI2Oftcvfw==")

    sms_responses = sms_client.send( 
        from_="+18332434288",
        to="+917972083675",
        message="Hello World via SMS", 
        enable_delivery_report=True, # optional property       
        tag="custom-tag") # optional property
    print("sms sent", sms_responses)
except Exception as ex:
    print('Exception:')
    print(ex)