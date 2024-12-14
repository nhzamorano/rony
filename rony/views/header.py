import reflex as rx
from rony.components.link_icon import link_icon
from rony.components.info_text import info_text
from rony.styles.styles import Size as Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src="rony.jpeg", size="9",width="100px", height="auto"),
            rx.vstack(
                rx.heading(
                    "Hola mi nombre es Rony Herrera", 
                    size="6"
                    ),
                rx.text(
                    "@ronydev",
                    margin_top="0px !important"
                    ),
                    rx.hstack(
                        link_icon("https://x.com"),
                        link_icon("https://x.com"),
                        link_icon("https://x.com"),
                    ),
                    
                    align_items="start"
            )
        ),
        rx.flex(
            info_text("+13", "años de experiencia"),
            rx.spacer(),
            info_text("+13", "años de experiencia"),
            rx.spacer(),
            info_text("+13", "años de experiencia"),
            width="100%"
        ),
        
        rx.text("""Contrary to popular belief, Lorem Ipsum is not simply random text. 
                It has roots in a piece of classical Latin literature from 45 BC, 
                making it over 2000 years old. Richard McClintock, a Latin professor 
                at Hampden-Sydney College in Virginia, looked up one of the more obscure 
                Latin words, consectetur, from a Lorem Ipsum"""),
                spacing="8",
        align_items="start"
    )