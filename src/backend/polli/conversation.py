from typing import Any

import src.backend.polli.pollinations as pls
import src.backend.polli.models as models
import src.backend.polli.imgmodels as imgmodels
import requests, random, os

def _get_images(paths: list[str]) -> list[tuple[bytes, str]]:
    out = []
    for path in paths:
        with open(path, 'rb') as f:
            out.append([f.read(), os.path.basename(path)])

    return out

def _get_files(paths: list[str]) -> str:
    if len(paths) == 0:
        return "No files are attached"
    content = "There are files with names and contents of this:\n"
    for path in paths:
        with open(path) as f:
            content += f"File: {os.path.basename(path)}\n\n" + ("=" * 20) + f'\n{f.read()}\n' + ("=" * 20) + '\n\n'
    
    return content

def download_image(url: str, path: str) -> bool:
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        return True
    return False

class Conversation:
    def __init__(self):
        self.messages: list[pls.Message] = []
        self.system_query = ""

    # Text request
    def ask_text(
        self, 
        prompt: str,
        files: list[str] = [],
        images: list[str] = [],

        model: str | Any = "gpt-4o-mini",
        seed = None 
    ) -> tuple[bool, pls.Message]:
        self.messages.append(pls.Message(f"{_get_files(files)}User Prompt: {prompt}", "user", image_paths=images))
        status, resp = pls.Client.media_generate(
            self.messages,
            self.system_query,
            model = model().name if not isinstance(model, str) else model,
            seed = seed if seed else random.randint(0, 9999999)
        )
        if status:
            self.messages.append(resp)
        
        return status, resp

    # Image generation request
    def ask_img(
        self, 
        prompt: str,
        width = 1280,
        height = 720,
        seed = None,
        enhance: bool = False,

        img_model: str | Any = "flux-dev",
        out_file: str = "./temp.jpg",
    ) -> bool:
        self.messages.append(pls.Message(f"New photo generaion by prompt {prompt}", "user"))
        status, url = pls.Client.image_generate(
            prompt = prompt,
            width = width,
            height = height,
            model = img_model().name if not isinstance(img_model, str) else img_model,
            seed = seed if seed else random.randint(0, 9999999),
            enhance=enhance
        )
        if status:
            self.messages.append(pls.Message(f"Image saved to {out_file}", "assistant"))
            download_image(url, out_file)
        else:
            self.messages.append(pls.Message(f"Image was failed to generate", "assistant"))

        return status

    # Speech synth request
    def tts(
        self, 
        prompt: str,

        voice: str = "ash",
        out_file: str = "./temp.wav"
    ) -> tuple[bool, str]:
        return pls.Client.text_to_speach(
            prompt = prompt,
            out_file = out_file,
            voice = voice
        )

    # Speech recognition request
    def stt(
        self,
        audio_path: str
    ) -> tuple[bool, str]:
        return pls.Client.speach_to_text(
            audio_path = audio_path
        )