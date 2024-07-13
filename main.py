from fasthtml.common import *
from content import benefits,components,stacked,faqs,testimonials,samples

icons = 'assets/icons'

col = "flex flex-col"
center = "flex items-center"
between = "flex justify-between"
gap2 = "flex gap-2"
section_base=f"pt-8 px-4 pb-24 {col} gap-8 lg:gap-16 lg:pt-16 lg:px-16 lg:pb-32"
section_base_no_flex="pt-8 px-4 pb-24 gap-8 lg:gap-16 lg:pt-16 lg:px-16 lg:pb-32"
def maxpx (px ): return f"w-full max-w-[{px}px]"
def maxrem(rem): return f"w-full max-w-[{rem}rem]"

icons = 'assets/icons'

def section_wrapper(content, bg_color, xtra=""):
    return Section(content, cls=f"bg-{bg_color} {section_base} -mt-8 lg:-mt-16 items-center rounded-t-3xl lg:rounded-t-[2.5rem] relative {xtra}")

def section_wrapper_no_flex(content, bg_color, xtra=""):
    return Section(content, cls=f"bg-{bg_color} {section_base_no_flex} -mt-8 lg:-mt-16 items-center rounded-t-3xl lg:rounded-t-[2.5rem] relative {xtra}")


def button(text, href="/", xtra="", **kw):
    return A(text, href=href, cls=f"bg-black text-white py-2 px-4 s-body rounded-full hover:bg-black/80 transition-colors duration-300 {xtra}", **kw)

def section_header(mono_text, heading, subheading, max_width=32):
    return Div(
        P(mono_text, cls="mono-body text-opacity-60"),
        H2(heading, cls=f"text-black heading-2"),
        P(subheading, cls=f"l-body {maxrem(max_width)}"),
        cls=f"{maxrem(50)} mx-auto {col} items-center text-center gap-6")

def benefit(title, content):
    return Div(
        H3(title, cls=f"text-black heading-3"),
        P(content, cls=f"l-body mt-6 lg:mt-8"),
        cls="w-full p-6 bg-soft-yellow rounded-2xl lg:p-12 lg:h-[22rem] lg:w-[26rem]")

def faq_item(question, answer, id):
    return Div(
        Input(id=f"collapsible-{id}", type="checkbox", cls=f"collapsible-checkbox peer/collapsible-{id} hidden"),
        Label(
            P(question, cls=f"text-black s-body flex-grow"),
            Img(src=f"{icons}/plus-icon.svg", alt="Expand", cls="plus-icon w-6 h-6"),
            Img(src=f"{icons}/minus-icon.svg", alt="Collapse", cls="minus-icon w-6 h-6"),
            for_=f"collapsible-{id}",
            cls=f"{between} items-center cursor-pointer"),
        P(answer, cls=f"overflow-hidden max-h-0 -mt-4 peer-checked/collapsible-{id}:max-h-[30rem] peer-checked/collapsible-{id}:mt-0 transition-all duration-300 ease-in-out s-body text-black/80 col-span-full"),
        cls=f"{col} gap-4 justify-between bg-soft-blue rounded-[1.25rem] py-4 lg:py-6 pl-6 lg:pl-8 pr-4 lg:pr-6")

def testimonial_card(idx, comment, name, role, company, image_src):
    return Div(
        P(comment, cls=f"m-body text-black"),
        Div(
            Div(Img(src=image_src, alt=f"Picture of {name}", width="112", height="112"),
                cls="rounded-full w-[2.625rem] lg:w-[3.5rem] lg:h-[3.5rem] h-[2.625rem]"),
            Div(
                P(name, cls=f"m-body text-black"),
                Div(
                    P(role),
                    Img(src=f"{icons}/dot.svg", alt="Dot separator", width="4", height="4"),
                    P(company),
                    cls=f"{gap2} xs-mono-body w-full"),
                cls="w-full"),
            cls=f"{center} justify-start gap-2"),
        id=f"testimonial-card-{idx+1}",
        cls=f"testimonial-card {col} flex-none whitespace-normal flex justify-between h-[22.8125rem] rounded-[1.5rem] items-start bg-soft-pink p-4 lg:p-8 {maxrem(36)} lg:w-[27rem]")

