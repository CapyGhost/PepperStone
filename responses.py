from random import choice, randint
import pepperstone

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    
    if "$" in lowered:
        try:
            response = pepperstone.chat.send_message(lowered)
            response = response.text
        except:
            response = "your message has been blocked cause of nsfw or being ratelimited due to constant messages"
        return response
