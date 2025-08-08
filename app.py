import streamlit as st
import random
import datetime

# --- CHATBOT DATA AND LOGIC (from your original code) ---

gen_aff = [
    "You're not alone. I'm here to listen.",
    "It's okay to feel — all emotions are valid.",
    "Take a deep breath. You’re doing the best you can.",
    "Talking about it is a sign of strength, not weakness.",
    "Remember: this feeling is temporary. You're strong enough to handle it."
]

gen_res = {
    "hi": ["Hi, I'm doing good, how about you {name}?",
           "Good Morning {name}, How are you feeling?",
           "Hello {name}!",
           "How are you doing today {name}?",
           "What's on agenda today {name}?"],
    "hello": ["Hello {name}!", "Hi {name}! How can I help you today?", "Hello {name}, hope you're well."],
    "good morning": ["Good morning {name}! Hope your day is bright.", "Morning {name}, how are you today?"],
    "time": ["The time is " + datetime.datetime.now().strftime("%I:%M %p on %A, %B %d, %Y") + ".",
             "It's " + datetime.datetime.now().strftime("%I:%M %p") + " right now.",
             "Current Time: " + datetime.datetime.now().strftime("%H:%M:%S")],
    "you feeling": ["I can't feel emotions, but I'm here to help you understand yours!",
                    "I am a bot, so I'm doing great! How can I assist you?",
                    "I feel great and hopefully you do too!"],
    "you doing": ["I'm here to support you. What's on your mind?",
                  "I am doing great! Ready to listen.",
                  "I feel great and hopefully you do too!"],
    "thanks": ["You're welcome, {name}!", "Anytime, {name}. I'm here for you.", "Happy to help, {name}!"],
    "thank": ["You're welcome, {name}!", "No problem at all, {name}.", "Glad I could be here for you, {name}."],
    "feel better": ["I hope you feel better soon, {name}. 💖",
                    "Sending positive thoughts your way, {name}.", "Take care, {name}, you deserve kindness."]
}

emot = {
    "sad": [
        "I'm really sorry you're feeling sad. It's okay to feel this way.",
        "Let yourself feel. Sadness is part of healing.",
        "Let's breathe together: Inhale… hold… exhale… slowly.",
        "Even rainy days end. Brighter ones will come too."
    ],
    "anxious": [
        "Anxiety is tough. But you're tougher.",
        "Try a simple breathing exercise — inhale for 4, hold for 4, exhale for 4.",
        "It's okay not to have everything figured out right now.",
        "Focus on what you can control. Let go of what you can't."
    ],
    "angry": [
        "Anger often hides pain. It's valid, but let’s find healthy ways to express it.",
        "Try writing it out or talking it through. Suppressing anger can hurt more.",
        "Breathe. Walk. Stretch. Let the heat cool before reacting.",
        "You're allowed to pause and collect yourself."
    ],
    "lonely": [
        "Loneliness feels heavy. But you're not invisible — you matter.",
        "I'm here for you. You’re not alone in this moment.",
        "Maybe journaling how you feel will bring some clarity or peace.",
        "Would it help to connect with someone you trust, or a pet, or a memory?"
    ],
    "stressed": [
        "Stress piles up easily. Step by step, we’ll untangle it.",
        "A short break can reset your brain — try a 2-minute walk or slow breathing.",
        "You are capable, even if it doesn't feel like it right now.",
        "Let’s breathe together. 4 seconds in… 4 hold… 4 out… repeat."
    ],
    "overwhelmed": [
        "It can feel like too much, but you're not drowning — you're learning to swim.",
        "Break it down. One task at a time. You don’t have to do everything today.",
        "Rest is productive too. Please take care of you.",
        "You are enough even when you're doing nothing."
    ],
    "guilty": [
        "Guilt shows you care. But don't carry unnecessary blame.",
        "Everyone makes mistakes. Forgiveness includes yourself.",
        "Ask yourself: what would I say to a friend feeling this? Say that to you.",
        "Growth starts with awareness, not punishment."
    ],
    "grieving": [
        "Grief has no timeline. It’s okay to feel broken.",
        "Let yourself cry. It’s part of healing, not weakness.",
        "The pain may not go away, but you’ll grow around it.",
        "Honor their memory in small acts of love."
    ],
    "insecure": [
        "You are more than your doubts. You are unique, worthy, and enough.",
        "Try affirming: 'I accept myself just as I am.'",
        "You don’t have to compare. You’re on your own path.",
        "Even stars take time to shine."
    ],
    "hopeless": [
        "It's okay to not be okay. Hope may feel far, but it's not gone.",
        "🕯 Sometimes all you need is a flicker. Let’s light it together.",
        "Tomorrow holds possibilities you haven’t seen yet.",
        "Please talk to someone you trust. You matter more than you know."
    ],
    "happy": [
        "I’m so glad to hear that! Let’s savor this good moment.",
        "Happiness suits you — let it shine through.",
        "Capture this feeling and revisit it when things get tough.",
        "I hope more of these moments fill your days."
    ],
    "excited": [
        "That’s amazing! Your joy is contagious.",
        "Keep chasing what excites you — you’re on the right path.",
        "You’ve worked hard. Celebrate that!",
        "Hold on to this energy. It fuels dreams."
    ]
}

def get_res(user_input, name):
    """
    Generates a response based on the user's input.
    """
    msg = user_input.lower()

    # Check for exit commands first
    if any(keyword in msg for keyword in ["exit", "quit", "bye", "leave", "good bye"]):
        return "Always remember you're not alone. Thank you for opening up today. Take care!"

    # Check for general keywords
    for k, v in gen_res.items():
        if k in msg:
            chosen_response = random.choice(v)
            try:
                return chosen_response.format(name=name)
            except KeyError:
                return chosen_response

    # Check for emotion keywords
    for emotion, responses in emot.items():
        if emotion in msg:
            return random.choice(responses)

    # If no specific keyword is found, return a general affirmation
    return random.choice(gen_aff)

# --- STREAMLIT FRONTEND ---

st.set_page_config(page_title="Nix - Your Mental Health Friend", page_icon="💖")

st.title("💖 Nix - Mental Health Support Chatbot")
st.markdown("""
I'm Nix, your companion for navigating emotions. Feel free to share what's on your mind.
I'm here to listen without judgment.
*(Type 'bye' or 'quit' to end our chat.)*
""")

# Initialize session state for storing messages and the user's name
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'name' not in st.session_state:
    st.session_state.name = ""

# Function to handle name submission and start the chat
def start_chat():
    if st.session_state.name_input:
        st.session_state.name = st.session_state.name_input
        # Add a personalized welcome message
        welcome_message = random.choice(gen_res["hi"]).format(name=st.session_state.name)
        st.session_state.messages.append({"role": "assistant", "content": welcome_message})

# Check if the user's name has been entered yet
if not st.session_state.name:
    st.text_input("To start, could you please tell me your name?", key="name_input", on_change=start_chat)
else:
    # --- Main Chat Interface ---

    # Display existing messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input(f"How are you feeling today, {st.session_state.name}?"):
        # Add user message to chat history and display it
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get and display bot response
        with st.chat_message("assistant"):
            response = get_res(prompt, st.session_state.name)
            st.markdown(response)
        
        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})