from reactpy import component, html, use_state
import json
from pathlib import Path

# Path to your JSON file
DATA_FILE_PATH = Path(__file__).parent / "data.json"

@component
def Apply():
    # States for the form inputs
    name, set_name = use_state("")
    regno, set_regno = use_state("")
    department, set_department = use_state("")
    intern_role, set_intern_role = use_state("")
    company_name, set_company_name = use_state("")
    company_location, set_company_location = use_state("")
    submission_status, set_submission_status = use_state("")
    # Submit button click handler
    def handle_submit(event=None):  # Accept the event argument
        # Collect form data
        new_entry = {
            "name": name,
            "regno": regno,
            "department": department,
            "intern_role": intern_role,
            "company_name": company_name,
            "company_location": company_location,
            "status": "Pending"  # Default status
        }
        
        # Append new entry to the existing data and save it to the JSON file
        append_to_json(new_entry)

        # Reset form fields after submission
        set_name("")
        set_regno("")
        set_department("")
        set_intern_role("")
        set_company_name("")
        set_company_location("")
        set_submission_status("Your application has been successfully submitted!")
    # Function to append data to the JSON file
    def append_to_json(new_entry):
        try:
            # Read existing data
            if DATA_FILE_PATH.exists():
                with open(DATA_FILE_PATH, "r") as f:
                    existing_data = json.load(f)
            else:
                existing_data = []
            
            # Append new entry
            existing_data.append(new_entry)

            # Save updated data
            with open(DATA_FILE_PATH, "w") as f:
                json.dump(existing_data, f, indent=4)
            print("Data saved successfully!")
        except Exception as e:
            print(f"Error saving data: {e}")
#display
    return html.div(
        {"style": apply_style()},
        html.div(
            {"style": overlay_style()},
        ),
        html.div(
            {"style": form_container_style()},
            html.h1({"style": header_style()}, "Permission for Internships"),
            html.p(
                {"style": paragraph_style()},
                "Fill out the form below to get permission from the Intern Coordinator."
            ),
            html.form(
                {"style": form_style(), "id": "internshipForm"},
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Name:"),
                    html.input({"type": "text", "name": "name", "style": input_style(), "value": name, "on_change": lambda event: set_name(event['target']['value']), "required": True})
                ),
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Registration Number:"),
                    html.input({"type": "text", "name": "regno", "style": input_style(), "value": regno, "on_change": lambda event: set_regno(event['target']['value'])})
                ),
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Department:"),
                    html.input({"type": "text", "name": "department", "style": input_style(), "value": department, "on_change": lambda event: set_department(event['target']['value'])})
                ),
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Intern Role:"),
                    html.input({"type": "text", "name": "intern_role", "style": input_style(), "value": intern_role, "on_change": lambda event: set_intern_role(event['target']['value'])})
                ),
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Company Name:"),
                    html.input({"type": "text", "name": "company_name", "style": input_style(), "value": company_name, "on_change": lambda event: set_company_name(event['target']['value'])})
                ),
                html.div(
                    {"style": form_group_style()},
                    html.label({"style": label_style()}, "Company Location:"),
                    html.input({"type": "text", "name": "company_location", "style": input_style(), "value": company_location, "on_change": lambda event: set_company_location(event['target']['value'])})
                ),
                html.button(
                    {"type": "button", "style": button_style(), "on_click": handle_submit},
                    "Submit"
                )
            ),
             # Display success message if submission_status is set
            html.div(
                {"style": success_message_style()},
                submission_status
            ) if submission_status else '',
        ),
    )


# Styles (same as before)
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
        "backgroundImage": "url('https://www.wallpaperhub.app/_next/image?url=https%3A%2F%2Fcdn.wallpaperhub.app%2Fcloudcache%2F8%2F1%2Fa%2Fe%2Fc%2F9%2F81aec9189ca0b7778fbba74ddfd67460bbe7c812.jpg&w=3000&h=2000&q=100')",
        "backgroundSize": "cover",
        "backgroundPosition": "fixed",
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
        "height":"15px",
        "background":"transparent",
        "color":"#ffff"
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
        "color":"#ffdd57"
    }

def paragraph_style():
    return {
        "fontSize": "1.2rem",
        "lineHeight": "1.6",
        "marginBottom": "30px",
    }
def success_message_style():
    return {
        "color": "lightgreen",
        "marginTop": "20px",
        "fontSize": "1.2rem",
        "fontWeight": "bold",
    }