
import os
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

def run_task(task):
    print(f"[START] task={task}")
    requests.post(f"{BASE_URL}/reset")

    actions = ["fix_missing", "remove_duplicates", "convert_type"]

    total = 0

    for i, act in enumerate(actions):
        res = requests.post(f"{BASE_URL}/step", json={"action": act}).json()
        total += res["reward"]

        print(f"[STEP] step={i} reward={res['reward']} done={res['done']}")

        if res["done"]:
            break

    print(f"[END] task={task} total_reward={round(total,2)}")

if __name__ == "__main__":
    for t in ["easy","medium","hard"]:
        run_task(t)
