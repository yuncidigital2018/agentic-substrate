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
  if (slides[current]) {
    slides[current].scrollTop = 0;
    slides[current].scrollLeft = 0;
  }
  window.scrollTo(0, 0);
  if (dots) dots.querySelectorAll(".dot").forEach((dot, i) => dot.classList.toggle("active", i === current));
  if (counter) counter.textContent = (current + 1) + " / " + slides.length;
}

document.getElementById("prev")?.addEventListener("click", () => show(current - 1));
document.getElementById("next")?.addEventListener("click", () => show(current + 1));
document.addEventListener("keydown", event => {
  if (event.target && ["TEXTAREA", "INPUT"].includes(event.target.tagName)) return;
  const activeSlide = slides[current];
  const canScroll = activeSlide && activeSlide.scrollHeight > activeSlide.clientHeight + 2;
  const atTop = !activeSlide || activeSlide.scrollTop <= 2;
  const atBottom = !activeSlide || activeSlide.scrollTop + activeSlide.clientHeight >= activeSlide.scrollHeight - 2;

  if ((event.key === "PageDown" || event.key === " ") && canScroll && !atBottom) {
    event.preventDefault();
    activeSlide.scrollBy({ top: activeSlide.clientHeight * 0.82, behavior: "smooth" });
    return;
  }
  if (event.key === "PageUp" && canScroll && !atTop) {
    event.preventDefault();
    activeSlide.scrollBy({ top: activeSlide.clientHeight * -0.82, behavior: "smooth" });
    return;
  }
  if (event.key === "ArrowRight" || ((event.key === "PageDown" || event.key === " ") && (!canScroll || atBottom))) {
    event.preventDefault();
    show(current + 1);
  }
  if (event.key === "ArrowLeft" || (event.key === "PageUp" && (!canScroll || atTop))) {
    event.preventDefault();
    show(current - 1);
  }
});

let touchStartX = 0;
let touchStartY = 0;
let touchStartedOnControl = false;

document.addEventListener("touchstart", event => {
  const touch = event.changedTouches[0];
  if (!touch) return;
  touchStartedOnControl = Boolean(event.target?.closest?.("a, button, input, textarea, select"));
  touchStartX = touch.clientX;
  touchStartY = touch.clientY;
}, { passive: true });

document.addEventListener("touchend", event => {
  if (touchStartedOnControl) return;
  const touch = event.changedTouches[0];
  if (!touch) return;
  const deltaX = touch.clientX - touchStartX;
  const deltaY = touch.clientY - touchStartY;
  const isHorizontalSwipe = Math.abs(deltaX) > 56 && Math.abs(deltaX) > Math.abs(deltaY) * 1.25;
  if (!isHorizontalSwipe) return;
  if (deltaX < 0) show(current + 1);
  if (deltaX > 0) show(current - 1);
}, { passive: true });

show(0);
