
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Action(BaseModel):
    action: str

state = {}

def init_state():
    return {
        "step": 0,
        "missing_fixed": 0,
        "duplicates_removed": 0,
        "type_converted": 0
    }

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    global state
    state = init_state()
    return {"observation": state}

@app.post("/step")
def step(action: Action):
    global state
    state["step"] += 1

    reward = 0.0
    done = False

    if action.action == "fix_missing":
        state["missing_fixed"] += 1
        reward += 0.3

    elif action.action == "remove_duplicates":
        state["duplicates_removed"] += 1
        reward += 0.3

    elif action.action == "convert_type":
        state["type_converted"] += 1
        reward += 0.3

    else:
        reward -= 0.1  # penalty

    score = (state["missing_fixed"] + state["duplicates_removed"] + state["type_converted"]) / 3

    if score >= 1.0:
        done = True
        reward = 1.0

    return {
        "observation": state,
        "reward": round(reward, 2),
        "done": done,
        "info": {"score": round(score, 2)}
    }

@app.get("/state")
def get_state():
    return state
