from openai import OpenAI

client = OpenAI(api_key="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",
                base_url="https://openrouter.ai/api/v1" )

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1:free", 
    messages=[
        {
            "role":"user",
            "content":"what is portuguese"
        }
    ]
)

print(chat.choices[0].message.content)