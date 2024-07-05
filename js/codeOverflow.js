function checkOverflow(codeContainer) {
  const fadeOutElement =
    codeContainer.parentElement.querySelector(".code-fade-out");

  if (
    Math.floor(codeContainer.getBoundingClientRect().bottom) !==
    Math.floor(codeContainer.childNodes[0].getBoundingClientRect().bottom)
  ) {
    fadeOutElement.classList.remove("hidden");
  } else {
    fadeOutElement.classList.add("hidden");
  }
}

checkOverflow(document.querySelector(".code-snippet"));

const codeSnippets = document.querySelectorAll(".code-snippet");
codeSnippets.forEach((container) => {
  container.addEventListener("scroll", () => checkOverflow(container));
});
