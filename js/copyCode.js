document.querySelectorAll(".copy-button").forEach((button) => {
  button.addEventListener("click", async () => {
    const codeContainer = button.closest(".code-container");
    // const buttonContent = button.querySelector(".button-content");
    const copiedText = button.querySelector(".copied-text");
    const codeSnippet = codeContainer.querySelector(".code-snippet").innerText;

    copiedText.parentElement.classList.add("rounded-r-[0.5rem]");
    copiedText.parentElement.classList.remove("rounded-[0.5rem]");
    copiedText.classList.add("w-fit");
    copiedText.classList.add("px-1");
    copiedText.classList.remove("w-0");

    copiedText.style.transform = "translateX(-2rem)";

    try {
      button.disabled = true;
      await navigator.clipboard.writeText(codeSnippet);

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
