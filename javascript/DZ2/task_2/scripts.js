document.getElementById('button').addEventListener('click', function(){

const num = document.getElementById('num').value;

const message = document.getElementById('message');


switch(num){
    case '0':
        message.textContent = ')'
        break;
    case '1':
        message.textContent = '!';
        break;
    case '2':
        message.textContent = '@';
        break;
    case '3':
        message.textContent = '#';
        break;
    case '4':
        message.textContent = '$';
        break;
    case '5':
        message.textContent = '%';
        break;
    case '6':
        message.textContent = '^';
        break;
    case '7':
        message.textContent = '&';
        break;
    case '8':
        message.textContent = '*';
        break;
    case '9':
        message.textContent = '(';
        break;
    default:
        message.textContent = "Укажите цифру в диапозоне от 1 до 9!"
}
})

// бе
