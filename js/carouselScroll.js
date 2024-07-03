document.getElementById("slideLeft").addEventListener("click", function () {
  document.querySelector(".carousel-container").scrollBy({
    left: -450,
    behavior: "smooth",
  });
});

document.getElementById("slideRight").addEventListener("click", function () {
  document.querySelector(".carousel-container").scrollBy({
    left: 450,
    behavior: "smooth",
  });
});
