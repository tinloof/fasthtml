// Bundled JavaScript, generated via `npx vite build`, do not edit manually

(function () {
  const o = document.createElement("link").relList;
  if (o && o.supports && o.supports("modulepreload")) return;
  for (const n of document.querySelectorAll('link[rel="modulepreload"]')) e(n);
  new MutationObserver((n) => {
    for (const i of n)
      if (i.type === "childList")
        for (const c of i.addedNodes)
          c.tagName === "LINK" && c.rel === "modulepreload" && e(c);
  }).observe(document, { childList: !0, subtree: !0 });
  function s(n) {
    const i = {};
    return (
      n.integrity && (i.integrity = n.integrity),
      n.referrerPolicy && (i.referrerPolicy = n.referrerPolicy),
      n.crossOrigin === "use-credentials"
        ? (i.credentials = "include")
        : n.crossOrigin === "anonymous"
        ? (i.credentials = "omit")
        : (i.credentials = "same-origin"),
      i
    );
  }
  function e(n) {
    if (n.ep) return;
    n.ep = !0;
    const i = s(n);
    fetch(n.href, i);
  }
})();
(function () {
  const t = document.getElementById("stacked-cards-section"),
    o = t.children[0],
    s = document.getElementById("stacked-cards"),
    e = Array.from(s.children),
    n = e.map((r) => r.children.item(0).getBoundingClientRect().height);
  if (
    (function () {
      let r = !1;
      return (
        (function (a) {
          (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(
            a
          ) ||
            /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(
              a.substr(0, 4)
            )) &&
            (r = !0);
        })(navigator.userAgent || navigator.vendor || window.opera),
        r
      );
    })() ||
    window.innerWidth < 1024
  ) {
    (s.style.gap = "var(--cardMargin)"),
      e.forEach((r) => (r.style.position = "relative")),
      (o.style.position = "relative");
    return;
  }
  const c = (r, a) => {
    const p = window.innerHeight,
      u = window.scrollY,
      f = r.offsetTop,
      g = r.offsetHeight,
      d = u + p - f - a,
      v = Math.round(d / ((p + g) / 100));
    return Math.min(100, Math.max(0, v));
  };
  e.forEach((r) => {
    r.style.top = `calc(${
      o.getBoundingClientRect().height + "px"
    } + var(--cardsSectionGap) + calc(var(--index) * var(--cardTopPadding)))`;
  });
  const l = +getComputedStyle(t)
    .getPropertyValue("--cardsHeaderBottomStop")
    .slice(0, -2);
  document.addEventListener("scroll", function () {
    const r = c(e[1], 64 + t.offsetTop),
      a = c(e[2], 128 + t.offsetTop);
    Math.abs(
      o.getBoundingClientRect().bottom - t.getBoundingClientRect().bottom
    ) <
    l + n[2]
      ? (o.children.item(
          0
        ).style.paddingBottom = `calc(var(--cardsHeaderBottomStop) + ${
          n[2] + "px"
        })`)
      : (o.children.item(0).style.paddingBottom = ""),
      (e[0].children.item(0).style.scale =
        1 - (0.1 * r) / 100 - (0.1 * a) / 100),
      (e[0].children.item(0).style.opacity =
        1 - (0.1 * r) / 100 - (0.1 * a) / 100),
      (e[0].children.item(0).style.filter = `blur(${
        (10 * r) / 100 + (10 * a) / 100
      }px)`),
      (e[0].style.paddingBottom = `calc(
      var(--cardTopPadding) * 2 - ${n[0] - n[2]}px
    )`),
      (e[1].children.item(0).style.scale = 1 - (0.1 * a) / 100),
      (e[1].children.item(0).style.opacity = 1 - (0.1 * a) / 100),
      (e[1].children.item(0).style.filter = `blur(${(10 * a) / 100}px)`),
      (e[1].style.paddingBottom = `calc(
      var(--cardTopPadding) - ${n[1] - n[2]}px
    )`);
  });
})();
(function () {
  const t = (n) => {
      const i = document.getElementById("stacked-cards-component-demo"),
        c = n.children.item(0),
        l = i.getBoundingClientRect(),
        r = c.getBoundingClientRect();
      return r.bottom < l.bottom
        ? 100
        : r.top > l.bottom
        ? 0
        : Math.round((Math.abs(l.bottom - r.top) / r.height) * 100);
    },
    o = document.getElementById("stacked-cards-component-demo"),
    s = document.getElementById("preview-stacked-cards"),
    e = Array.from(s.children);
  o.addEventListener("scroll", function () {
    const n = t(e[1]),
      i = t(e[2]);
    (e[0].children.item(0).style.scale = 1 - (0.1 * n) / 100 - (0.1 * i) / 100),
      (e[0].children.item(0).style.opacity =
        1 - (0.1 * n) / 100 - (0.1 * i) / 100),
      (e[0].children.item(0).style.filter = `blur(${
        (10 * n) / 100 + (10 * i) / 100
      }px)`),
      (e[1].children.item(0).style.scale = 1 - (0.1 * i) / 100),
      (e[1].children.item(0).style.opacity = 1 - (0.1 * i) / 100),
      (e[1].children.item(0).style.filter = `blur(${(10 * i) / 100}px)`);
  });
})();
hljs.registerLanguage("python-custom", (t) => {
  var o = t.getLanguage("python");
  (o.name = "Python Custom"),
    o.contains.push({
      className: "decorator",
      begin: "/@/",
      end: "/$/",
      contains: [
        { className: "symbol", match: "@" },
        { className: "name", begin: /[\w\.]+/ },
        { className: "params", begin: /\(/, end: /\)/ },
      ],
    });
  var s = { className: "yellow-char", begin: /\*/ },
    e = { className: "white-char", begin: /[,.:()@]/ },
    n = {
      className: "attribute",
      begin: /\./,
      end: /[\w]+/,
      contains: [{ begin: /\w+/, className: "attr-name" }],
    };
  return (
    (o.keywords.built_in = o.keywords.built_in.filter((i) => i !== "id")),
    o.contains.push(e),
    o.contains.push(n),
    o.contains.push(s),
    o
  );
});
hljs.highlightAll();
hljs.initLineNumbersOnLoad();
document.addEventListener("DOMContentLoaded", function () {
  const t = document.querySelectorAll(".toggle-button"),
    o = document.querySelectorAll(".code-container"),
    s = document.getElementById("tab-list"),
    e = s.getBoundingClientRect(),
    n = document.querySelector(".button-container");
  t.forEach((i) => {
    i.addEventListener("click", () => {
      const c = i.parentElement,
        l = c.getBoundingClientRect(),
        r = l.left - e.left + l.width / 2 - e.width / 2;
      s.scrollBy({ left: r, behavior: "smooth" });
      const a = document.getElementById("highlighter");
      o.forEach((d) => {
        d.style.display = "none";
      }),
        t.forEach((d) => {
          (d.parentElement.ariaSelected = !1),
            d.parentElement.classList.remove("active"),
            d.parentElement.classList.add("text-white/80"),
            d.parentElement.classList.add("hover:text-white"),
            d.parentElement.classList.remove("text-white");
        });
      const p = document.getElementById(i.dataset.target);
      (p.style.display = "flex"),
        (c.ariaSelected = !0),
        c.classList.add("active"),
        c.classList.add("text-white"),
        c.classList.remove("text-white/80");
      const u = c.getBoundingClientRect(),
        f = n.getBoundingClientRect(),
        g = u.x - f.x;
      a.style.transform = `translateX(${g}px)`;
    });
  }),
    t.forEach((i) => {
      i.addEventListener("click", () => {});
    });
});
function y(t) {
  const o = t.parentElement.querySelector(".code-fade-out");
  let s = t.querySelector("code");
  Math.floor(t.getBoundingClientRect().bottom) <
  Math.floor(s.getBoundingClientRect().bottom)
    ? (o.style.display = "block")
    : (o.style.display = "none");
}
y(document.querySelector(".code-snippet"));
const w = document.querySelectorAll(".code-snippet");
w.forEach((t) => {
  t.addEventListener("scroll", () => y(t));
});
const k = {
  "button-code-snippet": `
@rt("/")
async def get():
  add = Form(Group(mk_input(), Button("Add")), hx_post="/", target_id='todo-list', hx_swap="beforeend")
  card = Card(Ul(*todos(), id='todo-list', header=add, footer=Div(id=id_curr)), title = 'Todo list')
  return Title(title), Main(H1(title), card, cls='container')
`,
  "card-code-snippet": `
@rt("/")
async def put(todo: Todo): 
  return todos.upsert(todo), clr_details()

@rt("/todos/{id}")
async def get(id:int):
  todo = todos.get(id)
  btn = Button('delete', hx_delete=f'/todos/{todo.id}', target_id=tid(todo.id), hx_swap="outerHTML")
  return Div(Div(todo.title), btn)

if __name__ == '__main__': 
  uvicorn.run("main:app", host='0.0.0.0', port=int(os.getenv("PORT", default=5001))
`,
  "accordion-code-snippet": `
@rt("/")
async def post(todo:Todo): 
  return todos.insert(todo), mk_input(hx_swap_oob='true')

@rt("/edit/{id}")
async def get(id:int):
  res = Form(Group(Input(id="title"), 
      Button("Save")),
      Hidden(id="id"), 
      Checkbox(id="done", label='Done'),
      hx_put="/", 
      target_id=tid(id), 
      id="edit")
  return fill_form(res, todos.get(id))
`,
  "stacked-cards-code-snippet": `
@rt("/{fname:path}.{ext:static}")
async def get(fname:str, ext:str): 
  return FileResponse(f'{fname}.{ext}')

def mk_input(**kw): 
  return Input(id="new-title", name="title", placeholder="New Todo", **kw)

def clr_details(): 
    return Div(hx_swap_oob='innerHTML', id=id_curr)

@rt("/")
async def get():
  add = Form(Group(mk_input(), Button("Add")), hx_post="/", target_id='todo-list', hx_swap="beforeend")
  card = Card(Ul(*todos(), id='todo-list'), header=add, footer=Div(id=id_curr)),
  title = 'Todo list'
  return Title(title), Main(H1(title), card, cls='container')
`,
};
document.querySelectorAll(".copy-button").forEach((t) => {
  t.addEventListener("click", async () => {
    const s = t.closest(".code-container").querySelector("pre").id,
      e = t.querySelector(".copied-text");
    e.parentElement.classList.add("rounded-r-[0.5rem]"),
      e.parentElement.classList.remove("rounded-[0.5rem]"),
      e.classList.add("w-fit"),
      e.classList.add("px-1"),
      e.classList.remove("w-0"),
      (e.style.transform = "translateX(-2rem)");
    try {
      (t.disabled = !0),
        await navigator.clipboard.writeText(k[s]),
        setTimeout(() => {
          (e.style.transform = "translateX(0rem)"),
            e.addEventListener("transitionend", () => {
              e.classList.add("w-0"),
                e.classList.remove("w-fit"),
                e.classList.remove("px-1"),
                e.parentElement.classList.add("rounded-[0.5rem]"),
                e.parentElement.classList.remove("rounded-r-[0.5rem]"),
                (t.disabled = !1);
            });
        }, 2e3);
    } catch {
      console.error("Failed to copy the code to the clipboard");
    }
  });
});
const m = document.getElementById("carousel-container"),
  x = m.querySelectorAll(".testimonial-card"),
  E = document.querySelectorAll(".endicator"),
  b = { root: m, rootMargin: "0px", threshold: 1 };
