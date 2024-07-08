const preformattedCode = {
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

document.querySelectorAll(".copy-button").forEach((button) => {
  button.addEventListener("click", async () => {
    const codeContainer = button.closest(".code-container");
    const codeId = codeContainer.querySelector("pre").id;
    // const buttonContent = button.querySelector(".button-content");
    const copiedText = button.querySelector(".copied-text");

    copiedText.parentElement.classList.add("rounded-r-[0.5rem]");
    copiedText.parentElement.classList.remove("rounded-[0.5rem]");
    copiedText.classList.add("w-fit");
    copiedText.classList.add("px-1");
    copiedText.classList.remove("w-0");

    copiedText.style.transform = "translateX(-2rem)";

    try {
      button.disabled = true;
      await navigator.clipboard.writeText(preformattedCode[codeId]);

      setTimeout(() => {
        copiedText.style.transform = "translateX(0rem)";

        copiedText.addEventListener("transitionend", () => {
          copiedText.classList.add("w-0");
          copiedText.classList.remove("w-fit");
          copiedText.classList.remove("px-1");
          copiedText.parentElement.classList.add("rounded-[0.5rem]");
          copiedText.parentElement.classList.remove("rounded-r-[0.5rem]");
          button.disabled = false;
        });
      }, 2000);
    } catch {
      console.error("Failed to copy the code to the clipboard");
    }
  });
});
