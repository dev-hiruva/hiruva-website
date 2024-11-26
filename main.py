from fasthtml.common import *

app = FastHTML(hdrs=(picolink,
                     # `Style` is an `FT` object, which are 3-element lists consisting of:
                     # (tag_name, children_list, attrs_dict).
                     # FastHTML composes them from trees and auto-converts them to HTML when needed.
                     # You can also use plain HTML strings in handlers and headers,
                     # which will be auto-escaped, unless you use `NotStr(...string...)`.
                     Style(':root { --pico-font-size: 100%; }'))
                )

@app.get("/")
def home():
    return Div(
        H4("Hiruva is an educational non-profit developing courses in AI safety and security"),
        H4("More coming soon!"),
        style="text-align: center; margin-top: 100px"
    )

serve()