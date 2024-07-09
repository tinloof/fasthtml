const container = document.getElementById("carousel-container");
const elements = container.querySelectorAll(".testimonial-card");
const endicators = document.querySelectorAll(".endicator");

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

const boundsObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    const bound = entry.target.dataset.bound;
    if (entry.isIntersecting) {
      if (bound === "left") {
        document.getElementById("slideLeft").disabled = true;
      }

      if (bound === "right") {
        document.getElementById("slideRight").disabled = true;
      }
    } else {
      if (bound === "left") {
        document.getElementById("slideLeft").disabled = false;
      }

      if (bound === "right") {
        document.getElementById("slideRight").disabled = false;
      }
    }
  });
}, options);

endicators.forEach((element) => boundsObserver.observe(element));

elements.forEach((element) => {
  observer.observe(element);
});

function updateButtonState() {
  if (container.scrollLeft <= 0) {
    document.getElementById("slideLeft").disabled = true;
  } else {
    document.getElementById("slideLeft").disabled = false;
  }

  if (container.scrollLeft >= container.scrollWidth - container.clientWidth) {
    document.getElementById("slideRight").disabled = true;
  } else {
    document.getElementById("slideRight").disabled = false;
  }
}

document.getElementById("slideRight").addEventListener("click", function () {
  const scrollTo = document.getElementById(
    `testimonial-card-${visibleCardNum + 1}`
  );

  if (scrollTo) {
    const x = container.scrollLeft + scrollTo.offsetLeft - container.offsetLeft;
    container.scrollBy({ left: x, behavior: "smooth" });
    // updateButtonState();
  }
});

document.getElementById("slideLeft").addEventListener("click", function () {
  const scrollTo = document.getElementById(
    `testimonial-card-${visibleCardNum - 1}`
  );

  if (scrollTo) {
    const x = container.scrollLeft - scrollTo.offsetLeft + container.offsetLeft;
    container.scrollBy({ left: -x, behavior: "smooth" });
    // updateButtonState();
  }
});
