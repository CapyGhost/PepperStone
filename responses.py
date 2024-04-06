from random import choice, randint
import pepperstone

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    
    if "!" in lowered:
        try:
            response = pepperstone.chat.send_message(lowered)
            response = response.text
        except:
            response = "message was blocked due to nsfw. if these was no nsfw try again later"
        return response
