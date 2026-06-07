def log(message):

    with open("logs.txt", "a") as file:

        file.write(message + "\n")