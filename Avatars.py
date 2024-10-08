import requests
import random

# Zrobić losowy seed
seed = random.randint(0, 1)
seed = ["Felix", "Aneka"]


def main():
    response = requests.get(f"https://api.dicebear.com/9.x/pixel-art/svg?seed={seed}")

    with open('avatar.svg', 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    main()