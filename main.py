from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import random

app = FastAPI()

class PlayRequest(BaseModel):
    player: int

# Allow only requests from the specified website
origins = [
    "https://codechallenge.boohma.com",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["GET", "POST"],  
    allow_headers=["*"],  
)

rules = {
    "rock": ["scissors", "lizard"],  # rock beats scissors and lizard
    "paper": ["rock", "spock"],      # paper beats rock and spock
    "scissors": ["paper", "lizard"], # scissors beats paper and lizard
    "lizard": ["paper", "spock"],    # lizard beats paper and spock
    "spock": ["scissors", "rock"]    # spock beats scissors and rock
}

choices_dict: dict = {
    1: "rock",
    2: "paper",
    3: "scissors",
    4: "lizard",
    5: "spock"
}

score_board_history: list[dict] = []


@app.get("/choice")
def get_random_choice(response: Response):
    """Return random choice"""
    random_key = random.choice(list(choices_dict.keys()))
    
    random_value = choices_dict[random_key]
     
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, proxy-revalidate"
   
    return { "id": random_key, "name": random_value}



@app.get("/choices")
def choices():
    """Return all choices in id-name pairs"""
    return [{"id": key, "name": value} for key, value in choices_dict.items()]


@app.post("/play")
def play(r: PlayRequest):
    """Play the game, computer choice will be calculated randomly"""
    computer_choice = (get_random_number() % 5) + 1
    player_choice = r.player
    result = battle(choices_dict[player_choice], choices_dict[computer_choice])
    response = {"results": result, "player": player_choice, "computer": computer_choice} 

    score_board_history.append(response)
    return response 

@app.get("/history")
def history():
    return { "history": score_board_history[:10]}

@app.post("/reset-score")
def reset_score():
    score_board_history = []
    return {"message": "Scoreboard reset successfully"} 

def get_random_number():
    """get random number from third-party api"""
    with httpx.Client() as client:
        external_url = "https://codechallenge.boohma.com/random" 
        response = client.get(external_url)
        external_data = response.json()
    return external_data.get("random_number", 0) 

def battle(player_choice: str, computer_choice: str) -> str:
    """return result of the battle"""
    if player_choice == computer_choice:
        return "draw"
    elif computer_choice in rules[player_choice]:
        return "win"
    else:
        return "lose"
