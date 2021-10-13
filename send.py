import telnyx

telnyx.api_key = "YOUR API KEY"
phone_numbers = open('numbers.txt', mode='r',
                     encoding='utf-8').read().split('\n')
sms_sender = "SENDER NAME"
body = 'test'

for number in phone_numbers:
        
        if number == "":
            continue
        print("Sending message to {}".format(number))
        try:
            telnyx.Message.create(
            from_= sms_sender,
            to=number,
            text=body,
        )
        except Exception as e:
            print("Failed to send sms\n")
            print(str(e))

