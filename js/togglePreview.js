document.addEventListener("DOMContentLoaded", function () {
  const tabButtons = document.querySelectorAll(".toggle-button");
  const codeContainers = document.querySelectorAll(".code-container");
  const tabList = document.getElementById("tab-list");
  const tabListRect = tabList.getBoundingClientRect();

  // The first button container is our reference, since the highlighter
  // is initialized there. Any translations happen over this position.
  const firstButtonContainer = document.querySelector(".button-container");

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const currentButtonContainer = button.parentElement;
      const currentButtonContainerRect =
        currentButtonContainer.getBoundingClientRect();
      // Scroll the tab list to the clicked button
      // Try to center it, go as far as possible
      const offset =
        currentButtonContainerRect.left -
        tabListRect.left +
        currentButtonContainerRect.width / 2 -
        tabListRect.width / 2;
      tabList.scrollBy({ left: offset, behavior: "smooth" });

      // Make highlighter follow the clicked button
      const highlighter = document.getElementById("highlighter");
      // Remove 'active' class from all button containers
      codeContainers.forEach((container) => {
        container.style.display = "none";
      });

      tabButtons.forEach((btn) => {
        btn.parentElement.ariaSelected = false;
        btn.parentElement.classList.remove("active");
        btn.parentElement.classList.add("text-white/80");
        btn.parentElement.classList.add("hover:text-white");
        btn.parentElement.classList.remove("text-white");
      });

      // Add 'active' class to the clicked button
      const activeCodeContainer = document.getElementById(
        button.dataset.target
      );
      activeCodeContainer.style.display = "flex";
      currentButtonContainer.ariaSelected = true;
      currentButtonContainer.classList.add("active");
      currentButtonContainer.classList.add("text-white");
      currentButtonContainer.classList.remove("text-white/80");

      // Move highlighter to the clicked button
      const buttonRect = currentButtonContainer.getBoundingClientRect();
      const firstButtonContainerRect =
        firstButtonContainer.getBoundingClientRect();

      const translateX = buttonRect.x - firstButtonContainerRect.x;

      highlighter.style.transform = `translateX(${translateX}px)`;
    });
  });

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {});
  });
});
