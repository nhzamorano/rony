import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(src="rony.jpeg", size="9"),
        rx.text("@mouredev"),
        rx.text("Hola mi nombre es Rony Herrera"),
        rx.text("""Contrary to popular belief, Lorem Ipsum is not simply random text. 
                It has roots in a piece of classical Latin literature from 45 BC, 
                making it over 2000 years old. Richard McClintock, a Latin professor 
                at Hampden-Sydney College in Virginia, looked up one of the more obscure 
                Latin words, consectetur, from a Lorem Ipsum""")
    )