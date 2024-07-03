function updateCountdown() {
    const now = new Date();
    const nextYear = now.getFullYear() + 1;
    const newYearTime = new Date(`January 1, ${nextYear} 00:00:00`);
  
    const diff = newYearTime - now;
  
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((diff / 1000 / 60) % 60);
    const seconds = Math.floor((diff / 1000) % 60);
  
    document.getElementById('countdown-days').innerText = days + " Días";
    document.getElementById('countdown-hours').innerText = hours + " Horas";
    document.getElementById('countdown-minutes').innerText = minutes + " Minutos";
    document.getElementById('countdown-seconds').innerText = seconds + " Segundos";
  }
  
  // Actualizar el contador cada segundo
  setInterval(updateCountdown, 1000);