from src.backend.polli.conversation import *
import src.backend.polli.models as models
# client = Client()
# # print(
# #     json.dumps(client.available_models(), ensure_ascii=False, indent=2)
# # )

# print(
#     client.media_generate(
#         messages = [
#             Message(text="Привет, кто ты?", role="user")
#         ],
#         system_prompt="Ты асистент на базе ИИ, отвечай и помогай пользователю",
#         model="gpt-4o-mini",
#         seed=123456789
#     ).text
# )
if __name__ == "__main__":

    conversation = Conversation()

    status, ans = conversation.ask_text(
        "Скажи 0, если ничего не помнишь, и прибавь к предыдущему числу 1 если в переписке есть другое число от тебя",
        model=models.gpt_4o_mini,
        files = [],
        images = [],
    )

    print(ans.text)

    # status, ans = conversation.ask_text(
    #     "Скажи 0, если ничего не помнишь, и прибавь к предыдущему числу 1 если в переписке есть другое число от тебя",
    #     model="gpt-4o-mini",
    #     files = [],
    #     images = [],
    # )

    # print(ans.text)

    status = conversation.ask_img(
        conversation.ask_text("Переведи на английский и не говори ничего более: Изображение ламборгини на тротуаре перед дворцом в лондоне")[1].text,
        img_model=imgmodels.flux_realism,
        out_file="./lamborgini.jpg",
        width=1280,
        height=1280,
        enhance=True
    )