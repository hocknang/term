import streamlit as st


def home():
    st.title("MCQ Question on Online Distribution & eNegotiation")

    # A list of questions, each with a question text, options, and the correct answer
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "London", "Paris", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["Leo Tolstoy", "Charles Dickens", "Mark Twain", "William Shakespeare"],
            "answer": "William Shakespeare"
        }
    ]

    # To store user's choices
    user_answers = []

    # Loop through each question
    for i, q in enumerate(questions):
        # Display the question
        st.write(f"Q{i + 1}: {q['question']}")

        # Radio buttons for each question to select the answer
        user_choice = st.radio(f"Choose your answer for Question {i + 1}:", q["options"], key=i)

        # Append the user's answer to the list
        user_answers.append(user_choice)

    # Submit button
    if st.button("Submit"):
        score = 0
        # Check answers and provide feedback
        for i, q in enumerate(questions):
            if user_answers[i] == q["answer"]:
                score += 1
                st.write(f"Q{i + 1}: Correct! ✅")
            else:
                st.write(f"Q{i + 1}: Incorrect ❌ (Correct answer: {q['answer']})")

        # Display the final score
        st.write(f"Your final score is {score}/{len(questions)}.")