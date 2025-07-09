    // Función para detectar elementos en el viewport
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
          rect.top <= (window.innerHeight || document.documentElement.clientHeight) * 0.85
        );
      }
      
      // Función para manejar las animaciones al hacer scroll
      function handleScrollAnimations() {
        // Manejar las tarjetas de información
        document.querySelectorAll('.info-card').forEach(card => {
          if (isElementInViewport(card)) {
            card.style.transform = 'translateY(0)';
            card.style.opacity = '1';
          }
        });
        
        // Manejar los elementos con fade-in
        document.querySelectorAll('.fade-in').forEach(item => {
          if (isElementInViewport(item)) {
            item.classList.add('visible');
          }
        });
        
        // Manejar los elementos de la galería
        document.querySelectorAll('.gallery-item').forEach((item, index) => {
          if (isElementInViewport(item)) {
            setTimeout(() => {
              item.style.opacity = '1';
              item.style.transform = 'translateY(0)';
            }, index * 150);
          }
        });
      }
  
      // Inicializar los estilos
      document.querySelectorAll('.info-card').forEach(card => {
        card.style.transform = 'translateY(20px)';
        card.style.opacity = '0';
        card.style.transition = 'all 0.6s ease-out';
      });
      
      // Configurar evento de scroll
      window.addEventListener('scroll', handleScrollAnimations);
      
      // Activar la primera verificación cuando se carga la página
      window.addEventListener('load', handleScrollAnimations);
      
      // Disparar el evento de scroll para inicializar
      window.dispatchEvent(new Event('scroll'));