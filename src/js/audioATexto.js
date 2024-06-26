const btnStart = document.getElementById('btnStart');
const btnStop = document.getElementById('btnStop');
const textArea = document.getElementById('textArea');

const recognition = new webkitSpeechRecognition();

recognition.continuous = true;
recognition.lang = 'es-ES';
recognition.interimResult = false;

btnStart.addEventListener('click', () => {
    recognition.start();
});

btnStop.addEventListener('click', () => {
    recognition.abort();
});

recognition.onresult = (event) => {
    const texto = event.results[event.results.length - 1][0].transcript;
    textArea.value = texto;
}