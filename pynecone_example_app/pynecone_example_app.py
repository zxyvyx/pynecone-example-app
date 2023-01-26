"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
  """The app state."""

  pass


def index():
  return pc.center(
    pc.vstack(
      pc.heading("Welcome to Pynecone!", font_size="1em"),
      pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
      pc.link(
        "Check out our docs!",
        href=docs_url,
        border="0.1em solid",
        padding="0.5em",
        border_radius="0.5em",
        _hover={
          "color": "rgb(107,99,246)",
        },
      ),
      pc.link(
        "Go to the about page",
        href="/about",
        color="rgb(107,99,246)",
      ),
      spacing="1.5em",
      font_size="2em",
    ),
    padding_top="10%",
  )
  

def about():
  return pc.center(
    pc.vstack(
      pc.heading("About", font_size="1em"),
      pc.box("This is the about page."),
      spacing="1.5em",
      font_size="2em",
  )
)

def contact():
  return pc.center(
    pc.vstack(
      pc.heading("Contact", font_size="1em"),
      pc.box("This is the contact page."),
      spacing="1.5em",
      font_size="2em",
  )
)

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(about)
app.add_page(contact)
app.compile()
