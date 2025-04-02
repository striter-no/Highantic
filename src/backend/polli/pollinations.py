import requests, urllib
import base64
import aiohttp
import asyncio

class Message:
    @staticmethod
    def from_g4f(message):
        return Message(text=message["content"], role=message["role"])

    def __init__(self, text: str, role: str, image_paths: list[str] = []):
        self.text = text
        self.image_paths = image_paths
        self.role = role

    def get_image_info(self, image_path):
        image_format = image_path.split('.')[-1].lower()
        if image_format not in ['jpeg', 'jpg', 'png', 'gif', 'webp']:
            print(f"Warning: Potentially unsupported image format '{image_format}'. Assuming jpeg.")
            image_format = 'jpeg' # Default or make more robust
        with open(image_path, "rb") as image_file:
            return image_format, base64.b64encode(image_file.read()).decode('utf-8')

    def compile(self, g4f_compatibility = False):
        content = []

        if self.text:
            content.append({"type": "text", "text": self.text})
        
        if not g4f_compatibility:
            for img in self.image_paths:
                imgform, imgdata = self.get_image_info(img)
                content.append({"type": "image", "image_url": {"url": f"data:image/{imgform};base64,{imgdata}"}})

        return {
            "role": self.role,
            "content": content
        }
        
class AsyncClient:
    @staticmethod
    async def image_available_models() -> list[dict[str, str]]:
        url = "https://image.pollinations.ai/models"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}) as response:
                    response.raise_for_status()
                    return await response.json()
            except aiohttp.ClientError as e:
                print(f"Error fetching vision models: {e}")
                return []

    @staticmethod
    async def available_models() -> list[dict[str, str]]:
        url = "https://text.pollinations.ai/models"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}) as response:
                    response.raise_for_status()
                    return await response.json()
            except aiohttp.ClientError as e:
                print(f"Error fetching text models: {e}")
                return []

    @staticmethod
    async def text_to_speach(
        prompt: str,
        voice: str,
        out_file: str
    ):
        prompt = """[{\n    "role": "system",\n    "content": "You are the system for service of text to speach. Please say text naturally and without accents"\n},\n{\n    "role": "user",\n    "content": "{prompt}"\n},\n{\n    "role": "assistant",\n    "content": "{prompt}"\n},\n{\n    "role": "user",\n    "content": "Повтори свой ответ"\n}]""".replace("{prompt}", prompt)

        url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt)}?model=openai-audio&voice={voice}"
        response = requests.get(url)
        if 'audio/mpeg' in response.headers.get('Content-Type', ''):
            with open(out_file, 'wb') as f:
                f.write(response.content)
            return True, "success"
        else:
            return False, "failed-to-fetch"

    @staticmethod
    async def speach_to_text(
        audio_path: str
    ):
        with open(audio_path, "rb") as audio_file:
            enc = base64.b64encode(audio_file.read()).decode('utf-8')

        audio_format = audio_path.split('.')[-1].lower()
        supported_formats = ['mp3', 'mp4', 'mpeg', 'mpga', 'm4a', 'wav', 'webm'] # Check API/OpenAI docs for current list
        if audio_format not in supported_formats:
            print(f"Warning: Potentially unsupported audio format '{audio_format}'. Check API documentation.")

        payload = {
            "model": "openai-audio",
            "private": "true",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Trancribe this audio"},
                        {
                            "type": "input_audio",
                                "input_audio": {
                                "data": enc,
                                "format": audio_format
                            }
                        }
                    ]
                }
            ]
        }

        url = "https://text.pollinations.ai/openai"
        headers = {"Content-Type": "application/json"}

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, params=payload, headers=headers, json=payload) as response:
                    response.raise_for_status()
                    result = await response.json()
                    transcription = result.get('choices', [{}])[0].get('message', {}).get('content')
                    return True, transcription
            except aiohttp.ClientError as e:
                return False, "failed-to-proceeve"

    @staticmethod
    async def image_generate(
        prompt: str,
        model: str = "flux",
        seed: int = -1,
        width: int = 1280,
        height: int = 1280,
        enhance: bool = False
    ) -> tuple[bool, str]:
        
        payload = {
            "model": model,
            "width": width,
            "height": height,
            "seed": seed,
            "enhance": "true" if enhance else "false",
            "nologo": "true",
            "cached": "false"
        }
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, params=payload) as response:
                    response.raise_for_status()
                    return True, str(response.url)
            except aiohttp.ClientError as e:
                return False, "failed-to-gen"

    @staticmethod
    async def media_generate(
        messages: list[Message],
        system_prompt: str,
        model: str = "gpt-4",
        seed: int | None = None
    ) -> tuple[bool, Message]:
        url = "https://text.pollinations.ai/openai"
        headers = {"Content-Type": "application/json"}

        payload = {
            "model": model,
            "messages": [msg.compile() for msg in messages],
            "system": system_prompt,
            "seed": seed,
            "private": "true",
            "cached": "false"
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, headers=headers, json=payload) as response:
                    response.raise_for_status()
                    data = await response.json()
                    return True, Message(
                        text=data["choices"][0]["message"]["content"],
                        role=data["choices"][0]["message"]["role"]
                    )
            except aiohttp.ClientError as e:
                print(f"Error analyzing local image: {e}")
                return False, Message("", "")

class Client:
    @staticmethod
    def image_available_models() -> list[dict[str, str]]:
        return asyncio.run(AsyncClient.image_available_models())

    @staticmethod
    def available_models() -> list[dict[str, str]]:
        return asyncio.run(AsyncClient.available_models())

    @staticmethod
    def text_to_speach(
        prompt: str,
        voice: str,
        out_file: str
    ):
        return asyncio.run(AsyncClient.text_to_speach(prompt, voice, out_file))

    @staticmethod
    def speach_to_text(
        audio_path: str
    ):
        return asyncio.run(AsyncClient.speach_to_text(audio_path))

    @staticmethod
    def image_generate(
        prompt: str,
        model: str = "flux",
        seed: int = -1,
        width: int = 1280,
        height: int = 1280,
        enhance: bool = False
    ) -> tuple[bool, str]:
        return asyncio.run(AsyncClient.image_generate(prompt, model, seed, width, height, enhance))

    @staticmethod
    def media_generate(
        messages: list[Message],
        system_prompt: str,
        model: str = "gpt-4",
        seed: int | None = None
    ) -> tuple[bool, Message]:
        return asyncio.run(AsyncClient.media_generate(messages, system_prompt, model, seed))