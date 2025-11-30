with open("log.txt", "a") as f_append:
    f_append.write("\nProgram run successfully")

with open("log.txt", "r") as f_read:
    logs = [log[: len(log) - 1] if "\n" in log else log for log in f_read.readlines()]
    for log in logs:
        print(log)