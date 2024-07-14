## Special ids used

### Ids related to tabs in the "Component preview" section

#### Tab ids
In the "Component preview" section, each card has an id (e.g. [card-code-demo](https://github.com/tinloof/fasthtml/blob/11497eec3716ecd7b3f95df1cc4d1f5956516a7d/index.html#L268))
for the tab selection to be able to target it.
The target is set in the tab button through the `data-target` attribute).


#### Tab list id in `tab-list`
The list of tab buttons has an id `tab-list` used to identify the element in JavaScript and implement the tab selection logic.


#### Tab buttons ids (e.g. `tab-card`)
These ids are combinned with `aria-labelledby` to make it clear for screen readers which tab is being selected.

### Ids in the "Stacked cards" section

#### `stacked-cards` id
This id is targetted by both CSS and JavaScript to implement the component behaviour.

### Ids in the "FAQ section"

#### Collapsible ids (e.g. [`collapsible-1`](https://github.com/tinloof/fasthtml/blob/11497eec3716ecd7b3f95df1cc4d1f5956516a7d/index.html#L1390))

These ids are targetted by CSS to implement the collapsibles behaviour. 


### Ids in the "Testimonials section"

All ids inside this section are targetted by JavaScript to implement the carousel scrolling behaviour.

## Special classNames used

### "Code preview" section
- `.code-snippet`: targetted by JavaScript for the code blur overflow logic.
- `.toggle.button`, `.code-container`, `.button-container`: all targetted by JavaScript for the tab selection logic.


### "FAQ" section
- `.endicator`: targetted by JavaScript for the carousel logic.


### Other special classNames
Any non-tailwind className is targetted in `main.css` for custom styling.
