document.getElementById('button').addEventListener('click', function(){
    const vopros1 = document.getElementById('vopros1Input').value;
    const vopros2 = document.getElementById('vopros2Input').value;
    const vopros3 = document.getElementById('vopros3Input').value;
    let score = 0;
    const mes = document.getElementById('mes');

     
        if (vopros1 == '2025') {
            score += 2
            mes.textContent = `Правильный ответ 3`
            
        }
        if (vopros2 == '10') {
            score += 2
            mes.textContent = `Правильный ответ 1`
        }
        if (vopros3 == 'в Монголии') {
            score += 2
            mes.textContent = `Правильный ответ 2`
        }
     
    mes.textContent = score




});