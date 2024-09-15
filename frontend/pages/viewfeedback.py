from reactpy import component, html, use_state, use_effect,run
import json
from pathlib import Path

@component
def ViewFeedback():
    # State to store the loaded data
    data, set_data = use_state([])

    # Effect to load data on component mount (similar to useEffect in React)
    async def load_data():
        HERE = Path(__file__).parent
        DATA_PATH = HERE / 'feedback.json'
        try:
            with open(DATA_PATH, 'r') as f:
                loaded_data = json.load(f)
            set_data(loaded_data)  # Set the loaded data to the component state
        except FileNotFoundError:
            print("Data file not found!")

    use_effect(load_data, [])

    # Render each feedback as a card
    feedback_cards = [
        html.div(
            {"style": card_style()},
            html.h3({"style": card_title_style()}, feedback.get("name", "Anonymous")),
            html.p({"style": card_text_style()}, f"Role: {feedback.get('intern_role', 'N/A')}"),
            html.p({"style": card_text_style()}, f"Company: {feedback.get('company', 'N/A')}"),
            html.p({"style": card_text_style()}, f"Feedback: {feedback.get('feedback', 'No feedback')}"),
        )
        for feedback in data
    ]

    return html.div(
        {"style": container_style()},
        html.h2({"style": header_style()}, "User Feedbacks"),
        html.div({"style": card_container_style()}, feedback_cards)
    )

# Styles
def container_style():
    return {
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "justifyContent": "center",
        "width": "100vw",
        "height": "100vh",
        "backgroundImage": "url('https://www.wallpaperhub.app/_next/image?url=https%3A%2F%2Fcdn.wallpaperhub.app%2Fcloudcache%2F8%2F1%2Fa%2Fe%2Fc%2F9%2F81aec9189ca0b7778fbba74ddfd67460bbe7c812.jpg&w=3000&h=2000&q=100')",
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "padding": "40px",
        "overflowY": "auto",  # Allows scrolling if there are many feedbacks
    }

def header_style():
    return {
        "color": "#ffdd57",
        "fontSize": "2rem",
        "marginBottom": "30px",
    }

def card_container_style():
    return {
        "display": "grid",
        "gridTemplateColumns": "repeat(auto-fit, minmax(300px, 1fr))",
        "gap": "20px",
        "width": "100%",
        "maxWidth": "1200px",
        "padding": "20px",
    }

def card_style():
    return {
        "backgroundColor": "rgba(255, 255, 255, 0.8)",
        "borderRadius": "10px",
        "padding": "20px",
        "boxShadow": "0 4px 10px rgba(0, 0, 0, 0.1)",
        "transition": "transform 0.2s ease-in-out",
        "overflow": "hidden",
        "textAlign": "center",
        "backdropFilter": "blur(10px)",  # Adds a blur effect for transparency
        ":hover": {
            "transform": "scale(1.05)",  # Hover effect
            "boxShadow": "0 6px 15px rgba(0, 0, 0, 0.2)",
        },
    }

def card_title_style():
    return {
        "fontSize": "1.5rem",
        "color": "#333",
        "marginBottom": "10px",
    }

def card_text_style():
    return {
        "fontSize": "1rem",
        "color": "#666",
        "marginBottom": "5px",
    }