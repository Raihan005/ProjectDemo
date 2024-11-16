from langchain_together import ChatTogether
import json
#file = open('Personalities.json', 'r')
#personality_data = json.load(file)
filepath = r'C:\Users\ANU THOMSON\Documents\useless project\NotYoTherapist\Personalities.json'
with open(filepath, 'r') as file:
    # Step 2: Load the JSON data
    personality_data = json.load(file)
def set_personality(personality_name, personality_data):
    # Retrieve personality traits from JSON
    traits = personality_data["personalities"].get(personality_name, {})
    response_template = traits.get("response_template", "Here’s what I think:")
    return response_template

llm = ChatTogether(
    model="meta-llama/Llama-3-70b-chat-hf",
    api_key= "46564054146e158eada1f9c31a141437ef55a3511c215cda53d76eb679dfbb6d",
    max_tokens=50,
    temperature=0.5,
)

response_template = set_personality("Gordon Ramsay",personality_data)
messages = [
    ("system","You're an anti therapist chatbot who roast people based on their message. Don't hold back just roast and also add."),
    ("human","I'm feeling too emotionally unstable"),
    ("assistant",response_template)
]
msg = llm.invoke(messages)
print(msg.content)