import os
import requests
from env import graders 

# Read environment variables
BASE_URL = os.getenv("API_BASE_URL", "http://0.0.0.0:8000")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN", "")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is not set! Please export your Hugging Face token.")

# Actions for each task
tasks_actions = {
    "easy": ["fill_mean"],  # correct missing-value action
    "medium": ["fill_mean", "remove_duplicates"],
    "hard": ["fill_mean", "remove_duplicates", "convert_type"]
}
 # import your graders

def run_task(task):
    print(f"[START] task={task}")
    res = requests.post(f"{BASE_URL}/reset")
    if res.status_code != 200:
        raise RuntimeError(f"Failed to reset environment: {res.text}")

    total_reward = 0

    for i, action in enumerate(tasks_actions[task]):
        res = requests.post(f"{BASE_URL}/step", json={"action": action}).json()
        total_reward += res["reward"]
        print(f"[STEP] step={i} action={action} reward={res['reward']} done={res['done']}")

        if res["done"]:
            break

    # Compute grader score
    state = res["observation"]
    if task == "easy":
        score = graders.grade_easy(state)
    elif task == "medium":
        score = graders.grade_medium(state)
    else:  # hard
        score = graders.grade_hard(state)

    print(f"[END] task={task} total_reward={round(total_reward,2)} grader_score={score}")
    return total_reward, score
if __name__ == "__main__":
    print(f"Using MODEL_NAME={MODEL_NAME} | BASE_URL={BASE_URL}")
    for t in ["easy", "medium", "hard"]:
        run_task(t)