# File('assets/hero-shapes.svg')
# Section functions
def hero_section():
    return (
    Header(
        Nav(
            A(
                Img(src='/assets/logo.svg', alt='FastHTML', width='105', height='24'),
                href='#'),
            A('Try now', href='/', cls='bg-black text-white py-2 px-4 s-body rounded-[62.5rem] hover:bg-black/80 transition-colors duration-300 px-4 py-1 h-10 flex items-center justify-center'),
            cls='py-2 px-4 flex justify-between items-center rounded-full w-full max-w-[400px] bg-white/80 backdrop-blur-2xl'),
        cls='fixed top-0 w-full left-0 p-4 flex items-center justify-center z-50'),
    Section(
        Div(
            File('assets/hero-shapes.svg'),
            cls='absolute z-0 lg:-top-[15%] top-0 left-1/2 -translate-x-1/2 grid grid-cols-1 grid-rows-1 w-[120%] aspect-square max-w-[2048px] min-w-[900px]'),
        Div(
            Div(cls='lg:flex-1 max-lg:basis-[152px]'),
            Div(
                H1('Real web applications the right way', cls='heading-1 max-w-[800px]'),
                P('Built on solid web foundations, not the latest fads - with\nFastHTML you can get started on anything from simple dashboards to\nscalable web applications in minutes.',
                    cls='m-body max-w-[40rem] text-center'),
                cls=f'flex-1 {col} items-center justify-center gap-6 text-center w-full text-black'
            ),
            Div(
                A('See examples', cls='m-body px-4 py-1 rounded-full bg-black hover:bg-black/80 transition-colors duration-300 text-white h-[76px] w-full max-w-[350px] flex items-center justify-center', href='/'),
                A(
                    Img(src='/assets/intro-poster.png', width='240', height='120', cls='rounded-full w-[7.5rem] h-auto', alt='Youtube video poster'),
                    Span(
                        'Try now',
                        Span('4min 50sec', cls='s-body text-black/60'),
                        cls=f'text-black {col}'
                    ),
                    P(
                        Img(src='/assets/icons/youtube.svg', width='41', height='30', alt='Youtube icon'),
                        cls='flex-1 flex justify-center'
                    ),
                    cls='p-2 rounded-full bg-white hover:bg-white/80 transition-colors duration-300 h-[76px] w-full max-w-[350px] flex items-center gap-4',
                    href='/'),
                cls='flex-1 flex items-center justify-center content-center flex-wrap lg:gap-6 gap-4 m-body'),
            cls=f'{col} flex-1 relative px-4 lg:px-16'),
        cls=f'{col} relative w-full h-screen max-h-[1024px] min-h-[720px] overflow-hidden bg-grey')
    )

