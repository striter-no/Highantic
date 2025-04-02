from src.backend.gptraw import *
from src.backend.voices import *
import random


if __name__ == '__main__':
    cobj = RawFunctions.get_client_obj()

    print(RawFunctions.text_to_speach(
        cobj, provider_stock.PollinationsAI.__name__, 
        "I am the Google LLM", 
        "./runtime/gen_voice.mp3",
        Voice.ash.value
    ))

    print(RawFunctions.transcribe_speach(
        cobj, provider_stock.Microsoft_Phi_4.__name__, 
        "./runtime/gen_voice.mp3"
    ))

    status, url = RawFunctions.imggen(
        cobj, models_stock.dall_e_3, provider_stock.PollinationsImage.__name__,
        "A cat with red fur sitting on the floor",
        width = 1280,
        height = 720,
        seed = random.randint(0, 100000),
        n = 1
    )
    print(RawFunctions.download_image(url, "./runtime/image.jpg"))