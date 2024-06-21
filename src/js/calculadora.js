function calcularTotal() {
    const ingresos = parseFloat(document.getElementById('ingresos').value) || 0;
    const gastos = parseFloat(document.getElementById('gastos').value) || 0;
    const total = ingresos - gastos;
    document.getElementById('total').textContent = total.toFixed(2);
}