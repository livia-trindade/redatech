import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
  },
  
  data=json.dumps({
    "model": "deepseek/deepseek-r1:free", 
    "messages": [
      {
        "role": "user",
        "content": "quais são as vogais do alfabeto?"
      }
    ]
  })
)
if response.status_code == 200:
    print("Resposta bruta:", response.text)  
    try:
        result = response.json() 
        print(result)
    except requests.exceptions.JSONDecodeError as e:
        print("Erro ao decodificar JSON:", e)
else:
    print(f"Erro na requisição: {response.status_code} - {response.text}")
