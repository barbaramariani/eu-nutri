from fastapi import APIRouter, Request
from src.application.use_cases.calculate_macros import CalculateMacros
from twilio.twiml.messaging_response import MessagingResponse

router = APIRouter()

@router.post('/webhook')
async def webhook(request: Request):
    form_data = await request.form()
    message_body = form_data.get('Body')
    from_number = form_data.get('From')
    to_number = form_data.get('To')

    response = process_message(message_body, from_number, to_number)

    twiml_response = MessagingResponse()
    twiml_response.message(response)

    return str(twiml_response)

def process_message(message_body, from_number, to_number):
    macro_nutrients = CalculateMacros(message_body)

    return "Macronutrients from your meal:" + macro_nutrients

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)