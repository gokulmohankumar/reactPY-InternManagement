from reactpy import component, html

@component
def Home():
    return html.div(
        {"style": home_style()},
        # Background image overlay for opacity effect
        html.div(
            {"style": overlay_style()},
        ),
        html.div(
            {"style": text_container_style()},
            html.h1({"style": header_style()}, "Welcome to the Internship Management System"),
            html.p(
                {"style": paragraph_style()},
                "Manage your internships with ease. From applying to checking your status and "
                "receiving feedback, our system streamlines the entire process."
            ),
            html.div(
                {"style": feature_list_style()},
                html.div(
                    {"style": feature_item_style()},
                    html.h2({"style": feature_title_style()}, "Apply for Internships"),
                    html.p(
                        {"style": feature_text_style()},
                        "Easily apply for multiple internships in just a few clicks."
                    ),
                ),
                html.div(
                    {"style": feature_item_style()},
                    html.h2({"style": feature_title_style()}, "Track Your Application Status"),
                    html.p(
                        {"style": feature_text_style()},
                        "Stay updated on the status of your internship applications."
                    ),
                ),
                html.div(
                    {"style": feature_item_style()},
                    html.h2({"style": feature_title_style()}, "Faculty Login"),
                    html.p(
                        {"style": feature_text_style()},
                        "Faculty members can log in to approve or provide feedback on internships."
                    ),
                ),
            ),
        ),
    )

# Styles

def home_style():
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
        "backgroundImage": "url('https://images.pexels.com/photos/3182773/pexels-photo-3182773.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')",
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "backgroundRepeat": "no-repeat",
        "opacity": "0.9",
        "zIndex": "1",
    }

def text_container_style():
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

def header_style():
    return {
        "fontSize": "3rem",
        "margin": "0 0 20px 0",
    }

def paragraph_style():
    return {
        "fontSize": "1.2rem",
        "lineHeight": "1.6",
        "marginBottom": "30px"
    }

def feature_list_style():
    return {
        "display": "flex",
        "justifyContent": "space-around",
        "margin": "30px 0",
    }

def feature_item_style():
    return {
        "textAlign": "center",
        "maxWidth": "200px",
    }

def feature_title_style():
    return {
        "fontSize": "1.5rem",
        "marginBottom": "10px",
        "color": "#ffdd57"
    }

def feature_text_style():
    return {
        "fontSize": "1rem",
        "lineHeight": "1.4"
    }

def button_container_style():
    return {
        "marginTop": "30px",
        "display": "flex",
        "gap": "20px",
        "justifyContent": "center"
    }
