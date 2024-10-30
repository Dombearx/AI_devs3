from api import send_to_poligon
from utils import get_plain_text_from_url

TASK = "POLIGON"
DATA_URL = "https://poligon.aidevs.pl/dane.txt"


def main():
    data = get_plain_text_from_url(DATA_URL)

    answer = [line for line in data.split("\n") if line]

    send_to_poligon(TASK, answer)


if __name__ == "__main__":
    main()
