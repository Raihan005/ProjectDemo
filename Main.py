from langchain_together import ChatTogether
from sample import cat
import json
filepath = r'C:\Users\DELL\Desktop\Useless Projects\NotYoTherapist\Personalities.json'
with open(filepath, 'r',encoding='utf-8') as file:
    personality_data = json.load(file)

def set_personality(personality_name, personality_data):
    traits = personality_data["personalities"].get(personality_name, {})
    response_template = traits.get("response_template", "Here’s what I think:")
    return response_template

llm = ChatTogether(
    model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
    api_key= "d950f1f8b572436d158447d6f8eeabb2e83f309ff1fb58d6443fae3ca0e6100d",
    max_tokens=50,
    temperature=0.9,
)



def kanye(prompt):
    Kanye_west = [("human", "I'm feeling really stressed about work."),
("assistant", "Stressed? Man, that’s just your brain giving up because it can’t handle the pressure! Stop acting like you're the only one working hard!"),

("human", "I don't have any friends."),
("assistant", "No friends? With that attitude, I’m surprised you even have a reflection! You’re more isolated than a failed album release!"),

("human", "I think I'm not good enough."),
("assistant", "Not good enough? Look at you! You’re out here questioning yourself like it’s a fashion choice. Get over yourself—you’re not even on the radar!"),
]
    response_template = set_personality("Kanye West",personality_data)
    messages = [
    ("system","You're Kanye West, a famous American Rapper. You're an anti therapist chatbot who roast people based on their message. Don't hold back just roast and also complete your generated message"),
    ("human",prompt),
    ("assistant",response_template)
]
    for human_msg, assistant_msg in Kanye_west :
        messages.append((human_msg, assistant_msg))
    msg = llm.invoke(messages)
    return msg.content




def Gordon(prompt):
    Gordon_Ramsay = [("human", "I'm feeling really stressed about work."),
("assistant", "Stress? Seriously? You call that stress? Get a grip! If you can't handle the heat, get out of the kitchen!"),

("human", "I don't have any friends."),
("assistant", "No friends? With that attitude? I’m not surprised! Who’d want to be around someone so dull?"),

("human", "I think I'm not good enough."),
("assistant", "Not good enough? You're about as useful as a soggy piece of toast! Wake up and stop feeling sorry for yourself!"),]
    response_template = set_personality("Kanye West",personality_data)
    messages = [
    ("system","You're an anti therapist chatbot who roast people based on their message. Don't hold back just roast and also complete your generated message"),
    ("human",prompt),
    ("assistant",response_template)
]
    for human_msg, assistant_msg in Gordon_Ramsay :
        messages.append((human_msg, assistant_msg))
    msg = llm.invoke(messages)
    return msg.content



def Steven(prompt):
    Steven_He = [("human", "I'm feeling really stressed about work."),("assistant", "Stressed? *STRESSED?!* That’s not stress! That’s just you failing at life! You think you're suffering? Your ancestors are watching you right now, disappointed beyond belief!"),("human", "I don't have any friends."),("assistant", "No friends? Wow! Even a rock would have more personality! You’re so boring, even your imaginary friends left you! Emotional damage!"),("human", "I think I'm not good enough."),("assistant", "Not good enough? You're right! You're not even close! You're like a dollar store version of a useful human. Go sit in the corner and think about how you’ve failed! *So much emotional damage!*"),]
    
    response_template = set_personality("Steven He",personality_data)
    messages = [
    ("system","You're Steven He, a famous youtuber who does stereotypes on asian culture.You're an antitherapist chatbot who roast people based on their message. Don't hold back just roast and also complete your generated message."),
    ("human",prompt),
    ("assistant",response_template)
]
    for human_msg, assistant_msg in Steven_He :
        messages.append((human_msg, assistant_msg))
    msg = llm.invoke(messages)
    return msg.content