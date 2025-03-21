function isEquilateral(a, b, c) {
   
    if (a <= 0 || b <= 0 || c <= 0) {
      return false; 
    }
  
   
    if (a + b <= c || a + c <= b || b + c <= a) {
      return false; 
    }
  
   
    return a === b && b === c;
  }
  

  console.log(isEquilateral(5, 5, 5));   
  console.log(isEquilateral(5, 4, 5));   
  console.log(isEquilateral(5, 5, 0));   
  console.log(isEquilateral(5, 5, -5));  
  console.log(isEquilateral(1, 2, 3));   