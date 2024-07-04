const tabButtons = document.querySelectorAll(".toggle-button");
const codeContainers = document.querySelectorAll(".code-container");

const container = document.querySelector(".button-container");
tabButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const highlighter = document.getElementById("highlighter");
    // Remove 'active' class from all button containers
    codeContainers.forEach((container) => {
      container.style.display = "none";
    });
    tabButtons.forEach((btn) => {
      btn.parentElement.classList.remove("active");
      btn.parentElement.classList.add("text-white/80");
      btn.parentElement.classList.add("hover:text-white");
      btn.parentElement.classList.remove("text-purple");
    });

    // Add 'active' class to the clicked button
    const activeCodeContainer = document.getElementById(button.dataset.target);
    activeCodeContainer.style.display = "flex";
    button.parentElement.classList.add("active");
    button.parentElement.classList.add("text-purple");

    button.parentElement.classList.remove("text-white/80");
    button.parentElement.classList.remove("hover:text-white");

    // Move highlighter to the clicked button
    const buttonRect = button.parentElement.getBoundingClientRect();
    const containerRect = container.getBoundingClientRect();
    const translateX = buttonRect.x - containerRect.x;

    highlighter.style.transform = `translateX(${translateX}px)`;
  });
});
