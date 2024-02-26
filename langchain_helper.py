# from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import AgentType
from langchain.agents import initialize_agent

from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(game,countryName):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables = ['game','countryName'],
        template = "Give me a top 5 {game} team names in country {countryName}"
    )

    # name=llm("give me  top 5 basketball team names")
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="club_name")
    response = name_chain.invoke({'game': game, 'countryName': countryName})

    return response
def langchain_agent():
    llm=OpenAI(temperature=0.7)
    tools=load_tools(["wikipedia", "llm-math"], llm=llm)
    agent= initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

    result=agent.run("what is the Average age of a cat? Multiply the age by 3")
    print(result)

if __name__ == "__main__":
    langchain_agent()
    # print(generate_pet_name("football"))


