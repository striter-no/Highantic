import src.backend.async_gptraw as async_gpt
import src.backend.gptraw as gpt

class Conversation:
    def __init__(self):
        self.messages = []
        self.system_query = ""
        self.client = gpt.RawFunctions.get_client_obj()

    def new_message(self, message: str, msg_role: str):
        self.messages.append({
            "role": message,
            "content": msg_role
        })

    # Text request
    def ask_text(
        self, 
        prompt: str,
        files: list[str] = [],
        images: list[str] = [],

        model: str = "gpt-4o-mini",
        specified_provider = None 
    ) -> tuple[bool, str]:
        self.new_message(f"{gpt.RawFunctions._get_files(files)}User Prompt: {prompt}", "user")
        status, resp = gpt.RawFunctions.text_n_vision(
            self.client,
            model = model,
            provider = specified_provider,
            images = images,
            messages = self.messages
        )
        if status:
            self.new_message(resp, "assistant")
        
        return status, resp

    # Image generation request
    def ask_img(
        self, 
        prompt: str,
        width = 1280,
        height = 720,
        seed = None,
        n = 1,

        img_model: str = "flux-dev",
        out_file: str = "./temp.jpg",
        specified_provider = None
    ) -> bool:
        self.new_message(f"New photo generaion by prompt {prompt}")
        status, url = gpt.RawFunctions.imggen(
            self.client,
            model = img_model,
            provider = specified_provider,
            prompt = prompt,
            width = width,
            height = height,
            seed = seed,
            n = n
        )
        if status:
            self.new_message(f"Image saved to {out_file}", "assistant")
            gpt.RawFunctions.download_image(url, out_file)
        else:
            self.new_message(f"Image was failed to generate", "assistant")

        return status

    # Speech synth request
    def tts(
        self, 
        prompt: str,

        voice: str = "ash",
        out_file: str = "./temp.wav",
        specified_provider = None
    ) -> tuple[bool, str]:
        return gpt.RawFunctions.text_to_speach(
            self.client,
            provider = specified_provider,
            prompt = prompt,
            out_file = out_file,
            voice = voice
        )

    # Speech recognition request
    def stt(
        self,
        audio_file: str
    ) -> tuple[bool, str]:
        return gpt.RawFunctions.transcribe_speach(
            self.client,
            provider = "Microsoft_Phi_4",
            audio_file = audio_file
        )