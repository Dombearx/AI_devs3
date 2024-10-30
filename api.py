import os
from consts import API_URL
import requests
from loguru import logger
from dto import PoligonResponse
from dotenv import load_dotenv

load_dotenv()
AI_DEVS_API_KEY = os.getenv("AI_DEVS_API_KEY")


def send_to_poligon(task_name: str, answer) -> PoligonResponse:
    # Send the answer to the API
    payload = {"task": task_name, "apikey": AI_DEVS_API_KEY, "answer": answer}
    # Send the payload to the API
    response = requests.post(API_URL, json=payload)
    json_response = response.json()
    poligon_response = PoligonResponse(**json_response)

    # Print the response
    logger.info(f"Code: {poligon_response.code}")
    logger.info(f"Message: {poligon_response.message}")

    return poligon_response
