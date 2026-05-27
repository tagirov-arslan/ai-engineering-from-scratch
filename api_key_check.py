# Загружаем переменные окружения из файла .env
from dotenv import load_dotenv

# Модуль os нужен, чтобы читать переменные окружения
import os

# Загружаем содержимое .env в окружение Python
load_dotenv()

# Читаем ключ Anthropic из переменных окружения
anthropic_key = os.getenv("ANTHROPIC_API_KEY")

# Читаем ключ OpenAI из переменных окружения
openai_key = os.getenv("OPENAI_API_KEY")

# Проверяем, есть ли ключ Anthropic
if anthropic_key and anthropic_key != "replace_with_your_real_key":
    print("ANTHROPIC_API_KEY: found")
else:
    print("ANTHROPIC_API_KEY: missing or placeholder")

# Проверяем, есть ли ключ OpenAI
if openai_key and openai_key != "replace_with_your_real_key":
    print("OPENAI_API_KEY: found")
else:
    print("OPENAI_API_KEY: missing or placeholder")