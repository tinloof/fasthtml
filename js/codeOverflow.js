function checkOverflow(codeContainer) {
  const fadeOutElement =
    codeContainer.parentElement.querySelector(".code-fade-out");

  if (
    Math.floor(codeContainer.getBoundingClientRect().bottom) <
    Math.floor(codeContainer.childNodes[0].getBoundingClientRect().bottom)
  ) {
    fadeOutElement.style.display = "block";
  } else {
    fadeOutElement.style.display = "none";
  }
}

checkOverflow(document.querySelector(".code-snippet"));

const codeSnippets = document.querySelectorAll(".code-snippet");
codeSnippets.forEach((container) => {
  container.addEventListener("scroll", () => checkOverflow(container));
});
