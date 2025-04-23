import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# Function for creating the header
def header():

    st.image('mathlab.png')


def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


# Sidebar function with icons
def sidebar():
    st.sidebar.title("📌 Navigation")
    st.sidebar.markdown("Welcome to Math-Lab")
    st.sidebar.image(r"C:\\projects\\temppycharm\\streamlit\\mathlab.png", width=200)
    options = ["🏠 Home", "📞 Contact Us", "ℹ️ About MathLab", "💻 Source Code & Tech"]
    selection = st.sidebar.radio("Select Option", options)
    return selection


def main_dashboard():
    st.markdown("""
        <style>
            body {
                background-color: white;
            }
            .header {
                text-align: center;
                font-size: 35px;
                font-weight: bold;
                padding: 2px;
                color: #4CAF50;
                background-color: #ADD8E6;
                border-radius: 50px;
            }
        </style>
        """, unsafe_allow_html=True)

    image_path = r"C:\\projects\\temppycharm\\streamlit\\imgs\\logo.png"
    image = Image.open(image_path)

    st.markdown(
        '<div class="header">  MathLab Dashboard</div>'.format(
            image_to_base64(image)),
        unsafe_allow_html=True)
    st.title("🏠 Welcome to Math-lab")
    st.subheader("📘 Your go-to platform for education and resources.")
    st.markdown("""
        EduCare is an online educational platform that brings together cutting-edge tech and learning resources.
        - 🎯 Interactive Courses with real-world applications.
        - 🧑‍🏫 Expert Instructors from top universities and industries.
        - 📊 Data-driven Learning Paths to track progress.
        - 🌍 Community Support & Webinars to stay updated.
        - 🔥 Career Guidance and job interview preparation.
        - 🚀 Hands-on Projects to build your portfolio.
        - 🧑‍💻 Coding Challenges to sharpen your skills.
        - 🎓 Certification upon completion to enhance your resume.
        - 🕒 Flexible Scheduling to learn at your own pace.
    """)


def combined_info():
    st.title("ℹ️ About MathLab & Testimonials")
    st.markdown("""
    **Our Mission**: To create a platform that bridges the gap between traditional education and modern learning.
    - 🏆 Award-winning educational platform trusted by thousands.
    - 🤖 AI-powered Personalized Learning Experiences.
    - 📚 Course materials from reputed universities & industry experts.
    - 🌟 Recognized by major tech firms for skill development.
    - 🎓 Partnerships with top institutions for certifications.
    - 🚀 Hands-on projects to enhance learning.
    - 📈 Career-oriented roadmap to help students excel.
    """)



def contact_us():
    st.title("📞 Contact Us")
    st.markdown("Have any questions? Reach out to us.")

    with st.form(key='contact_form'):
        name = st.text_input("👤 Name")
        email = st.text_input("📧 Email")
        message = st.text_area("💬 Your Message")
        submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        st.success(f"Thank you {name}! Your message has been sent.")

    # Live Chat Section
    st.subheader("💬 Live Chat Support")
    st.markdown("Need quick help? Chat with our support team below.")

    chat_input = st.text_input("Type your message...")
    if st.button("Send"):
        st.markdown(f"**You:** {chat_input}")
        st.markdown("**Support:** We’ll respond to you shortly after our lunch break. 😊")


def source_code_tech():
    st.title("💻 Source Code & Tech")
    st.markdown("""
    ### Technologies Used:
    - **Python** 🐍: Core language for backend and ML tasks.
    - **Streamlit** 🚀: Fast and interactive UI development.
    - **Ai Agent** 🐳: Containerized deployments for scalability.
    - **FastAPI** ⚡: Modern API framework for fast performance.
    - **TensorFlow & PyTorch** 🧠: Machine learning model integrations.
    - **AWS & GCP** ☁️: Cloud hosting and storage solutions.
    - **Manim** 🗃️: Reliable relational animation creator.
    - **Bootstrap & Tailwind CSS** 🎨: UI and responsive design frameworks.
    """)




def footer():
    st.markdown("""
    <style>
        .footer {
            text-align: center;
            font-size: 12px;
            padding: 10px;
            color: white;
            background-color: #4CAF50;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="footer">All Rights Reserved - EduCare</div>', unsafe_allow_html=True)


def main():
    header()
    option = sidebar()

    if option == "🏠 Home":
        main_dashboard()
    elif option == "📞 Contact Us":
        contact_us()
    elif option == "ℹ️ About EduCare":
        combined_info()
    elif option == "📚 Course List":
        course_list()
    elif option == "💻 Source Code & Tech":
        source_code_tech()

    if option == "📚 Course List":
        course_stats()

    footer()


if __name__ == "__main__":
    main()
