class Carousel {
  constructor(container) {
    this.container = container;
    this.slides = container.getElementsByClassName("mySlides");
    this.dots = container.parentElement.querySelectorAll(".dot");
    this.slideIndex = 1;

    this.showSlides(this.slideIndex);

    // Si quieres autoplay
    this.autoPlay();
  }

  plusSlides(n) {
    this.showSlides(this.slideIndex += n);
  }

  currentSlide(n) {
    this.showSlides(this.slideIndex = n);
  }

  showSlides(n) {
    if (n > this.slides.length) { this.slideIndex = 1 }
    if (n < 1) { this.slideIndex = this.slides.length }

    // Ocultar todos
    for (let i = 0; i < this.slides.length; i++) {
      this.slides[i].style.display = "none";
    }

    // Quitar active de todos los dots
    if (this.dots.length > 0) {
      this.dots.forEach(dot => dot.classList.remove("active"));
    }

    // Mostrar actual
    this.slides[this.slideIndex - 1].style.display = "block";
    if (this.dots.length > 0) {
      this.dots[this.slideIndex - 1].classList.add("active");
    }
  }

  autoPlay() {
    setInterval(() => {
      this.plusSlides(1);
    }, 10000); // cada 3s
  }
}

// Inicializar todos los carruseles en la página
document.addEventListener("DOMContentLoaded", () => {
  const carousels = document.querySelectorAll(".slideshow-container");
  carousels.forEach(container => {
    const carousel = new Carousel(container);

    // Conectar botones
    const prev = container.querySelector(".prev");
    const next = container.querySelector(".next");
    if (prev) prev.addEventListener("click", () => carousel.plusSlides(-1));
    if (next) next.addEventListener("click", () => carousel.plusSlides(1));

    // Conectar dots
    const dots = container.parentElement.querySelectorAll(".dot");
    dots.forEach((dot, index) => {
      dot.addEventListener("click", () => carousel.currentSlide(index + 1));
    });
  });
});