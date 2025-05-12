import requests
from bot.config import settings

API_TOKEN = settings.HUGGINGFACE_TOKEN
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

TEXT_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon3-7b-instruct"
IMAGE_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"


def generate_text(prompt: str) -> str:
    res = requests.post(TEXT_URL, headers=HEADERS, json={"inputs": prompt})
    try:
        return res.json()[0]["generated_text"]
    except Exception:
        return f"❌ Text error: {res.status_code} - {res.text}"


def generate_image(
    prompt: str, path: str = "/mnt/data/test_generated_image.png"
) -> str:
    res = requests.post(IMAGE_URL, headers=HEADERS, json={"inputs": prompt})
    if res.status_code == 200:
        with open(path, "wb") as f:
            f.write(res.content)
        return path
    return f"❌ Image error: {res.status_code} - {res.text}"


def run_tests():
    print("🔤 Text test:")
    print(generate_text("Напиши коротку мотиваційну цитату для жінок."))

    print("\n🖼️ Image test:")
    print(generate_image("Жінка на вершині гори на світанку, акварельний стиль"))


if __name__ == "__main__":
    run_tests()