def code_demo(title, file_name, code_snippet, demo_content, is_active=False):
    demo_cls = f"{col} my-[2.66rem] p-4 flex-none whitespace-normal justify-between h-[22.8125rem] rounded-[1.5rem] items-start bg-soft-purple lg:p-8 w-full max-w-[40rem] lg:max-w-[27rem] lg:mx-[7rem] lg:my-[2.13rem]"
    return Div(
        Div(
            Div(
                Div(
                    P(file_name, cls="xs-mono-body flex items-center"),
                    Button(
                        Div(
                            Img(cls="button-content w-4 h-4", src="assets/icons/copy-icon.svg", alt="Copy"),
                            Span("Copied!", cls="absolute flex bg-inherit rounded-l-[0.5rem] items-center py-2 h-full right-0 copied-text overflow-hidden w-0 peer-clicked:w-fit s-body text-white/80 transition-transform transition-all duration-600 ease-out"),
                            cls="relative bg-black/20 rounded-[0.5rem] flex items-center p-2 h-8 w-fit"),
                        cls="copy-button"),
                    cls="w-full flex justify-between"),
                cls="bg-black/20 text-white/80 lg:max-w-[32.75rem] w-full max-w-[40rem] p-4 rounded-2xl"),
            Pre(
                Code(code_snippet, cls="python w-full mono-body"),
                id=f"{title.lower().replace(' ', '-')}-code-snippet",
                cls="code-snippet relative max-h-[25rem] overflow-y-auto hide-scrollbar"),
            Div(cls="absolute code-fade-out bottom-0 left-0 right-0 h-16 bg-gradient-to-b from-transparent to-[#3a2234] pointer-events-none"),
            cls=f"relative {col} gap-6 lg:max-w-[45rem] w-full overflow-hidden"),
        Div(demo_content, cls=demo_cls),
        aria_labelledby=f"tab-{title.lower().replace(' ', '-')}", role="tabpanel",
        cls=f"code-container pt-8 lg:pt-16 tab-panel relative hide-scrollbar toggle-element {col} lg:flex-row lg:justify-between overflow-hidden w-full lg:max-w-[1440px] xl:mx-auto {'hidden' if not is_active else ''}",
        id=f"{title.lower().replace(' ', '-')}-code-demo")

def tab_button(title, is_active=False):
    common_classes = "z-10 button-container flex-none relative w-[10.59375rem] h-[2.75rem] rounded-[62.5rem] flex items-center"
    active_classes = f"{common_classes} current active transition-all duration-300 text-white"
    inactive_classes = f"{common_classes} text-white/80 hover:text-white"

    return Li(
        Button(
            Div(title, cls="m-body w-max mx-auto"),
            id=f"tab-{title.lower().replace(' ', '-')}",
            cls="toggle-button w-full cursor-pointer",
            data_target=f"{title.lower().replace(' ', '-')}-code-demo",
            tabindex="-1" if not is_active else None,
            name=f"tab-{title.lower().replace(' ', '-')}"),
        role="tab", aria_selected="true" if is_active else "false",
        cls=active_classes if is_active else inactive_classes)

def component_preview_section():
    return Section(
        *[code_demo(title, file_name, code_snippet, demo_content, i == 0) for i, (title, file_name, code_snippet, demo_content) in enumerate(components)],
        Ul(
            *[tab_button(title, i == 0) for i, (title, _, _, _) in enumerate(components)],
            Div(id="highlighter", cls="z-0 highlighter w-[10.59375rem] absolute bg-white/20 h-[2.75rem] rounded-[62.5rem] transition-transform duration-300"),
            role="tablist", id="tab-list",
            cls="relative mt-12 flex text-white/80 flex-none rounded-[62.5rem] bg-black/20 p-2 max-w-full overflow-x-auto lg:mx-auto items-center hide-scrollbar lg:max-w-[43.375rem]"),
        cls="relative bg-purple px-4 lg:px-16 pb-24 -mt-8 lg:-mt-10 flex-col xl:items-center items-start gap-6 lg:gap-16 lg:pb-32 rounded-t-3xl lg:rounded-t-[2.5rem] overflow-x-hidden")

def tech_stack_item(name, icon_src, href):
    return A(
        Img(src=f"./assets/icons/stack/{icon_src}", alt=name, width="24", height="24"),
        P(name, cls="text-black/60"),
        href=href, target="_blank", rel="noopener noreferrer",
        cls=f"{gap2} items-center px-4 py-2 bg-white/60 rounded-full")

def stacked_card(title, description, tech_stack):
    return Div(
        Div(
            H3(title, cls="heading-3 mb-4"),
            P(description, cls="mb-12"),
            Div(
                *[tech_stack_item(name, icon, href) for name, icon, href in tech_stack],
                cls=f"{gap2} flex-wrap items-center"),
            cls=f"rounded-3xl bg-soft-green lg:p-12 p-6 {col} m-body")
    )

