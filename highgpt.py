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
        purposes = "This is where you write your main text answer or image description if you are using `image_gen`",
        description = "The tool is needed to communicate the TEXT result of your activity to the user"
    )

    image_gen = hhg.Tool(
        name = "image_gen",
        use_requirements = "Used when you want to generate an image",
        purposes = "This tool is used to generate images based on provided requests",
        description = "The tool is needed to create static visual content. It streectly need to be set to only English. It is a prompt for image generation, be precise. Do not include words \"Generate an image ...\" in the request",
        subtools=[
            hhg.SubTool(
                name = "image_resolution",
                description = "Resolution of the image. If prompt does not specify it, then it should be 1280x1280",
                data_type = "tuple[number, number]",
                use_requirements = "Used **always**, even if prompt does not specify it"
            )
        ]
    )

    chain_next = hhg.Tool(
        name = "answer_chain",
        use_requirements = "Used if you need additional processing of your current answer or if you need to develop your answer, use tools to process already used tools",
        purposes = "This tool is used to chain answers together",
        description = "The tool is needed to create response based on provided answers"
    )

    system_prompt = hhg.Compiler.compile(
        base = basics,
        tools = [answer, image_gen, chain_next]
    )
    
    conversation.system_query = system_prompt

    with open("./sysprompt.txt", 'w') as f:
        f.write(conversation.system_query)

    status, ans = conversation.ask_text(
        hhg.Salt.add_salt("Сгенерируй лого на подобии трех прямоугольников, где по середение один выше других, он серый, два по бокам оранжевые, фон белый, а под фигурой небольшая тень. Все 3 прямоугольника соединены побокам"),
        model=models.deepseek_r1_full,
    )

    @realTools.callback("image_gen")
    def img_handler(img_arg: dict):
        main_prompt = img_arg["main"]
        resolution = tlr.ArgParser.parse(img_arg["image_resolution"], "tuple[number, number]")

        status = conversation.ask_img(
            prompt=main_prompt,
            width = resolution[0],
            height = resolution[1],
            img_model=imgmodels.flux_pro
        )

        print(status)
    
    realTools.run(ans.text)