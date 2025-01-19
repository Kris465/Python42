document.addEventListener('DOMContentLoaded', function() {
    let password = prompt("Введите пароль ");
    const vallitPassword = ["Step", "Web", "JavaScript"];

    if (vallitPassword.includes(password)){
        alert("Подверждено");
    } else {
        alert("Отменено");
    }
   

});
