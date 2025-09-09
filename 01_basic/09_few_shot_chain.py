# 09_few_shot_chain.py
# 说明：Few‑Shot 反义词接龙示例，演示如何使用 FewShotPromptTemplate + LLMChain
# 运行方式：python 01_basic/09_few_shot_chain.py

from langchain import PromptTemplate, FewShotPromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# 1️⃣ 训练示例
examples = [
    {"input": "高", "output": "矮"},
    {"input": "长", "output": "短"},
    {"input": "大", "output": "小"},
]

# 2️⃣ 示例模板
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="""
    词语：{input}
    反义词：{output}
    """
)

# 3️⃣ Few‑Shot Prompt
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="来玩一个反义词接龙游戏，我说词语你说它的反义词\n",
    suffix="现在轮到你了。词语：{input}\n 反义词：",
    input_variables=["input"],
)

# 4️⃣ LLMChain
chain = LLMChain(
    llm=OpenAI(openai_api_key="YOUR_OPENAI_API_KEY"),
    prompt=few_shot_prompt
)

# 5️⃣ 运行
print(chain.run("冷"))   # 期望输出类似 “热”

# 最终prompt
# 来玩一个反义词接龙游戏，我说词语你说它的反义词
# 词语：高
# 反义词：矮

# 词语：长
# 反义词：短

# 词语：大
# 反义词：小

# 现在轮到你了。词语：冷
# 反义词：
