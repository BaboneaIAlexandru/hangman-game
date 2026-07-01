import requests
from random import randint

url = "https://random-word-api.herokuapp.com/word?lang=en&number=1"

def choose_word(difficulty):

    if difficulty=="Easy":
        difficulty=1
        length=randint(3,5)
    elif difficulty=="Medium":
        difficulty=3
        length=randint(6,8)
    elif difficulty=="Hard":
        difficulty=5
        length=randint(9,12)

    req=requests.get(url,params={"diff":difficulty,"length":length})
    word=req.json()[0].upper()
    return word

