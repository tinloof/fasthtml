from fasthtml.common import *

samples = [
    ("Game of life", "game-of-life.svg"),
    ("To-do", "todo.svg"),
    ("Chat bot", "chat-bot.svg"),
    ("Pictionary AI", "pictionary-ai.svg")
]

components = [
    ("Card", "/card.fasthtml", "# card demo code", P("FastHTML is as intuitive as FastAPI", cls="m-body text-black")),
    ("Button", "/button.fasthtml", "# button demo code", P("FastHTML is as intuitive as FastAPI", cls="m-body text-black")),
    ("Accordion", "/accordion.fasthtml", "# accordion demo code", P("FastHTML is as intuitive as FastAPI", cls="m-body text-black")),
    ("Stacked Cards", "/stacked_cards.fasthtml", "# stacked-cards demo code", P("FastHTML is as intuitive as FastAPI", cls="m-body text-black"))
]

stacked = [
    ("What you need to know", "Everything you need to get started with FastHTML.", [
        ("Python", "python.svg", "https://www.python.org/"),
        ("HTMX", "htmx.svg", "https://htmx.org/"),
    ]),
    ("What it is built on top of", "Now it's time to use FastHTML", [
        ("Python", "python.svg", "https://www.python.org/"),
        ("Uvicorn", "uvicorn.svg", "https://www.uvicorn.org/"),
        ("Starlette", "starlette.svg", "https://www.starlette.io/"),
        ("HTMX", "htmx.svg", "https://htmx.org/"),
    ]),
    ("Where you can deploy", "Companies that we provide deployment for", [
        ("Railway", "railway.svg", "https://railway.app/"),
        ("Hugging Face", "hugging-face.svg", "https://huggingface.co/"),
        ("Vercel", "vercel.svg", "https://vercel.com/"),
        ("PythonAnywhere", "python-anywhere.svg", "https://www.pythonanywhere.com/"),
    ]),
]

benefits = [
    ("Low learning curve", "Incorporate any Python library and any JavaScript library you like."),
    ("Speed and scalability", "HTTP/HTML, bringing the foundations of the web to you."),
    ("Styling", "Pure CSS or you can use framework like Tailwind.")
]

faqs = [
    ("What kinds of applications can be written with this?", "It's good for: general purpose web applications (i.e anything you'd build with React, Django, NexJS, etc); quick dashboards, prototypes, and in-company apps (e.g. like what you might use gradio/streamlit/etc for); Analytics/models/dashboards interactive reports; Custom blogs and content-heavy sites where you also want some interactive/dynamic content."),
    ("Where can I deploy my FastHTML to? What's needed?", "You can deploy a FastHTML app to any service or server that supports Python. We have guides and helpers for Railway.app, Vercel, Hugging Face Spaces, Replit, and PythonAnywhere. You can also use any VPS or server, or any on-premise machine with Python installed. All major operating systems are supported."),
    ("How does FastHTML relate to FastAPI?", "FastAPI is one of the inspirations for FastHTML. We are fans of its developer experience and tried to make FastHTML extremely familiar for FastAPI users. FastAPI is designed for creating APIs, whereas FastHTML is designed for creating HTML (i.e \"Hypermedia applications\"). Anything you could create with FastAPI (plus a JS frontend), you could also create with FastHTML, and vice versa -- if you prefer mainly writing JS, you might prefer FastAPI, since you can move a lot of client-side logic into the JS. If you prefer mainly writing Python, you'll probably want to use FastHTML, since you can often avoid using JS entirely."),
    ("Is this only for multi-page \"old style\" web apps, or can FastHTML be used for modern SPA apps too?", "FastHTML is specifically designed to make writing modern SPA apps as fast and easy as possible, whilst also ensuring the apps you write are scalable and performant. By default, FastHTML routes return lightweight \"partials\" that update the DOM directly, rather than doing a full page refresh."),
    ("What is HTMX, and what's it go to do with FastHTML?", "HTMX is best thought of as filling in the missing bits of a web browser -- in fact, web browser manufacturers are considering incorporating similar features directly into future browsers. It is a small javascript library that with a single line of HTML lets you respond to any event from any part of a web page by modifying the DOM in any way you like, all directly from Python. Whilst you don't have to use it with FastHTML, it will dramatically increase the amount of stuff you can do!"),
    ("Do I need to know JS? Can I use it if I want, with FastHTML?", "No, and yes! You can write nearly any standard web app with just Python. However, using a bit of JS can be helpful -- for instance, nearly any existing JS lib can be incorporated into a FastHTML app, and you can sprinkle bits of JS into your pages anywhere you like."),
    ("Are FastHTML apps slower than React, Next.JS, etc?", "It depends. Apps using FastHTML and HTMX are often faster than JS-based approaches using big libraries, since they can be very lightweight.")
]

testimonials = [
    ("FastHTML is as intuitive as FastAPI, lends itself to clean architecture, and its HTML+HTMX structure makes it a good competitor to Django for building webapps. Most importantly, it's fun to use.", "Daniel Roy Greenfield", "Co-author", "Two Scoops of Django", "assets/testimonials/daniel-roy.png"),
    ("Python has always been a wonderful tool for creating web applications; with FastHTML, it's even better!", "Giles Thomas", "Founder", "PythonAnywhere", "assets/testimonials/giles-thomas.png"),
    ("With FastHTML and Railway, Pythonistas can now have a real web application running in minutes, and can scale it all the way up to sophisticated production deployments.", "Jake Cooper", "CEO", "Railway.app", "assets/testimonials/jake-cooper.png")
]
