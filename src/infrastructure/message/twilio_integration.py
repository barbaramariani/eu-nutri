from src.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from twilio.rest import Client


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_message() -> None:
    message = client.messages.create(
        body='Olá, :)',
        from_='whatsapp:+14888888888',
        to='whatsapp:+5521999999999'
    )

    print("Message sent: " + message)