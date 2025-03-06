import streamlit as st
import google.generativeai as genai
import subprocess
import os

# Configure Google Generative AI
genai.configure(api_key="AIzaSyAv_Hozwv3jAycftamoGYb1Gc0rMl5_j4c")
model = genai.GenerativeModel("gemini-1.5-flash")

# Set page config (Moved this above everything else)
st.set_page_config(page_title="Math Solution and Video Generator", layout="wide")

# Streamlit UI setup
st.image('quicksolve.png')
st.title("📚 Math Solution and Video Generator")
st.write("Enter a math equation, solve it step by step, and generate a video explanation!")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Chat history display
st.subheader("Chat History")
for chat in st.session_state["chat_history"]:
    st.markdown(f"**You:** {chat['user_input']}")
    st.markdown(f"**AI:** {chat['response']}")

# Input for math equation
st.subheader("Math Solver")
user_input = st.text_input("Enter a math equation or problem here:")

def clean_manim_code(raw_code):
    """Removes unnecessary prefix/suffix and formats the Manim script correctly."""
    cleaned_code = raw_code.strip().replace("```python", "").replace("```", "").strip()
    return cleaned_code

def handle_error_and_retry(error_message, manim_code, attempt_count):
    """Send the error back to the API to fix and retry."""
    st.error(f"Manim error: {error_message}")
    retry_prompt = (
        f"The following Manim script failed with an error:\n"
        f"{manim_code}\n"
        f"Error message:\n{error_message}\n"
        f"Please fix the issue and return only the corrected Manim script without any additional comments, explanations, or formatting markers."
    )
    response = model.generate_content([retry_prompt])
    corrected_code = clean_manim_code(response.text)

    # Save corrected code to file
    with open("generate_solution.py", "w") as script_file:
        script_file.write(corrected_code)

    return corrected_code, attempt_count + 1

# Solve Button
if st.button("Solve"):
    if user_input:
        try:
            # Request solution steps from Gemini
            response = model.generate_content([f"Provide step-by-step solution for: {user_input}"])
            solution_steps = response.text
            st.session_state["chat_history"].append({
                "user_input": user_input,
                "response": solution_steps,
            })
            st.markdown("### Solution Steps:")
            st.write(solution_steps)
        except Exception as e:
            st.error(f"Error solving the problem: {e}")

# Make Video Button
if st.button("Generate Video"):
    if user_input:
        try:
            # Request Python code for Manim animations
            prompt = (
                f"Create a Manim script that visualizes the solution for the following math problem: {user_input}.\n"
                f"Ensure the script follows these guidelines strictly:\n"
                f"- Use `MathTex` or `Tex` for LaTeX equations.\n"
                f"- Start with `from manim import *` and define a class inheriting from `Scene`.\n"
                f"- Include shapes, figures, and graphs where necessary.\n"
                f"- Use different colors, backgrounds, animations, and effects to enhance creativity.\n"
                f"- Add more movements and creative visuals to make the solution engaging.\n"
                f"- Return only the Manim script without any explanations, comments, or formatting markers."
            )
            response = model.generate_content([prompt])
            manim_code = clean_manim_code(response.text)

            # Save Manim code to generate_solution.py
            with open("generate_solution.py", "w") as script_file:
                script_file.write(manim_code)

            retry_limit = 3  # Increased retry attempts from 2 to 3
            attempts = 0
            progress_bar = st.progress(0)

            while attempts < retry_limit:
                st.write(f"Retry attempt: {attempts + 1}/{retry_limit}")
                try:
                    progress_bar.progress(int((attempts + 1) * 50 / retry_limit))

                    # Generate video using Manim
                    manim_command = ["manim", "-pql", "generate_solution.py"]
                    result = subprocess.run(manim_command, capture_output=True, text=True)

                    if result.returncode == 0:
                        progress_bar.progress(100)
                        video_path = "media/videos/generate_solution/1080p60/Scene.mp4"
                        if os.path.exists(video_path):
                            st.video(video_path)
                            break
                        else:
                            st.error("Video generation succeeded but video file was not found.")
                            break
                    else:
                        error_message = result.stderr
                        manim_code, attempts = handle_error_and_retry(error_message, manim_code, attempts)
                except Exception as e:
                    error_message = str(e)
                    manim_code, attempts = handle_error_and_retry(error_message, manim_code, attempts)
                progress_bar.progress(int((attempts + 1) * 50 / retry_limit))

            if attempts == retry_limit:
                st.error("Failed to generate video after 3 attempts.")
        except Exception as e:
            st.error(f"Error generating video: {e}")
