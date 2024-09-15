from reactpy import component, html, use_state
import json
from pathlib import Path

# Path to your feedback JSON file
FEEDBACK_FILE_PATH = Path(__file__).parent / "feedback.json"

@component
def Feedback():
    # States for the form inputs
    name, set_name = use_state("")
    intern_role, set_intern_role = use_state("")
    company, set_company = use_state("")
    feedback_text, set_feedback_text = use_state("")
    submission_status, set_submission_status = use_state("")
    # Submit button click handler
    def handle_submit(event=None):
        # Collect form data
        new_feedback = {
            "name": name,
            "intern_role": intern_role,
            "company": company,
            "feedback": feedback_text
        }

        # Append new feedback entry to the JSON file
        append_to_json(new_feedback)

        # Reset form fields after submission
        set_name("")
        set_intern_role("")
        set_company("")
        set_feedback_text("")
        set_submission_status("Your feedback has been submitted!")
    # Function to append data to the JSON file
    def append_to_json(new_feedback):
        try:
            # Read existing data
            if FEEDBACK_FILE_PATH.exists():
                with open(FEEDBACK_FILE_PATH, "r") as f:
                    existing_feedback = json.load(f)
            else:
                existing_feedback = []

            # Append new feedback
            existing_feedback.append(new_feedback)

            # Save updated feedback data
            with open(FEEDBACK_FILE_PATH, "w") as f:
                json.dump(existing_feedback, f, indent=4)
            print("Feedback saved successfully!")
        except Exception as e:
            print(f"Error saving feedback: {e}")

    return html.div(
        {"style": apply_style()},
        html.div(
            {"style": overlay_style()},
        ),
        html.div(
            {"style": form_container_style()},
            html.h2({"style": header_style()}, "Internship Feedback"),
            html.p({"style": paragraph_style()}, "We would love to hear about your internship experience!"),
            html.form(
                {"style": form_style()},
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Name:"),
                    html.input({"type": "text", "name": "name", "style": input_style(), "value": name, "on_change": lambda event: set_name(event['target']['value']), "required": True})
                ),
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Intern Role:"),
                    html.input({"type": "text", "name": "intern_role", "style": input_style(), "value": intern_role, "on_change": lambda event: set_intern_role(event['target']['value']), "required": True})
                ),
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Company:"),
                    html.input({"type": "text", "name": "company", "style": input_style(), "value": company, "on_change": lambda event: set_company(event['target']['value']), "required": True})
                ),
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Feedback:"),
                    html.textarea(
                        {
                            "style": textarea_style(),
                            "name": "feedback",
                            "rows": "4",
                            "value": feedback_text,
                            "on_change": lambda event: set_feedback_text(event['target']['value']),
                            "required": True
                        }
                    )
                ),
                html.button(
                    {"type": "button", "style": button_style(), "on_click": handle_submit},
                    "Submit"
                ),
                html.div(
                {"style": success_message_style()},
                submission_status
            ) if submission_status else '',
        ),
            
        ),
    )
# The same styles used from the Apply page
def apply_style():
    return {
        "position": "relative",
        "height": "100vh",
        "width": "100vw",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "flexDirection": "column",
        "overflow": "hidden",
    }

def overlay_style():
    return {
        "position": "absolute",
        "top": "0",
        "left": "0",
        "right": "0",
        "bottom": "0",
        "backgroundImage": "url('https://www.wallpaperhub.app/_next/image?url=https%3A%2F%2Fcdn.wallpaperhub.app%2Fcloudcache%2F3%2F4%2F0%2F0%2Fa%2F8%2F3400a80abe7d3c93801628df3e7a9753490164e5.jpg&w=3000&h=2000&q=100')",
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "backgroundRepeat": "no-repeat",
        "opacity": "0.9",
        "zIndex": "1",
    }

def form_container_style():
    return {
        "position": "relative",
        "backgroundColor": "rgba(0, 0, 0, 0.6)",
        "padding": "30px",
        "borderRadius": "10px",
        "textAlign": "center",
        "color": "#fff",
        "maxWidth": "80%",
        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
        "zIndex": "2",
    }

def form_style():
    return {
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "gap": "15px",
    }

def form_group_style():
    return {
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "space-between",
        "marginBottom": "15px",
        "width": "100%",
    }

def label_style():
    return {
        "flex": "1",
        "fontSize": "1rem",
        "textAlign": "left",
        "marginRight": "10px",
    }

def input_style():
    return {
        "flex": "2",
        "padding": "10px",
        "borderRadius": "5px",
        "border": "1px solid #ddd",
        "fontSize": "1rem",
        "height": "15px",
        "background": "transparent",
        "color": "#ffff",
    }

def textarea_style():
    return {
        "flex": "2",
        "padding": "10px",
        "borderRadius": "5px",
        "border": "1px solid #ddd",
        "fontSize": "1rem",
        "background": "transparent",
        "color": "#ffff",
        "resize": "none",
    }

def button_style():
    return {
        "backgroundColor": "#ffdd57",
        "color": "#333",
        "padding": "10px 20px",
        "borderRadius": "5px",
        "border": "none",
        "fontSize": "1.1rem",
        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
        "cursor": "pointer",
        "transition": "background-color 0.3s ease",
    }

def header_style():
    return {
        "fontSize": "2rem",
        "margin": "0 0 20px 0",
        "color": "#ffdd57"
    }

def paragraph_style():
    return {
        "fontSize": "1.2rem",
        "lineHeight": "1.6",
        "marginBottom": "30px",
        "color": "#fff",
    }
def success_message_style():
    return {
        "color": "lightgreen",
        "marginTop": "20px",
        "fontSize": "1.2rem",
        "fontWeight": "bold",
    }