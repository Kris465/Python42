let old = prompt('Укажите ваш возраст: ');

if(old >=0 && old <= 12){
    alert('Вы ребенок');
}else if(old >=12 && old <= 18){
    alert('Вы подросток');
}else if(old >=18 && old <= 60){
    alert('Вы взрослый');
}else if(old >=60 && old <=101){
    alert('Вы пенсионер');
}else{
    alert('Укажите реальный возраст!');
}
   