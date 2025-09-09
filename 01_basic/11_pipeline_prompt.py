# 11_pipeline_prompt.py
# 说明：演示 LangChain 的 PipelinePromptTemplate，展示如何将多个子 Prompt 组装成一个最终 Prompt
# 运行方式：python 01_basic/11_pipeline_prompt.py

from langchain import PipelinePromptTemplate

prompt = PromptTemplate(template="{foo}{bar}",input_variables=["foo","bar"])
partial_prompt=prompt.partial(foo="foo")
print(partial_prompt.format(bar="baz"))

full_template = """
    {introduction}
    {example}
    {start}
    """
full_prompt = PromptTemplate.from_template(full_template)
input_prompts = [
    {"introduction",introduction_prompt},
    {"example",example_prompt},
    {"start",start_prompt}
]
pipeline_prompt=PipelinePromptTemplate(final_prompt=full_prompt,
    pipeline_prompts=input_prompts)