def stacked_cards_section():
    return Section(
        Div(
            Div(
                Div(
                    P("TECH STACK", cls="mono-body text-opacity-60"),
                    H2("Components and sections exemplified via FastHTML.", cls="text-black heading-2"),
                    P("Python developers can now create UI.", Br(), "The right way.", cls=f"l-body {maxrem(32)}"),
                    cls=f"{maxrem(50)} mx-auto {col} {center} text-center gap-6"),
                cls="py-8 lg:pt-16 px-4 lg:px-16 rounded-t-3xl lg:rounded-t-[2.5rem] bg-green"),
            cls="bg-purple sticky top-0 bottom-[calc(100%-300px)] w-full"),
        Div(
            Div(
                *[stacked_card(title, description, tech_stack) for title, description, tech_stack in stacked],
                id="stacked-cards", cls=f"{maxrem(50)} mx-auto"),
            cls="px-4 lg:px-16 w-full bg-green pt-8"),
        id="stacked-cards-section", cls="relative")

def samples_section():
    return section_wrapper(
            (section_header(
                "SAMPLES", "See FastHTML in action", "FastHTML can be used for everything from collaborative games to multi-modal UI. We've selected small self-contained examples for you to learn from.",
                max_width=40),
            Div(
                *[Div(
                    A(
                        Img(src=f"/assets/{svg}", alt=name),
                        Div(
                            P(name, cls="regular-body"),
                            Img(src=f"{icons}/arrow-up-right.svg", alt="Arrow right icon", cls="group-hover:translate-y-[-0.1rem] transition-all ease-in-out duration-300"),
                            cls=f"{gap2} transition-transform transform relative items-center mt-4 lg:mt-6"),
                        href="/", cls=f"{col} items-center"),
                    cls="group px-2"
                ) for name, svg in samples],
                cls="grid max-w-5xl lg:grid-cols-4 lg:max-w-7xl lg:gap-x-12 grid-cols-2 gap-x-4 gap-y-8 w-full mx-auto"),
            button("Discover all")),
        "grey")

def how_it_works_section():
    msg = "FastHTML comes in battery-included - create good-looking interactive modern web applications and deploy them in minutes"
    return section_wrapper_no_flex(
        (Div(
            section_header( "GET STARTED IN MINUTES", "The fastest way to create a real web application", msg),
            cls="max-w-[50rem] w-full mx-auto flex-col items-center text-center gap-6 mb-8 lg:mb-8"),
            Div(*[benefit(title, content) for title, content in benefits],
                cls=f"{col} w-full lg:flex-row gap-4 items-center lg:gap-8 max-w-7xl mx-auto")),
        "yellow")

def faq_section():
    return section_wrapper(
        Div(
            section_header( "FAQ", "Questions? Answers.", "Your top FastHTML questions clarified.",
                max_width=21),
            Div(
                *[faq_item(question, answer, i) for i, (question, answer) in enumerate(faqs)],
                cls=f"{col} gap-4 {maxrem(32)} transition ease-out delay-[300ms]"),
            cls=f"{section_base} w-full mx-auto lg:flex-row items-start max-w-7xl"),
        "blue")

def arrow(d):
    return Button(Img(src=f"assets/icons/arrow-{d}.svg", alt="Arrow left"),
           cls="disabled:opacity-40 transition-opacity", id=f"slide{d.capitalize()}", aria_label=f"Slide {d}")

