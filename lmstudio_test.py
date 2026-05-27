# Импортируем OpenAI-клиент, но будем использовать его не для OpenAI,
# а для локального сервера LM Studio
from openai import OpenAI

# Создаём клиента и указываем локальный адрес LM Studio
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # Для LM Studio можно указать любую строку
)

# Отправляем запрос в локальную модель
response = client.chat.completions.create(
    model="google/gemma-4-e2b@q4_k_m",
    messages=[
        {
            "role": "user",
            "content": "Объясни одним предложением, что такое нейронная сеть."
        }
    ],
    temperature=0.7,
)

# Печатаем ответ модели
print(response.choices[0].message.content)