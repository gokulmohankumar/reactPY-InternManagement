from reactpy import component, html, use_state, use_effect
import json
from pathlib import Path

# Load data from the JSON file
HERE = Path(__file__).parent
DATA_PATH = HERE / 'data.json'

def load_data():
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

# FacultyLogin Component
@component
def InternControl():
    # Load and manage data state
    data, set_data = use_state([])

    # Effect to load data when component mounts
    use_effect(lambda: set_data(load_data()), [])

    # Approve or Disapprove action
    def update_status(regno, new_status):
        updated_data = []
        for item in data:
            if item["regno"] == regno:
                item["status"] = new_status
            updated_data.append(item)
        set_data(updated_data)

        # Write back to the JSON file
        with open(DATA_PATH, 'w') as f:
            json.dump(updated_data, f, indent=4)

    # Table for pending items with Approve and Disapprove actions
    def render_pending_table():
        pending_items = [item for item in data if item["status"].lower() == "pending"]
        return html.div(
            {"style": table_container_style()},
            html.h2({"style": header_style()}, "Pending Applications"),
            html.table(
                {"style": table_style()},
                html.thead(
                    html.tr(
                        html.th({"style": table_head_style()}, "Reg No"),
                        html.th({"style": table_head_style()}, "Name"),
                        html.th({"style": table_head_style()}, "Department"),
                        html.th({"style": table_head_style()}, "Intern Role"),
                        html.th({"style": table_head_style()}, "Company"),
                        html.th({"style": table_head_style()}, "Location"),
                        html.th({"style": table_head_style()}, "Actions")
                    )
                ),
                html.tbody(
                    [
                        html.tr(
                            {"style": table_row_style()},
                            html.td({"style": table_cell_style()}, item["regno"]),
                            html.td({"style": table_cell_style()}, item["name"]),
                            html.td({"style": table_cell_style()}, item["department"]),
                            html.td({"style": table_cell_style()}, item["intern_role"]),
                            html.td({"style": table_cell_style()}, item["company_name"]),
                            html.td({"style": table_cell_style()}, item["company_location"]),
                            html.td({"style": table_cell_style()},
                                html.button(
                                    {"style": approve_style(), "onClick": lambda event, regno=item["regno"]: update_status(regno, "Approved")},
                                    "Approve"
                                ),
                                html.button(
                                    {"style": disapprove_style(), "onClick": lambda event, regno=item["regno"]: update_status(regno, "Disapproved")},
                                    "Disapprove"
                                )
                            )
                        ) for item in pending_items
                    ]
                )
            )
        )

    # Table for approved items
    def render_approved_table():
        approved_items = [item for item in data if item["status"].lower() == "approved"]
        return html.div(
            {"style": table_container_style()},
            html.h2({"style": header_style()}, "Approved Applications"),
            html.table(
                {"style": table_style()},
                html.thead(
                    html.tr(
                        html.th({"style": table_head_style()}, "Reg No"),
                        html.th({"style": table_head_style()}, "Name"),
                        html.th({"style": table_head_style()}, "Department"),
                        html.th({"style": table_head_style()}, "Intern Role"),
                        html.th({"style": table_head_style()}, "Company"),
                        html.th({"style": table_head_style()}, "Location")
                    )
                ),
                html.tbody(
                    [
                        html.tr(
                            {"style": table_row_style()},
                            html.td({"style": table_cell_style()}, item["regno"]),
                            html.td({"style": table_cell_style()}, item["name"]),
                            html.td({"style": table_cell_style()}, item["department"]),
                            html.td({"style": table_cell_style()}, item["intern_role"]),
                            html.td({"style": table_cell_style()}, item["company_name"]),
                            html.td({"style": table_cell_style()}, item["company_location"])
                        ) for item in approved_items
                    ]
                )
            )
        )

    # Table for disapproved items
    def render_disapproved_table():
        disapproved_items = [item for item in data if item["status"].lower() == "disapproved"]
        return html.div(
            {"style": table_container_style()},
            html.h2({"style": header_style()}, "Disapproved Applications"),
            html.table(
                {"style": table_style()},
                html.thead(
                    html.tr(
                        html.th({"style": table_head_style()}, "Reg No"),
                        html.th({"style": table_head_style()}, "Name"),
                        html.th({"style": table_head_style()}, "Department"),
                        html.th({"style": table_head_style()}, "Intern Role"),
                        html.th({"style": table_head_style()}, "Company"),
                        html.th({"style": table_head_style()}, "Location")
                    )
                ),
                html.tbody(
                    [
                        html.tr(
                            {"style": table_row_style()},
                            html.td({"style": table_cell_style()}, item["regno"]),
                            html.td({"style": table_cell_style()}, item["name"]),
                            html.td({"style": table_cell_style()}, item["department"]),
                            html.td({"style": table_cell_style()}, item["intern_role"]),
                            html.td({"style": table_cell_style()}, item["company_name"]),
                            html.td({"style": table_cell_style()}, item["company_location"])
                        ) for item in disapproved_items
                    ]
                )
            )
        )

    # Render the full page with separate tables
    return html.div(
        {"style": status_container_style()},
        render_pending_table(),
        html.br,
        render_approved_table(),
        html.br,
        render_disapproved_table()
    )

# Table and page styling
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
        "fontSize": "1rem",
        "margin": "0 0 10px 0",
        "color": "#ffdd57"
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
        "width": "100%",
        "height": "100%"
    }

def table_style():
    return {
        "width": "100%",
        "borderCollapse": "collapse",
        "backgroundColor": "transparent",
        "color": "#ffff",
    }

def table_head_style():
    return {
        "backgroundColor": "#ffdd57",
        "color": "#333",
        "fontWeight": "bold",
        "padding": "10px",
    }

def table_row_style():
    return {
        "borderBottom": "1px solid #ddd",
    }

def table_cell_style():
    return {
        "padding": "15px",
        "textAlign": "left",
    }

def approve_style():
    return {
        "padding": "5px",
        "background": "green",
        "color": "white",
        "borderRadius": "3px",
        "cursor": "pointer"
    }

def disapprove_style():
    return {
        "padding": "5px",
        "background": "red",
        "color": "white",
        "borderRadius": "3px",
        "cursor": "pointer"
    }
