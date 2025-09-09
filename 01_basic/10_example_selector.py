# 10_example_selector.py
# 说明：演示 LangChain 的四种示例选择器（Length、MRR、NGram、Semantic）
# 运行方式：python 01_basic/10_example_selector.py

from langchain.prompts.examples_selector import (
    LengthBasedExampleSelector,
    MaxMarginalRelevanceExampleSelector,
    NGramOverlapExampleSelector,
    SemanticSimilarityExampleSelector,
)
from langchain import PromptTemplate, FewShotPromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS, Chroma

examples = [
    {"input": "高", "output": "矮"},
    {"input": "长", "output": "短"},
    {"input": "大", "output": "小"},
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="""
    词语：{input}
    反义词：{output}
    """
)

#基于长度的选择
examples_selector_1=LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=25,
)
#最大边际相关性选择器
examples_selector_2=MaxMarginalRelevancexampleSelector.from_examples(
    examples,
    OpenAIEmbeddings(), # 用于生成语义相似测量的嵌入类
    FAISS, #用于存储嵌入类和执行相似性搜索
    k=2, #需要生成的示例数量
)
#基于n-gram重叠度
examples_selector_3=NGramOverlapExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    threshold=1.0, #设定示例选择器的停止阈值
)
#基于相似性
examples_selector_4=SemanticSimilarityExampleSelector.from_examples(
    examples,
    OpenAIEmbeddings(), # 用于生成语义相似测量的嵌入类
    Chroma, #用于存储嵌入类和执行相似性搜索
    k=1, #需要生成的示例数量
)

examples_selector_prompt = FewShotPromptTemplate(
    examples_selector=examples_selector_1,
    example_prompt=example_prompt,
    prefix="来玩一个反义词接龙游戏，我说词语你说它的反义词\n",
    suffix="现在轮到你了。词语：{input}\n 反义词：",
    input_variables=["input"],
)

examples_selector_prompt.format(input="好")

