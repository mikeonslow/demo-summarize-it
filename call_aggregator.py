from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.deepgram import deepgram_transcribe
import json
import sys

def main():
    print("starting application...")

    if len(sys.argv) > 1:
        audio_file_url = sys.argv[1]
        print(f"The audio file URL is: {audio_file_url}")
    else:
        print("No arguments were provided.")

    summary_template = """
    given the {information} about a conversation, I want you to tell me the main points of the conversation
    1. a short summary
    2. 1 key point that was the most important part of the conversation
    3. how many speakers were in the conversation
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    transription = deepgram_transcribe(audio_file_url)

    print("CALL SUMMARY")
    print(chain.run(information=transription))

if __name__ == "__main__":
    main()
