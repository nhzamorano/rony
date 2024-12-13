import reflex as rx 
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="rony.jpeg"),
        rx.link(
            f"2014-{datetime.date.today().year} There are many variations of passages",
            href="https://www.lipsum.com/",
            is_external=True),
        rx.text(" of Lorem Ipsum available, but the majority have")
    )