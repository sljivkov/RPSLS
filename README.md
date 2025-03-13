# FastAPI Rock-Paper-Scissors-Lizard-Spock Game

This is a simple FastAPI-based game of Rock-Paper-Scissors-Lizard-Spock. The application allows a player to compete against the computer, which makes random choices. It also tracks the game history and allows resetting the score.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)

### Installation & Running Locally
1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd fastapi-game
   ```

2. **Create a virtual environment and install dependencies**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application**
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```


## 📌 API Endpoints

### 1️⃣ Get Random Choice
- **Endpoint:** `GET /choice`
- **Description:** Returns a random choice from rock, paper, scissors, lizard, or spock.
- **Response Example:**
  ```json
  {
    "id": 3,
    "name": "scissors"
  }
  ```

### 2️⃣ Get All Choices
- **Endpoint:** `GET /choices`
- **Description:** Returns all choices as id-name pairs.
- **Response Example:**
  ```json
  [
    { "id": 1, "name": "rock" },
    { "id": 2, "name": "paper" },
    { "id": 3, "name": "scissors" },
    { "id": 4, "name": "lizard" },
    { "id": 5, "name": "spock" }
  ]
  ```

### 3️⃣ Play the Game
- **Endpoint:** `POST /play`
- **Description:** Play a round of the game. The computer picks randomly, and the result is returned.
- **Request Body:**
  ```json
  {
    "player": 1
  }
  ```
- **Response Example:**
  ```json
  {
    "results": "win",
    "player": 1,
    "computer": 3
  }
  ```

### 4️⃣ Get Game History
- **Endpoint:** `GET /history`
- **Description:** Returns the last 10 game results.
- **Response Example:**
  ```json
  {
    "history": [
      { "results": "win", "player": 1, "computer": 3 }
    ]
  }
  ```

### 5️⃣ Reset Scoreboard
- **Endpoint:** `POST /reset-score`
- **Description:** Clears the game history.
- **Response Example:**
  ```json
  {
    "message": "Scoreboard reset successfully"
  }
  ```

## 🐳 Running with Docker

1. **Build the Docker image**
   ```sh
   docker build -t fastapi-game .
   ```
2. **Run the container**
   ```sh
   docker run -p 8000:8000 fastapi-game
   ```

## 📌 Notes
- The game uses an external API (`https://codechallenge.boohma.com/random`) for random number generation.
- CORS is restricted to `https://codechallenge.boohma.com`.

Happy coding! 🚀

