import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "ronydeveloper",
            height="40px"
        ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        width="100%",
        z_index="999"
    )