def testimonials_section():
    return section_wrapper(
        Div(
            section_header(
                "LOVE IS IN THE AIR", "What our community says", "Experiences from FastHTML users around the globe.",
                max_width=21),
            Div(
                Div(
                    *[testimonial_card(i, *args) for i,args in enumerate(testimonials)],
                    id="carousel-container",
                    cls=f"hide-scrollbar {col} lg:flex-row gap-4 lg:gap-6 rounded-l-3xl xl:rounded-3xl w-full lg:overflow-hidden xl:overflow-hidden whitespace-nowrap"
                ),
                Div(
                    Div(arrow("left"), arrow("right"),
                        cls="w-[4.5rem] flex justify-between ml-auto"),
                    cls=f"hidden lg:flex xl:flex justify-start {maxrem(41)} py-6 pl-6 pr-20"),
                cls=f"max-h-fit {col} items-start lg:-mr-16 {maxpx(1440)} overflow-hidden"),
            cls=f"{section_base} {maxrem(90)} mx-auto lg:flex-row items-start"),
        "pink")

def footer_link(text, href, **kw):
    return Li(A(text, href=href, cls=f"{gap2} items-center hover:text-white border-b border-b-transparent hover:border-b-white", **kw))

def footer():
    return Section(
        Div(
            Div(
                P("© 2024 FastHTML. All rights reserved.", cls="mr-auto"),
                Nav(
                    Ul(
                    footer_link("Join Discord", "/"),
                    footer_link("Docs", "/"),
                    footer_link("Site credit", "https://tinloof.com/", target="_blank", rel="noopener noreferrer"),
                    cls="flex max-lg:flex-col max-lg:items-start gap-4 lg:gap-6 flex-wrap")),
                cls="relative z-[1] mono-s flex max-lg:flex-col gap-6 text-white/80 px-4 lg:px-16 pb-16"),
            Div(
                Div(
                    File("assets/footer-shapes.svg"),
                    cls=f"absolute z-0 lg:-top-[15%] top-0 left-1/2 -translate-x-1/2 grid grid-cols-1 grid-rows-1 lg:w-[150%] w-[200%] aspect-square max-w-none min-w-max"),
                Img(src="/assets/footer-path.svg", alt="FastHTML logo", cls="relative w-full h-auto"),
                cls=f"relative z-0 w-full px-4 lg:px-16 pb-1 {col} flex-1 justify-end"),
            cls=f"relative w-full h-[420px] lg:h-[600px] {col} pt-8 lg:pt-12 rounded-t-3xl lg:rounded-t-[2.5rem] bg-black overflow-hidden -mt-8 lg:-mt-10"))

hdrs = [
    Meta(name='description', content='Real web applications the right way'),
    *Favicon('assets/favicon.ico', 'assets/favicon-dark.ico'),
    *Socials(title='FastHTML',
        description='Real web applications the right way',
        site_name='fasthtml.answer.ai',
        image='https://fasthtml.vercel.app/assets/og-image.png',
        url='https://fasthtml.vercel.app/'),
    Link(href='css/main.css', rel='stylesheet'),
    Script(src='https://cdn.tailwindcss.com'),
    Script(src='js/tailwind.config.js'),
    Link(href='css/stack.css', rel='stylesheet'),
    Link(href='css/preview-stack.css', rel='stylesheet'),
    Link(href='css/highlighter-theme.css', rel='stylesheet')]

bodykw = {"class": "relative bg-grey font-geist text-black/80 font-details-off"}
app,rt = fast_app(hdrs=hdrs, default_hdrs=False, bodykw=bodykw)

@rt("/")
def get():
    scripts = (Script(src='/js/stack.js'),
        Script(src='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js'),
        Script(src='https://cdnjs.cloudflare.com/ajax/libs/highlightjs-line-numbers.js/2.8.0/highlightjs-line-numbers.min.js'),
        Script(src='js/pythonHighlighter.js'),
        Script(src='js/togglePreview.js'),
        Script(src='js/codeOverflow.js'),
        Script(src='js/copyCode.js'),
        Script(src='js/carouselScroll.js'))

    return (Title("FastHTML - Real web applications the right way"), 
        Main(
            hero_section(),
            component_preview_section(),
            stacked_cards_section(),
            samples_section(),
            how_it_works_section(),
            faq_section(),
            testimonials_section(),
            footer()),
            *scripts
    )

run_uv()
