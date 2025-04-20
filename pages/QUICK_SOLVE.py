import streamlit as st
import google.generativeai as genai
import subprocess
import os

# Configure Google Generative AI
genai.configure(api_key="AIzaSyAv_Hozwv3jAycftamoGYb1Gc0rMl5_j4c")  # Replace with your actual key
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI setup
st.set_page_config(page_title="Math Solution and Video Generator", layout="wide")
st.image('quicksolve.png')
st.title("📚 Math Solution and Video Generator")
st.write("Enter a math equation, solve it step by step, and generate a video explanation!")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Chat history display
st.subheader("Chat History")
for chat in st.session_state["chat_history"]:
    st.markdown(f"**You:** {chat['user_input']}")
    st.markdown(f"**AI:** {chat['response']}")

# Math problem input
st.subheader("Math Solver")
user_input = st.text_input("Enter a math equation or problem here:")

def clean_manim_code(raw_code):
    """Remove formatting and clean the raw Manim code."""
    return raw_code.strip().replace("```python", "").replace("```", "").strip()

def handle_error_and_retry(error_message, manim_code, attempt_count):
    """Retry on Manim code errors with feedback loop."""
    st.error(f"Manim error: {error_message}")
    retry_prompt = (
        f"The following Manim script failed with an error:\n"
        f"{manim_code}\n"
        f"Error:\n{error_message}\n"
        f"Please correct the code. Ensure:\n"
        f"- All objects stay within screen boundaries.\n"
        f"- No overlapping of text or visuals.\n"
        f"- Use .move_to() and scaling to keep layout clean.\n"
        f"Return ONLY the corrected Manim script, no extra text or comments."
    )
    response = model.generate_content([retry_prompt])
    corrected_code = clean_manim_code(response.text)
    with open("generate_solution.py", "w") as f:
        f.write(corrected_code)
    return corrected_code, attempt_count + 1

# Button to generate step-by-step solution
if st.button("Solve"):
    if user_input:
        try:
            response = model.generate_content([f"Provide a detailed, step-by-step solution to: {user_input}"])
            solution_steps = response.text
            st.session_state["chat_history"].append({
                "user_input": user_input,
                "response": solution_steps,
            })
            st.markdown("### Solution Steps:")
            st.write(solution_steps)
        except Exception as e:
            st.error(f"Error: {e}")

# Button to generate video using Manim
if st.button("Generate Video"):
    if user_input:
        try:
            prompt = (

                f"Create a Manim script to explain this math problem visually: {user_input}\n"
                f"Requirements: follow this strictly\n"
                f"- Use 'from manim import *' and define a Scene class.\n"
                f"- Start with a title using `Tex` or `Text`, centered.\n"
                f"- For formulas, use `MathTex(...).scale(0.7)`.\n"
                f"- Stack steps using `.arrange(DOWN, buff=0.5).move_to(ORIGIN)`.\n"
                f"- No overlapping — use `.next_to(...)` for side-by-side or `.arrange()` for stacks.\n"
                f"- Use `.move_to()` or `.to_edge()` to center things or pin to corners.\n"
                f"- Do NOT use FRAME_WIDTH / FRAME_HEIGHT — use 14 (width) and 8 (height) if needed.\n"
                f"- Use `Rectangle(width=14, height=8)` if full background is needed.\n"
                f"- Animate cleanly. Use FadeIn/Write/FadeOut sensibly.\n"
                f"Return only valid Python code. No explanation, markdown, or comments."
                f"- also use figures and diagrams neetly if they are necceassary\n"
                f"- with proper transition and animation.\n"
                f"- make sure objects and elemets not overlap each other on screen and not fall out of screen may stay in fix frame.\n"

            )


            response = model.generate_content([prompt])
            manim_code = clean_manim_code(response.text)

            with open("generate_solution.py", "w") as f:
                f.write(manim_code)

            retry_limit = 3
            attempts = 0
            progress_bar = st.progress(0)

            while attempts < retry_limit:
                st.write(f"Render attempt: {attempts + 1}/{retry_limit}")
                progress_bar.progress(int((attempts + 1) * 33))
                try:
                    manim_cmd = ["manim", "-pql", "generate_solution.py"]
                    result = subprocess.run(manim_cmd, capture_output=True, text=True)

                    if result.returncode == 0:
                        video_path = "media/videos/generate_solution/1080p60/Scene.mp4"
                        if os.path.exists(video_path):
                            st.video(video_path)
                            break
                        else:
                            st.error("Video generated but file not found.")
                            break
                    else:
                        error_message = result.stderr
                        manim_code, attempts = handle_error_and_retry(error_message, manim_code, attempts)
                except Exception as e:
                    error_message = str(e)
                    manim_code, attempts = handle_error_and_retry(error_message, manim_code, attempts)

            if attempts == retry_limit:
                st.error("Failed to generate video after 3 attempts.")
        except Exception as e:
            st.error(f"Error: {e}")


