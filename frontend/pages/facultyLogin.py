from reactpy import component, html, use_state

@component
def FacultyLogin(on_navigate, set_logged_in):
    # Hardcoded faculty credentials
    FACULTY_ID = "faculty123"
    FACULTY_PASSWORD = "password456"

    # States for form inputs and error messages
    faculty_id, set_faculty_id = use_state("")
    password, set_password = use_state("")
    error_message, set_error_message = use_state("")

    # Handle login submission
    def handle_login(event=None):
        if faculty_id == FACULTY_ID and password == FACULTY_PASSWORD:
            set_logged_in(True)  # Set global login state to true
            set_error_message("")
            on_navigate("dashboard")  # Redirect to the dashboard
        else:
            set_error_message("Invalid Faculty ID or Password.")

    # Styling for the outer container (background image, centering the form)
    outer_container_style = {
        "width": "100vw",
        "height": "100vh",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "backgroundImage": "url(https://images.pexels.com/photos/1421903/pexels-photo-1421903.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)",  # Replace with your actual image URL
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "boxSizing": "border-box",
        "padding": "20px"
    }

    # Styling for the login form container (transparent background)
    login_box_style = {
        "backgroundColor": "rgba(0, 0, 0, 0.6)",  # Transparent black background
        "padding": "40px",
        "borderRadius": "10px",
        "boxShadow": "0 8px 16px rgba(0, 0, 0, 0.3)",
        "width": "100%",
        "maxWidth": "400px",
        "boxSizing": "border-box",
        "color": "white"
    }

    # Input field styling
    input_style = {
        "width": "100%",
        "padding": "12px",
        "margin": "10px 0",
        "border": "none",
        "borderRadius": "4px",
        "fontSize": "16px",
        "boxSizing": "border-box"
    }

    # Button styling
    button_style = {
        "width": "100%",
        "padding": "12px",
        "backgroundColor": "#4CAF50",  # Green color for the button
        "color": "white",
        "border": "none",
        "borderRadius": "4px",
        "cursor": "pointer",
        "fontSize": "16px",
        "fontWeight": "bold"
    }

    # Error message styling
    error_message_style = {
        "color": "#ff4d4d",  # Light red for error messages
        "marginTop": "15px"
    }

    # Render the login form
    return html.div(
        {"style": outer_container_style},
        html.div(
            {"style": login_box_style},
            html.h1({"style": {"textAlign": "center", "marginBottom": "20px"}}, "Faculty Login"),
            html.form(
                {"onSubmit": handle_login},
                html.div(
                    html.label("Faculty ID:"),
                    html.input({
                        "type": "text", 
                        "value": faculty_id, 
                        "onChange": lambda event: set_faculty_id(event['target']['value']),
                        "style": input_style
                    })
                ),
                html.div(
                    html.label("Password:"),
                    html.input({
                        "type": "password", 
                        "value": password, 
                        "onChange": lambda event: set_password(event['target']['value']),
                        "style": input_style
                    })
                ),
                html.button({"type": "button", "onClick": handle_login, "style": button_style}, "Login")
            ),
            html.p({"style": error_message_style}, error_message) if error_message else ''
        )
    )
