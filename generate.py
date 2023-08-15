from llama_cpp import Llama

# プロンプトを記入
prompt = """
### Instruction:What is the height of Mount Fuji?
### Response:
"""
# ダウンロードしたModelをセット
llm = Llama(model_path="llama-2-7b-chat.ggmlv3.q8_0.bin")

# 生成実行
output = llm(prompt,max_tokens=500,temperature=0.1,stop=["Instruction:", "Input:", "Response:"],echo=True)

print(output)