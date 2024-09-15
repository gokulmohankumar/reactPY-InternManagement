from reactpy import component, html, run, use_state
from pages import Home, Apply, Status, FacultyLogin, Feedback, InternControl, ViewFeedback

# Navbar Component
@component
def Navbar(on_navigate, faculty_logged_in, handle_logout):
    return html.nav(
        {"style": navbar_style()},
        html.h3({"href": "#", "style": logo_style(), "onClick": lambda event: on_navigate("home")}, "GTPDS~intern"),
        html.a({"href": "#", "style": link_style(), "onClick": lambda event: on_navigate("home")}, "Home"),
        html.a({"href": "#", "style": link_style(), "onClick": lambda event: on_navigate("apply")}, "Apply"),
        html.a({"href": "#", "style": link_style(), "onClick": lambda event: on_navigate("status")}, "Check Status"),
        html.a({"href": "#", "style": link_style(), "onClick": lambda event: on_navigate("feedback")}, "Feedback"),
        html.a({"href": "#", "style": link_style(), "onClick": lambda event: on_navigate("view-feedback")}, "View Feedbacks"),
        html.a(
            {"href": "#", "style": link_style(), "onClick": lambda event: handle_logout()}, "Logout"
        ) if faculty_logged_in else html.a(
            {"href": "#", "style": link_style(), "onClick": lambda event: on_navigate("faculty-login")}, "Faculty Login"
        )
    )

# MainApp Component
@component
def MainApp():
    # Manage page navigation and faculty login state
    page, set_page = use_state("home")
    faculty_logged_in, set_faculty_logged_in = use_state(False)

    # Navigation handler
    def handle_navigation(new_page):
        set_page(new_page)

    # Logout handler
    def handle_logout():
        set_faculty_logged_in(False)  # Set login state to false
        set_page("home")  # Redirect to home page after logout

    # Render page based on navigation
    def render_page():
        if page == "home":
            return Home()
        elif page == "apply":
            return Apply()
        elif page == "status":
            return Status()
        elif page == "faculty-login":
            # Pass the global login handler here
            return FacultyLogin(on_navigate=handle_navigation, set_logged_in=set_faculty_logged_in)
        elif page == "feedback":
            return Feedback()
        elif page == "dashboard":
            return InternControl()
        elif page == "view-feedback":
            return ViewFeedback()
        else:
            return Home()  # Default to Home if route is not recognized

    return html.div(
        {"style": global_style()},
        # Pass handle_logout to the Navbar
        Navbar(handle_navigation, faculty_logged_in, handle_logout),  
        render_page()  # Render the current page based on state
    )

# Styles
def global_style():
    return {
        "margin": "0",
        "padding": "0",
        "boxSizing": "border-box",
        "overflow": "hidden",
        "width": "100vw",
        "height": "100vh",
        "fontFamily": "Arial, sans-serif"
    }

def navbar_style():
    return {
        "display": "flex",
        "justifyContent": "flex-end",
        "padding": "10px",
        "backgroundColor": "#333",
        "width": "100%",
        "zIndex": "1000",
        "position": "fixed",
        "top": "0",
        "left": "0",
        "right": "0",
        "height": "30px"
    }

def link_style():
    return {
        "color": "#fff",
        "padding": "5px 15px",
        "textDecoration": "none",
        "fontSize": "1.1rem",
        "borderRadius": "5px",
        "marginLeft": "5px",
        ":hover": {  
            "color": "#f39c12" 
        }
    }

def logo_style():
    return {
        "color": "yellow",
        "position": "relative",
        "right": "500px",
        "bottom": "10px"
    }

# Main Function to run the app
def main():
    run(MainApp)

if __name__ == "__main__":
    main()
