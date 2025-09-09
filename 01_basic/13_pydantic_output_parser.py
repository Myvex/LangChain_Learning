# 13_pydantic_output_parser.py
# 说明：演示 LangChain + PydanticOutputParser，生成并解析结构化笑话
# 运行方式：python 01_basic/13_pydantic_output_parser.py

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field,validator
from typing import List

model = OpenAI(openai_api_key="")

class Joke(BaseModel):
    setup: str=Field(description="question to set up a joke")
    punchline:str=Field(description="answer to resolve the joke")

    @validator("setup")
    def question_ends_with_question_mark(cls,field)
        if field[-1] != "?":
            raise ValueError("Badly formed question!")
        return field

joke_query = "Tell me a joke."

parser=PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Answer the user query.\n {format_instructions} \n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions":
    parser.get_format_instructions()},
)

_input = prompt.format_prompt(query=joke_query)

output = model(_input.to_string())

joke=parser.parse(output)

Joke(setup='Why did the chicken cross the road?', punchline = To get to the other side!)