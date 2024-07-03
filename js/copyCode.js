document.querySelectorAll(".copy-button").forEach((button) => {
  button.addEventListener("click", async () => {
    const codeContainer = button.closest(".code-container");
    const buttonContent = button.querySelector(".button-content");
    const copiedText = button.querySelector(".copied-text");
    const codeSnippet = codeContainer.querySelector(".code-snippet").innerText;

    buttonContent.classList.add("hidden");
    copiedText.classList.remove("hidden");

    try {
      button.disabled = true;
      await navigator.clipboard.writeText(codeSnippet);

      setTimeout(() => {
        buttonContent.classList.remove("hidden");
        copiedText.classList.add("hidden");
        button.disabled = false;
      }, 2000);
    } catch {
      console.error("Failed to copy the code to the clipboard");
    }
  });
});
