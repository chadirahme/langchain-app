import langchain_helper as lch
import streamlit as st
import textwrap

from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003")
llm("explain large language models in one sentence")

# st.title("Game Generator")
# animal_type = st.sidebar.selectbox("What is your Game?",( "Football", "BasketBall", "Hocky"))

# country_labels = {
#     "Football": "What country for Football",
#     "BasketBall": "What country is your BasketBall?",
#     "Hocky": "What country is your Hocky?"
# }

# country_name = st.sidebar.text_area(
#     label=country_labels[animal_type],
#     max_chars=15
# )

# if country_name:
#     response = lch.generate_pet_name(animal_type,country_name)
#     st.text(response['club_name'])
                                   
                                   

                                   
                                   

