from llama_cpp import Llama
from googletrans import Translator

# プロンプトを記入
prompt = """
### Instruction:What is the height of Mount Fuji?
### Response:
"""
# ダウンロードしたModelをセット
llm = Llama(model_path="llama-2-7b-chat.ggmlv3.q8_0.bin")

# 生成実行
output = llm(prompt,max_tokens=500,temperature=0.1,stop=["Instruction:", "Input:", "Response:"],echo=True)

text = output["choices"][0]["text"].split("Response:\n", 1)[-1]

translator = Translator()
output_jp = translator.translate(text, src='en', dest='ja').text

print(output_jp)