let h = -1;
const L = new IntersectionObserver((t) => {
    t.forEach((o) => {
      o.isIntersecting && (h = Number(o.target.id.split("-")[2]));
    });
  }, b),
  B = new IntersectionObserver((t) => {
    t.forEach((o) => {
      const s = o.target.dataset.bound;
      o.isIntersecting
        ? (s === "left" && (document.getElementById("slideLeft").disabled = !0),
          s === "right" &&
            (document.getElementById("slideRight").disabled = !0))
        : (s === "left" && (document.getElementById("slideLeft").disabled = !1),
          s === "right" &&
            (document.getElementById("slideRight").disabled = !1));
    });
  }, b);
E.forEach((t) => B.observe(t));
x.forEach((t) => {
  L.observe(t);
});
document.getElementById("slideRight").addEventListener("click", function () {
  const t = document.getElementById(`testimonial-card-${h + 1}`);
  if (t) {
    const o = m.scrollLeft + t.offsetLeft - m.offsetLeft;
    m.scrollBy({ left: o, behavior: "smooth" });
  }
});
document.getElementById("slideLeft").addEventListener("click", function () {
  const t = document.getElementById(`testimonial-card-${h - 1}`);
  if (t) {
    const o = m.scrollLeft - t.offsetLeft + m.offsetLeft;
    m.scrollBy({ left: -o, behavior: "smooth" });
  }
});
