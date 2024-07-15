from fasthtml.common import *
from itertools import starmap

icons = 'assets/icons'
col = "flex flex-col"
center = "flex items-center"
between = "flex justify-between"
gap2 = "flex gap-2"
# inset = "shadow-[0_3px_2px_rgba(255,255,255,0.9),0_5px_5px_rgba(0,0,0,0.3)]"
# bnset = "shadow-[0_3px_2px_rgba(255,255,255,0.1),0_4px_4px_rgba(0,0,0,0.7)]"
inset = "shadow-[0_1px_1px_rgba(255,255,255,0.3),0_2px_2px_rgba(0,0,0,0.1)]"
bnset = "shadow-[0_1px_1px_rgba(255,255,255,0.03),0_2px_2px_rgba(0,0,0,0.2)]"
# inset = "shadow-[inset_0_-4px_8px_rgba(0,0,0,0.2)]"

section_base1= "pt-8 px-4 pb-24 gap-8 lg:gap-16 lg:pt-16 lg:px-16"
section_base =f"{col} {section_base1}"

def maxpx (px ): return f"w-full max-w-[{px}px]"
def maxrem(rem): return f"w-full max-w-[{rem}rem]"

def section_wrapper(content, bg_color, xtra="", flex=True):
    return Section(content, cls=f"bg-{bg_color} {section_base1} {col if flex else ''} -mt-8 lg:-mt-16 items-center rounded-t-3xl lg:rounded-t-[2.5rem] relative {xtra}")

def section_header(mono_text, heading, subheading, max_width=32, center=True):
    pos = 'items-center text-center' if center else 'items-start text-start'
    return Div(
        P(mono_text, cls="mono-body text-opacity-60"),
        H2(heading, cls=f"text-black heading-2 {maxrem(max_width)}"),
        P(subheading, cls=f"l-body {maxrem(max_width)}"),
        cls=f"{maxrem(50)} mx-auto {col} {pos} gap-6")

def arrow(d):
    return Button(Img(src=f"assets/icons/arrow-{d}.svg", alt="Arrow left"),
           cls="disabled:opacity-40 transition-opacity", id=f"slide{d.capitalize()}", aria_label=f"Slide {d}")

def carousel(items, id="carousel-container", extra_classes=""):
    carousel_content = Div(*items, id=id,
        cls=f"hide-scrollbar {col} lg:flex-row gap-4 lg:gap-6 rounded-l-3xl xl:rounded-3xl w-full lg:overflow-hidden xl:overflow-hidden whitespace-nowrap {extra_classes}")

    arrows = Div(
        Div(arrow("left"), arrow("right"),
            cls=f"w-[4.5rem] {between} ml-auto"),
        cls=f"hidden lg:flex xl:flex justify-start {maxrem(41)} py-6 pl-6 pr-20")
    return Div(carousel_content, arrows, cls=f"max-h-fit {col} items-start lg:-mr-16 {maxpx(1440)} overflow-hidden")

