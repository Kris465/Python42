document.getElementById('button').addEventListener('click', function(){
    const length = document.getElementById('lengthInput').value;
    const perimetr = document.getElementById('perimetrInput').value;
    const result = document.getElementById('result');

    const is = ((length / Math.PI) <= (perimetr / 4));
    result.textContent = is ? 'окружность поместится в квадрат' : 'окружность не поместится в квадрат';

});