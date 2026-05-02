from google import genai
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Новая библиотека google.genai автоматически ищет ключ в переменной окружения GEMINI_API_KEY.
# Убедитесь, что ваш файл .env содержит: GEMINI_API_KEY="ВАШ_API_КЛЮЧ"

def main():
    # Инициализация клиента Gemini. Ключ API будет автоматически взят из GEMINI_API_KEY.
    client = genai.Client()

    # Выбор модели. На данный момент актуальная быстрая модель — gemini-2.0-flash
    # Если появится 2.5, просто измените строку ниже
    model_name = "gemini-2.5-flash"
    
    try:
        # Пример простого текстового запроса
        prompt = "Привет! Расскажи короткую шутку про программистов."

        print(f"Отправка запроса к {model_name}...")
        response = client.models.generate_content(model=model_name, contents=prompt)
        
        print("\nОтвет модели:")
        print("-" * 20)
        print(response.text)
        print("-" * 20)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        print("\nУбедитесь, что:")
        print("1. Вы установили библиотеку: pip install -U google-genai")
        print("2. Вы вставили корректный API ключ.")

if __name__ == "__main__":
    main()
