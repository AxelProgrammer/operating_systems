document.addEventListener('DOMContentLoaded', () => {
  const output = document.getElementById('output');

  // Ловушка на клавиатуру
  document.addEventListener('keydown', (event) => {
    output.innerHTML += `Key Pressed: ${event.key}<br>`;
  });

  // Ловушка на мышь
  document.addEventListener('mousedown', (event) => {
    output.innerHTML += `Mouse Button Pressed: ${event.button}<br>`;
  });
});
