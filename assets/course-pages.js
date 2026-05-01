const slides = Array.from(document.querySelectorAll(".slide"));
const counter = document.getElementById("counter");
const dots = document.getElementById("dots");
let current = 0;

if (dots) {
  slides.forEach((_, index) => {
    const button = document.createElement("button");
    button.className = "dot" + (index === 0 ? " active" : "");
    button.setAttribute("aria-label", "Slide " + (index + 1));
    button.addEventListener("click", () => show(index));
    dots.appendChild(button);
  });
}

function show(index) {
  current = Math.max(0, Math.min(slides.length - 1, index));
  slides.forEach((slide, i) => slide.classList.toggle("active", i === current));
  if (dots) dots.querySelectorAll(".dot").forEach((dot, i) => dot.classList.toggle("active", i === current));
  if (counter) counter.textContent = (current + 1) + " / " + slides.length;
}

document.getElementById("prev")?.addEventListener("click", () => show(current - 1));
document.getElementById("next")?.addEventListener("click", () => show(current + 1));
document.addEventListener("keydown", event => {
  if (event.key === "ArrowRight" || event.key === "PageDown" || event.key === " ") {
    if (event.target && ["TEXTAREA", "INPUT"].includes(event.target.tagName)) return;
    event.preventDefault();
    show(current + 1);
  }
  if (event.key === "ArrowLeft" || event.key === "PageUp") {
    if (event.target && ["TEXTAREA", "INPUT"].includes(event.target.tagName)) return;
    event.preventDefault();
    show(current - 1);
  }
});

show(0);
