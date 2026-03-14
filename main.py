from fastapi import FastAPI
from agent import run_agent
from servicenow import create_ticket

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Support Agent Running"}


@app.post("/create-ticket")
def create_ticket_api(short_description: str, description: str):

    ticket = create_ticket(short_description, description)

    return ticket


if __name__ == "__main__":
    run_agent()