import reflex as rx 
from rony.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twich","https://www.twitch.tv/?lang=es-ES"),
        link_button("Youtube","https://www.youtube.com/"),
        link_button("Instagram","https://www.instagram.com/"),
        link_button("Fecebook","https://es-la.facebook.com/")
    )