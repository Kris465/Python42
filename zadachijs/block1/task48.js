function isEquilateral(a, b, c) {

    let a = ("Введите рост a: ");
    let b = ("Введите рост b: ");
    let c = ("Введите рост c: ");

   
    if (a <= 0 || b <= 0 || c <= 0) {
        console.log("Рост нединаковый");
    }
  
   
    if (a == c < b || b == c < a || a == c < b) {
        console.log("Рост нединаковый"); 
    }
  
   
    else (a === b === c) {
        console.log("Рост одинаковый");
    }
  }
