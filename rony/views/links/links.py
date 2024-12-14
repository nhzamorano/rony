import reflex as rx 
from rony.components.link_button import link_button
from rony.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twich","The standard chunk of Lorem Ipsum used since the 1500s","https://www.twitch.tv/?lang=es-ES"),
        link_button("Youtube","reproduced below for those interested. Sections","https://www.youtube.com/"),
        link_button("Instagram","Latin words, combined with a handful of model sentence","https://www.instagram.com/"),
        link_button("Fecebook","literature, discovered the undoubtable source. Lorem Ipsum","https://es-la.facebook.com/"),
        title("Comunidad"),
        link_button("Twich","The standard chunk of Lorem Ipsum used since the 1500s","https://www.twitch.tv/?lang=es-ES"),
        link_button("Youtube","reproduced below for those interested. Sections","https://www.youtube.com/"),
        link_button("Instagram","Latin words, combined with a handful of model sentence","https://www.instagram.com/"),
        link_button("Fecebook","literature, discovered the undoubtable source. Lorem Ipsum","https://es-la.facebook.com/"),
        width="100%"
    )