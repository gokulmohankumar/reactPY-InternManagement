from reactpy import component, html, use_state, use_effect
import json
from pathlib import Path

@component
def Status():
    # State to store the loaded data
    data, set_data = use_state([])

    # Effect to load data on component mount (similar to useEffect in React)
    async def load_data():
        HERE = Path(__file__).parent
        DATA_PATH = HERE / 'data.json'
        try:
            with open(DATA_PATH, 'r') as f:
                loaded_data = json.load(f)
            set_data(loaded_data)  # Set the loaded data to the component state
        except FileNotFoundError:
            print("Data file not found!")

    use_effect(load_data, [])

    return html.div(
        {"style": status_container_style()},
        html.h2({"style": header_style()}, "Check Status"),
        html.p({"style": paragraph_style()}, "Check the status of your internship applications here."),
        html.div(
            {"style": table_container_style()},
            html.table(
                {"style": table_style()},
                html.thead(
                    html.tr(
                        html.th({"style": table_head_style()}, "Name"),
                        html.th({"style": table_head_style()}, "Reg No"),
                        html.th({"style": table_head_style()}, "Department"),
                        html.th({"style": table_head_style()}, "Intern Role"),
                        html.th({"style": table_head_style()}, "Company Name"),
                        html.th({"style": table_head_style()}, "Company Location"),
                        html.th({"style": table_head_style()}, "Status")
                    )
                ),
                html.tbody(
                    [html.tr(
                        {"style": table_row_style()},
                        html.td({"style": table_cell_style()}, entry.get("name", "N/A")),
                        html.td({"style": table_cell_style()}, entry.get("regno", "N/A")),
                        html.td({"style": table_cell_style()}, entry.get("department", "N/A")),
                        html.td({"style": table_cell_style()}, entry.get("intern_role", "N/A")),
                        html.td({"style": table_cell_style()}, entry.get("company_name", "N/A")),
                        html.td({"style": table_cell_style()}, entry.get("company_location", "N/A")),
                        html.td({"style": table_cell_style()}, entry.get("status", "N/A"))
                    ) for entry in data]  # Iterate over loaded data
                )
            )
        )
    )

# Define styles to match Apply page
def status_container_style():
    return {
        "position": "relative",
        "height": "100vh",
        "width": "100vw",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "flexDirection": "column",
        "overflow": "hidden",
        "backgroundImage": "url('https://www.wallpaperhub.app/_next/image?url=https%3A%2F%2Fcdn.wallpaperhub.app%2Fcloudcache%2F8%2F1%2Fa%2Fe%2Fc%2F9%2F81aec9189ca0b7778fbba74ddfd67460bbe7c812.jpg&w=3000&h=2000&q=100')",
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "backgroundRepeat": "no-repeat",
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
        "color": "#fff",  # Ensuring the text is visible on the background
    }

def table_container_style():
    return {
        "position": "relative",
        "backgroundColor": "rgba(0, 0, 0, 0.6)",  # Semi-transparent background
        "padding": "20px",
        "borderRadius": "10px",
        "textAlign": "center",
        "color": "#fff",
        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
        "maxWidth": "90%",
        "zIndex": "2",
        "overflowX": "auto",
        "width": "100%",  # Full width
        "height": "100%",
        "bottom":"20px"  # Full height
    }

def table_style():
    return {
        "width": "100%",
        "borderCollapse": "collapse",
        "backgroundColor": "transparent",  # Transparent table background
        "color": "#ffff",
    }

def table_head_style():
    return {
        "backgroundColor": "#ffdd57",  # Yellow header background
        "color": "#333",
        "fontWeight": "bold",
        "padding": "10px",  # Padding for header cells
    }

def table_row_style():
    return {
        "borderBottom": "1px solid #ddd",
    }

def table_cell_style():
    return {
        "padding": "15px",  # Increased padding for table cells
        "textAlign": "left",
    }
