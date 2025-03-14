function calculatePerimeter(a, b) {
   
    const c = Math.sqrt(a * a + b * b);
  
    
    const perimeter = a + b + c;
  
    return perimeter;
  }
  
  
  const a = 3; // Один катет
  const b = 4; // Другой катет
  const perimeter = calculatePerimeter(a, b);
  
  console.log("Периметр треугольника: " + perimeter);