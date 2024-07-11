document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');
    const saveButton = document.getElementById('saveDrawing');
    const clearButton = document.getElementById('clearCanvas'); 
    const eraserButton = document.getElementById('eraser'); 


    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let painting = false;
    let erasing = false; 

    function startPosition(e) {
        painting = true;
        draw(e);
    }

    function finishedPosition() {
        painting = false;
        ctx.beginPath();
    }

    function draw(e) {
        if (!painting) return;
        ctx.lineWidth = erasing ? 20 : 5; 
        ctx.strokeStyle = erasing ? 'white' : 'black'; 
        ctx.lineCap = 'round';
        ctx.lineTo(e.clientX, e.clientY);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(e.clientX, e.clientY);
    }


    function clearCanvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function toggleEraser() {
        erasing = !erasing; // Activa o desactiva el modo goma
        eraserButton.textContent = erasing ? 'Dibujar' : 'Goma';
    }

    canvas.addEventListener('mousedown', startPosition);
    canvas.addEventListener('mouseup', finishedPosition);
    canvas.addEventListener('mousemove', draw);
    clearButton.addEventListener('click', clearCanvas);
    eraserButton.addEventListener('click', toggleEraser); 


    saveButton.addEventListener('click', function() {
        const dataURL = canvas.toDataURL('image/png');
        fetch('http://127.0.0.1:5000/save-drawing', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: dataURL }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    });
});