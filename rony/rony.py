import reflex as rx
from rony.components.navbar import navbar
from rony.components.footer import footer
from rony.views.header import header
from rony.views.links.links import links
import rony.styles.styles as styles
from rony.styles.styles import Size as Size




def index() -> rx.Component:
    return  rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value
            )
        ),
        rx.center(
            footer()
        )
    )

    
    


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)