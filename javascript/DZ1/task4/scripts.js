document.getElementById('Button').addEventListener('click', function() {
    const radius = document.getElementById('radiusInput').value
    const message = document.getElementById('message')

    if (radius) {
        message.textContent = `Площадь окружности: ${2 * 3.14 * radius}`
    }else{
        message.textContent = 'Пожалуйста введите радиус окружности'
    }
})