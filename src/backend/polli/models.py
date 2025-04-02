class gpt_4o_mini:
    def __init__(self):
        
        self.name = "gpt_4o_mini"
        self.polli_allias = "openai"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class gpt_4o:
    def __init__(self):
        
        self.name = "gpt_4o"
        self.polli_allias = "openai-large"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class o3_mini:
    def __init__(self):
        
        self.name = "o3_mini"
        self.polli_allias = "openai-reasoning"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class qwen_2_5_coder_32B:
    def __init__(self):
        
        self.name = "qwen_2.5_coder_32B"
        self.polli_allias = "qwen-coder"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class llama_3_3_70B:
    def __init__(self):
        
        self.name = "llama_3.3_70B"
        self.polli_allias = "llama"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class mistral_small_3:
    def __init__(self):
        
        self.name = "mistral_small_3"
        self.polli_allias = "mistral"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class unity_mistral_large:
    def __init__(self):
        
        self.name = "unity_mistrallarge",
        self.polli_allias = "unity"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }
        self.censored=False

class midijourney:
    def __init__(self):
        
        self.name = "midijourney"
        self.polli_allias = "midijourney"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class rtist:
    def __init__(self):
        
        self.name = "rtist"
        self.polli_allias = "rtist"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class searchgpt:
    def __init__(self):
        
        self.name = "searchgpt"
        self.polli_allias = "searchgpt"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class evil:
    def __init__(self):
        
        self.name = "evil"
        self.polli_allias = "evil"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }
        self.censored=False

class deepseek_r1_distill_qwen_32B:
    def __init__(self):
        
        self.name = "deepseek_r1_distill_qwen_3B",
        self.polli_allias = "deepseek-reasoning"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class deepseek_r1_llama_70B:
    def __init__(self):
        
        self.name = "deepseek_r1_llama_70B"
        self.polli_allias = "deepseek-reasoning-large"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class llama_3_1_8B_instruct:
    def __init__(self):
        
        self.name = "llama_3.1_8B_instrct",
        self.polli_allias = "llamalight"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class phi_4_instruct:
    def __init__(self):
        
        self.name = "phi_4_instrct",
        self.polli_allias = "phi"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class llama_3_2_11B_vision:
    def __init__(self):
        
        self.name = "llama_3.2_11B_vision"
        self.polli_allias = "llama-vision"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class pixtral_12B:
    def __init__(self):
        
        self.name = "pixtral_12B"
        self.polli_allias = "pixtral"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class gemini_2_0_flash:
    def __init__(self):
        
        self.name = "gemini_2.0_flah",
        self.polli_allias = "gemini"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": True,
        }
        self.outputs = {
            "text": True,
            "images": True,
            "audio": True
        }

class gemini_2_0_flash_thinking:
    def __init__(self):
        
        self.name = "gemini_2.0_flash_thinkin",
        self.polli_allias = "gemini-reasoning"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": True,
        }
        self.outputs = {
            "text": True,
            "images": True,
            "audio": True
        }

class hormoz_8b:
    def __init__(self):
        
        self.name = "hormoz_8b"
        self.polli_allias = "hormoz"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class hypnosis_tracy_7B:
    def __init__(self):
        
        self.name = "hypnosis_tracy_7B"
        self.polli_allias = "hypnosis-tracy"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class deepseek_v3:
    def __init__(self):
        
        self.name = "deepseek_v3"
        self.polli_allias = "deepseek"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class deepseek_r1_full:
    def __init__(self):
        
        self.name = "deepseek_r1_full"
        self.polli_allias = "deepseek-reasoning"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class mistral_sur:
    def __init__(self):
        
        self.name = "mistral_sur"
        self.polli_allias = "sur"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }

class llama_uncensored:
    def __init__(self):
        
        self.name = "llama_scaleway_uncensoed",
        self.polli_allias = "llama-scaleway"
        self.inputs = {
            "text": True,
            "images": False,
            "audio": False,
        }
        self.outputs = {
            "text": True,
            "images": False,
            "audio": False
        }
        self.censored=False

class gpt_4o_audio:
    def __init__(self):
        
        self.name = "gemini_2.0_flash"
        self.polli_allias = "openai-audio"
        self.inputs = {
            "text": True,
            "images": True,
            "audio": True,
        }
        self.outputs = {
            "text": True,
            "images": True,
            "audio": True
        }