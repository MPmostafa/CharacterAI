from characterai import aiocai
import asyncio

async def main():
    char = "De_AzlU9pHh8ujlZ672Va2H4esHlGrAnVlgzJQzivAw"
    client = aiocai.Client('b2daeded189d8ea3cadfcae9aa159d90966775fd')
    chat = 'f89c3b7d-9fd9-420c-a98a-a3916a06b34'
    me = await client.get_me()

    async with await client.connect() as chat:

        print(f'{answer.name}: {answer.text}')
        
        while True:
            text = input('YOU: ')

            message = await chat.send_message(
                char, chat, text
            )

            print(f'{message.name}: {message.text}')

asyncio.run(main())
