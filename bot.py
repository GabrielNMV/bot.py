import discord
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$adios'):
        await message.channel.send(f"👋 ¡Adios {message.author.mention}! Que tengas un buen dia. 👋")

    elif message.content.startswith("$hola"):
        await message.channel.send(f'¡Hola {message.author.mention}! ¿Cómo estás? 😊')

    elif message.content.startswith("$chiste"):
        chistes = [
            "¿Qué le dice una impresora a otra? - ¡Esa hoja es tuya o es impresión mía!",
            "¿Cómo se despiden los químicos? - Ácido un placer.",
            "¿Qué le dijo el cero al ocho? - ¡Qué buen cinturón!",
            "¿Cuál es el café más peligroso del mundo? - El ex-preso."
        ]
        response = random.choice(chistes)
        await message.channel.send(response)
    elif message.content.startswith("$moneda"):
        resultado = random.choice(["Cara", "Cruz"])
        await message.channel.send(f'La moneda cayó en: {resultado}')

    elif message.content.startswith("$adivina"):
        numero = random.randint(1, 10)
        await message.channel.send("Estoy pensando en un número entre 1 y 10. ¡Intenta adivinarlo!")

        def check(m):
            return m.author == message.author and m.content.isdigit()   

        try:
            guess = await client.wait_for("message", check=check, timeout=15.0)
            if int(guess.content) == numero:
                await message.channel.send("¡Correcto! Adivinaste el número.")
            else:
                await message.channel.send(f'¡Casi! El número era {numero}.')
        except:
            await message.channel.send("¡Ups! Se acabó el tiempo para adivinar.")

    

client.run("")  

#def flip_coin():
    #flip = random.randint(1, 2)
    #if flip == 1:
        #return "Cara"
    #else:
        #return "Sello"
