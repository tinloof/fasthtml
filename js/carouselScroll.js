const container = document.getElementById("carousel-container");
const elements = container.querySelectorAll(".testimonial-card");

const options = {
  root: container,
  rootMargin: "0px",
  threshold: 1,
};

// From specs, there's only ever gonna be one card fully visible at a time
let visibleCardNum = -1;
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      visibleCardNum = Number(entry.target.id.split("-")[2]);
    }
  });
}, options);

elements.forEach((element) => {
  observer.observe(element);
});

document.getElementById("slideRight").addEventListener("click", function () {
  const scrollTo = document.getElementById(
    `testimonial-card-${visibleCardNum + 1}`
  );
  if (scrollTo) {
    scrollTo.scrollIntoView({ behavior: "smooth" });
  }
});

document.getElementById("slideLeft").addEventListener("click", function () {
  const scrollTo = document.getElementById(
    `testimonial-card-${visibleCardNum - 1}`
  );

  if (scrollTo) {
    scrollTo.scrollIntoView({ behavior: "smooth" });
  }
});
