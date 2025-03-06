import streamlit as st
import google.generativeai as genai
from fpdf import FPDF
import requests  # For calling the second API for explanation

# Set up the first Gemini API Key for practice questions
genai.configure(api_key="AIzaSyCjjFyXDIbnjOdOSLuj0W3trl3eCXdkQ6g")


def generate_practice_questions(topic, difficulty, num_questions):
    prompt = f"Generate {num_questions} {difficulty} level math practice questions on {topic}. Provide questions in a numbered list format without extra space in lines and other stuff. and give only question not other stuff only Q "
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text


def evaluate_answers(questions, user_answers):
    prompt = f"Check the following answers for these math questions:\n\nQuestions:\n{questions}\n\nUser Answers:\n{user_answers}\n\nProvide correct answers and feedback in a clear format."
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content(prompt)
    return response.text


def get_explanation_from_new_api(question):
    url = "https://api.newapi.com/explanation"  # Replace with the actual URL
    headers = {
        "Authorization": "Bearer AIzaSyByz2fCoMLCiLP1T8e2UFlnNG96s7RlzSE"
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

    if st.button("Generate Practice Questions"):
        st.write("Generating questions...")
        questions_text = generate_practice_questions(topic, difficulty, num_questions)
        st.session_state["questions"] = questions_text.strip().split("\n")
        st.session_state["answers"] = ["" for _ in range(len(st.session_state["questions"]))]

    if st.session_state["questions"]:
        st.write(f"### Practice Questions for {topic} ({difficulty}):")
        for i, question in enumerate(st.session_state["questions"]):
            st.write(f"**Q{i + 1}:** {question}")
            st.session_state["answers"][i] = st.text_input(f"Your answer for Q{i + 1}:", key=f"ans_{i}")

        if st.button("Submit Answers"):
            st.write("Submitting answers for evaluation...")
            feedback = evaluate_answers("\n".join(st.session_state["questions"]), st.session_state["answers"])
            feedback_lines = feedback.strip().split("\n")
            st.write("### Feedback & Evaluation:")

            for i, question in enumerate(st.session_state["questions"]):
                correct_answer = feedback_lines[i * 3].split(":")[-1].strip() if i * 3 < len(feedback_lines) else "N/A"
                user_answer = st.session_state["answers"][i]
                is_correct = "✅ Correct" if correct_answer.lower() == user_answer.lower() else "❌ Incorrect"

                st.write(f"**Q{i + 1}:** {question}")
                st.write(f"**Correct Answer:** {correct_answer}")
                st.write(f"**Your Answer:** {user_answer}")
                st.write(f"**Result:** {is_correct}")

                with st.expander(f"Click to view the solution and explanation for Q{i + 1}"):

                    # When clicking the "Explain" button, fetch explanation from new API
                    if st.button(f"Generate Explanation for Q{i + 1}", key=f"explain_{i}"):
                        explanation = get_explanation_from_new_api(question)
                        st.write(explanation)

                st.write("---")

    if st.button("Download Questions as PDF"):
        file_name = create_pdf("\n".join(st.session_state["questions"]))
        with open(file_name, "rb") as pdf_file:
            st.download_button("Download PDF", pdf_file, file_name=file_name)


if __name__ == "__main__":
    practice_test()
