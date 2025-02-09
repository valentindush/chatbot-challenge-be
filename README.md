# Chatbot Backend (Challenge)

This is a FastAPI-based chatbot backend that integrates with Groq + Langchain. The API supports streaming responses and is designed to be used with a frontend application.


## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `virtualenv` (optional but recommended)
- Docker & Docker Compose (if running with Docker)

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/valentindush/chatbot-challenge-be.git
cd fastapi-chatbot
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy the example environment file and update it with your own values:
```sh
cp .env.example .env
```

Ensure your `.env` file contains the necessary `GROQ_API_KEY`.
You can get your own key from [console.groq.com/keys](https://console.groq.com/keys).

### 5. Run the Application
#### Using FastAPI directly:
```sh
fastapi dev app/main.py
```

#### Using Docker Compose:
```sh
docker compose up --build
```

The application will be available at:
- **Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **API Root:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

