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

def maxpx (px ): return f"w-full max-w-[{px}px]"
def maxrem(rem): return f"w-full max-w-[{rem}rem]"

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

def video_button(txt, poster_src, video_duration, youtube_id, poster_alt="Video poster", youtube_icon_src="/assets/icons/youtube.svg", max_width="350px"):
    return (
        # 'Popup container'
        Div(
            Div(
                # 'Pastel green top bar',
                Div(
                    H3(txt, cls='text-green-800 font-semibold'),
                        # 'Close button',
                        Button('×', id='closePopup', cls='text-green-800 hover:text-green-950'),
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
        ),
        # Button link
        A(
            Img(src=poster_src, width='240', height='120', cls='rounded-full w-[7.5rem] h-auto', alt=poster_alt),
            Span(
                txt, Span(video_duration, cls='s-body text-black/60'),
                cls=f'text-black {col}'),
            P(
                Img(src=youtube_icon_src, width='41', height='30', alt='Youtube icon'),
                cls=f'flex-1 {center}'),
            cls=f'{inset} p-2 rounded-full bg-white hover:bg-white/80 transition-colors duration-300 h-[76px] w-full max-w-[{max_width}] {center} gap-4',
            href="#", id='videoLink'),        
        Script("""
            const videoLink = document.getElementById('videoLink');
            const videoPopup = document.getElementById('videoPopup');
            const closePopup = document.getElementById('closePopup');
            const youtubeVideo = document.getElementById('youtubeVideo');

            videoLink.addEventListener('click', (e) => {
                e.preventDefault();
                youtubeVideo.src = 'https://www.youtube.com/embed/{youtube_id}';
                videoPopup.classList.remove('hidden');
            });

            closePopup.addEventListener('click', () => {
                youtubeVideo.src = '';
                videoPopup.classList.add('hidden');
            });

            videoPopup.addEventListener('click', (e) => {
                if (e.target === videoPopup) {
                youtubeVideo.src = '';
                videoPopup.classList.add('hidden');
                }
            });""".replace('{youtube_id}', youtube_id)
        )
    )