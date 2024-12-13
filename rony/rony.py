import reflex as rx
from rony.components.navbar import navbar
from rony.components.footer import footer
from rony.views.header import header
from rony.views.links.links import links


def index() -> rx.Component:
    return  rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
        )
    
    


app = rx.App()
app.add_page(index)