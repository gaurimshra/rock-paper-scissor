import streamlit as st
import random

st.title("🪨📄✂️ Rock Paper Scissors")

choices = ["rock", "paper", "scissor"]

# Initialize scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0

user_choice = st.selectbox("Choose one:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)

    st.write(f"**You chose:** {user_choice}")
    st.write(f"**Computer chose:** {computer_choice}")

    if user_choice == computer_choice:
        st.info("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        st.success("🎉 You win this round!")
        st.session_state.user_score += 1
    else:
        st.error("💻 Computer wins this round!")
        st.session_state.computer_score += 1

st.divider()
st.write(
    f"### 📊 Score\n"
    f"- You: {st.session_state.user_score}\n"
    f"- Computer: {st.session_state.computer_score}"
)
