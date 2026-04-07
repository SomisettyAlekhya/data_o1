
class DataCleaningEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "step": 0,
            "missing_fixed": 0,
            "duplicates_removed": 0,
            "type_converted": 0
        }
        return self.state

    def step(self, action):
        self.state["step"] += 1
        reward = 0.0
        done = False

        if action == "fix_missing":
            self.state["missing_fixed"] += 1
            reward += 0.3
        elif action == "remove_duplicates":
            self.state["duplicates_removed"] += 1
            reward += 0.3
        elif action == "convert_type":
            self.state["type_converted"] += 1
            reward += 0.3
        else:
            reward -= 0.1

        score = (self.state["missing_fixed"] + self.state["duplicates_removed"] + self.state["type_converted"]) / 3

        if score >= 1.0:
            done = True
            reward = 1.0

        return self.state, reward, done, {"score": score}
