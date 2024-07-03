document.querySelectorAll(".toggle-button").forEach((button) => {
  button.addEventListener("click", () => {
    // Hide all elements
    document.querySelectorAll(".toggle-element").forEach((element) => {
      element.classList.add("hidden");
      element.classList.remove("flex");
    });

    // Show the target element
    const targetId = button.getAttribute("data-target");

    const targetElement = document.getElementById(targetId);

    if (targetElement) {
      targetElement.classList.remove("hidden");
      targetElement.classList.add("flex");
    }
    document.querySelectorAll(".button-container").forEach((container) => {
      container.classList.remove("bg-soft-purple");
      container.classList.remove("text-purple");
      container.classList.add("text-white/80");
    });

    const selectedContainer = button.closest(".button-container");

    selectedContainer.classList.remove("text-white/80");
    selectedContainer.classList.add("bg-soft-purple");
    selectedContainer.classList.add("text-purple");
  });
});
