def save_history(command):
    with open("history.txt", "a") as f:
        f.write(command + "\n")