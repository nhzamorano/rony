import reflex as rx 
import datetime
from rony.styles.styles import Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="rony.jpeg",width="200px", height="auto"),
        rx.link(
            f"2014-{datetime.date.today().year} There are many variations of passages",
            href="https://www.lipsum.com/",
            is_external=True,
            font_size=Size.MEDIUM.value
            ),
        rx.text(" of Lorem Ipsum available, but the majority have",
                font_size=Size.MEDIUM.value,
                margin_top="0px !important"
                ),
        margin_bottom=Size.BIG.value
    )