def testimonial_card(idx, comment, name, role, company, image_src):
    return Div(
        P(comment, cls=f"m-body text-black"),
        Div(
            Div(Img(src=image_src, alt=f"Picture of {name}", width="112", height="112"),
                cls="rounded-full w-11 h-11 lg:w-14 lg:h-14"),
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
        cls=f"testimonial-card {col} flex-none whitespace-normal flex justify-between h-96 rounded-3xl items-start bg-soft-pink p-4 lg:p-8 {maxrem(36)} lg:w-96")

def stack_item(name, icon_src, href):
    return A(
        Img(src=f"./assets/icons/stack/{icon_src}", alt=name, width="24", height="24"),
        P(name, cls="text-black/60"),
        href=href, target="_blank", rel="noopener noreferrer",
        cls=f"{gap2} items-center px-4 py-2 bg-white/60 rounded-full {inset}")

def stacked_card(title, description, stacks, color):
    return Div(
        Div(
            H3(title, cls="heading-3 mb-4"),
            P(description, cls="mb-12"),
            Div(*starmap(stack_item, stacks),
                cls=f"{gap2} flex-wrap items-center"),
            cls=f"rounded-3xl {color} lg:p-12 p-6 {col} m-body")
    )

def accordion(id, question, answer, question_cls="", answer_cls="", container_cls=""):
    pc = f"peer-checked/collapsible-{id}"
    return Div(
        Input(id=f"collapsible-{id}", type="checkbox", cls=f"collapsible-checkbox peer/collapsible-{id} hidden"),
        Label(
            P(question, cls=f"flex-grow {question_cls}"),
            Img(src=f"{icons}/plus-icon.svg", alt="Expand", cls=f"plus-icon w-6 h-6"),
            Img(src=f"{icons}/minus-icon.svg", alt="Collapse", cls=f"minus-icon w-6 h-6"),
            _for=f"collapsible-{id}",
            cls="flex items-center cursor-pointer"),
        P(answer, cls=f"overflow-hidden max-h-0 -mt-4 {pc}:max-h-[30rem] {pc}:mt-0 transition-all duration-300 ease-in-out {answer_cls}"),
        cls=container_cls)

def video_player(txt):
    return (
        # Video Popup container - TODO make pretty
        Div(
            Div(
                # 'Pastel green top bar',
                Div(
                    H3(txt, cls='text-green-800 font-semibold'),
                        # 'Close button',
                        Button('X', id='closePopup', cls='text-green-800 hover:text-green-950'),
                    cls='bg-green-200 p-2 flex justify-between items-center'
                ),
                # 'YouTube video iframe',
                Div(
                Iframe(id='youtubeVideo', width='560', height='315', src='', frameborder='0', allowfullscreen=''),
                cls='p-4'
                ),
                cls='bg-white rounded-lg shadow-lg overflow-hidden'
            ),
            id='videoPopup',
            cls='hidden fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center'
        )
    )

yt_frame = """<iframe id="youtubeFrame" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""
def video_button(txt, poster_src, video_duration, video_id, poster_alt="Video poster", youtube_icon_src="/assets/icons/youtube.svg", max_width="350px"):
    return (
        A(
            Img(src=poster_src, width='240', height='120', cls='rounded-full w-[7.5rem] h-auto', alt=poster_alt),
            Span(txt, Span(video_duration, cls='s-body text-black/60'), cls=f'text-black {col}'),
            P(Img(src=youtube_icon_src, width='41', height='30', alt='Youtube icon'), cls=f'flex-1 {center}'),
            Script(f"""
                me().on('click', (e) => {{
                    e.preventDefault();
                    me('#videoOverlay').classRemove('hidden').classAdd('flex');
                    me('#youtube-player').setAttribute('src', 'https://www.youtube.com/embed/{video_id}');
                }});"""),
            id="openVideo", href='#',
            cls=f'{inset} p-2 rounded-full bg-white hover:bg-white/80 transition-colors duration-300 h-[76px] w-full max-w-[{max_width}] {center} gap-4'
        ),
        Div(
            Iframe(id="youtube-player", src="", cls="w-full aspect-video", allowfullscreen=True, allow="autoplay; encrypted-media"),
            Button("Close",
                Script("""
                    me().on('click', () => {
                        me('#videoOverlay').classRemove('flex').classAdd('hidden');
                        me('#youtube-player').setAttribute('src', '');
                    });"""),
                id="closeVideo", cls="mt-4 bg-soft-pink text-black font-bold py-2 px-4 rounded"
            ),
            Script("document.addEventListener('keydown', (e) => { if (e.key === 'Escape') me('#closeVideo').send('click'); });"),
            id="videoOverlay", cls="fixed inset-0 bg-black bg-opacity-50 hidden items-center justify-center z-50"
        )
    )

