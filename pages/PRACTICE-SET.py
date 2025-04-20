import streamlit as st
import google.generativeai as genai
from fpdf import FPDF
import requests

# Set up Gemini API
genai.configure(api_key="AIzaSyCjjFyXDIbnjOdOSLuj0W3trl3eCXdkQ6g")  # Replace with your actual key


def generate_practice_questions(topic, difficulty, num_questions):
    prompt = f"Generate {num_questions} {difficulty} level math practice questions on {topic}. Provide questions in a numbered list format without extra space in lines and other stuff. and give only question not other stuff only Q "
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text


def evaluate_answers(questions, user_answers):
    prompt = f"""Check the following answers for these math questions:

Questions:
{questions}

User Answers:
{user_answers}

Provide correct answers and feedback in the following format:
Q1: Correct Answer: ...
User Answer: ...
Feedback: ...

Use this format for each question.
"""
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content(prompt)
    return response.text


def get_explanation_from_new_api(question):
    url = "https://api.newapi.com/explanation"  # Replace with the actual working URL
    headers = {
        "Authorization": "Bearer YOUR_SECOND_API_KEY"  # Replace with actual key
    }
    payload = {"question": question}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("explanation", "Explanation not found.")
    else:
        return "Failed to fetch explanation."


def create_pdf(questions, file_name="questions.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Math Practice Questions", ln=True, align='C')
    pdf.ln(10)
    for i, question in enumerate(questions.split("\n")):
        pdf.cell(200, 10, txt=f"Q{i + 1}: {question}", ln=True)
        pdf.ln(5)
    pdf.output(file_name)
    return file_name


def practice_test():
    st.image('practise.png')
    st.title("Math Practice Test Generator")

    topic = st.selectbox("Choose a math topic:", ["Algebra", "Geometry", "Calculus", "Trigonometry", "Probability"])
    difficulty = st.selectbox("Choose difficulty level:", ["Easy", "Medium", "Hard"])
    num_questions = st.number_input("Enter the number of questions:", min_value=1, max_value=20, value=5)

    if "questions" not in st.session_state:
        st.session_state["questions"] = []
        st.session_state["answers"] = []
        st.session_state["feedback"] = ""
        st.session_state["explanations"] = {}

    if st.button("Generate Practice Questions"):
        questions_text = generate_practice_questions(topic, difficulty, num_questions)
        questions = [q.strip() for q in questions_text.strip().split("\n") if q.strip()]
        st.session_state["questions"] = questions
        st.session_state["answers"] = ["" for _ in questions]
        st.session_state["feedback"] = ""
        st.session_state["explanations"] = {}

    if st.session_state["questions"]:
        st.subheader(f"Practice Questions for {topic} ({difficulty}):")
        for i, question in enumerate(st.session_state["questions"]):
            st.write(f"**Q{i + 1}:** {question}")
            st.session_state["answers"][i] = st.text_input(f"Your answer for Q{i + 1}:", key=f"ans_{i}")

        if st.button("Submit Answers"):
            joined_questions = "\n".join(st.session_state["questions"])
            joined_answers = "\n".join(st.session_state["answers"])
            feedback = evaluate_answers(joined_questions, joined_answers)
            st.session_state["feedback"] = feedback

        if st.session_state["feedback"]:
            st.subheader("Feedback & Evaluation:")
            feedback_lines = [line.strip() for line in st.session_state["feedback"].split("\n") if line.strip()]
            for i, question in enumerate(st.session_state["questions"]):
                st.write(f"**Q{i + 1}:** {question}")
                user_ans = st.session_state["answers"][i]
                correct_line = next((line for line in feedback_lines if f"Q{i + 1}:" in line), "")
                correct_answer = correct_line.split("Correct Answer:")[
                    -1].strip() if "Correct Answer:" in correct_line else "N/A"
                feedback_line = next((line for line in feedback_lines if
                                      "Feedback:" in line and f"Q{i + 1}" in feedback_lines[
                                          feedback_lines.index(line) - 2]), "No feedback found.")

                is_correct = "✅ Correct" if user_ans.lower() == correct_answer.lower() else "❌ Incorrect"
                st.write(f"**Your Answer:** {user_ans}")
                st.write(f"**Correct Answer:** {correct_answer}")
                st.write(f"**Result:** {is_correct}")
                st.write(f"**Feedback:** {feedback_line}")

                with st.expander(f"Click to view explanation for Q{i + 1}"):
                    if st.button(f"Generate Explanation for Q{i + 1}", key=f"explain_btn_{i}"):
                        explanation = get_explanation_from_new_api(question)
                        st.session_state["explanations"][i] = explanation

                    if i in st.session_state["explanations"]:
                        st.markdown(st.session_state["explanations"][i])

                st.markdown("---")

    if st.session_state.get("questions") and st.button("Download Questions as PDF"):
        file_name = create_pdf("\n".join(st.session_state["questions"]))
        with open(file_name, "rb") as pdf_file:
            st.download_button("Download PDF", pdf_file, file_name=file_name)


if __name__ == "__main__":
    practice_test()

