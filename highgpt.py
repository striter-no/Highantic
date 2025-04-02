from src.backend.polli.conversation import *
import src.highend.gpt_chain as hhg
import src.highend.tools_real as tlr
import json

if __name__ == '__main__':
    basics = hhg.BasicToolSpec()
    realTools = tlr.RealTools()
    conversation = Conversation()

    answer = hhg.Tool(
        name = "answer",
        use_requirements = "Used **always**, even if prompt does not specify it",
        purposes = "This is where you write your main answer",
        description = "The tool is needed to communicate the result of your activity to the user"
    )

    image_gen = hhg.Tool(
        name = "image_gen",
        use_requirements = "Used when you want to generate an image",
        purposes = "This tool is used to generate images based on provided requests",
        description = "The tool is needed to create static visual content. It streectly need to be set to only English. It is a prompt for image generation, be precise",
        subtools=[
            hhg.SubTool(
                name = "image_resolution",
                description = "Resolution of the image. If prompt does not specify it, then it should be 1280x1280",
                data_type = "tuple[number, number]",
                use_requirements = "Used **always**, even if prompt does not specify it"
            )
        ]
    )

    system_prompt = hhg.Compiler.compile(
        base = basics,
        tools = [answer, image_gen]
    )
    
    conversation.system_query = system_prompt

    status, ans = conversation.ask_text(
        hhg.Salt.add_salt("Сгенерируй изображение машины"),
        model=models.deepseek_r1_full,
    )

    @realTools.callback("image_gen")
    def img_handler(img_arg: dict):
        main_prompt = img_arg["main"]
        resolution = tlr.ArgParser.parse(img_arg["image_resolution"], "tuple[number, number]")

        status = conversation.ask_img(
            prompt=main_prompt,
            width = resolution[0],
            height = resolution[1]
        )
    
    realTools.run(ans.text)