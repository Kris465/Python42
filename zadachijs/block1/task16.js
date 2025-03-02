// Перевести из линейной записи в обычную следующие выражения: 
// а) / / a b c;     
// б) abc;          
// в) abc;          
// г) a bc;         
// д) a b c;        
// е) a bb c;        
// ж) a b b c ;     
// з) sin a b;
// и) 12 sin ab x; 
// к) 2 cos 2 b c a b c ; 
// л) 4 sin 2 sin 2 sin 2 R a b c ; 
// м) a x b cx d ; 
// н) 2 sin 2 cos 2 a b a b ;
// о) abs 2 sin 3abs 2 x . 


function solve() {
    function calculate_a(a, b, c) { return a / (b / c); }
    function calculate_b(a, b, c) { return a * b * c; }
    function calculate_c(a, b, c) { return (a / b) * c; }
    function calculate_d(a, b, c) { return a / (b * c); }
    function calculate_e(a, b, c) { return a / (b * b * c); }
    function calculate_f(a, b, c) { return a / b / (b * c); }
    function calculate_g(a, b) { return Math.sin(a / b); }
    function calculate_h(a, b, x) { return (12 * Math.sin(a * b)) / x; }
    function calculate_i(b, c, a) { return (2 * Math.cos(2 * b * c)) / (a * b * c); }
    function calculate_j(R, a, b, c) { return (4 * Math.sin(2 * Math.sin(2 * Math.sin(2 * R)))) / (a * b * c); }
    function calculate_k(a, x, b, c, d) { return (a / x + b) / (c * x + d); }
    function calculate_l(a, b) { return (2 * Math.sin(2) / Math.cos(2)) * (a / b) / (a / b); }
    function calculate_m(x) { return Math.abs(2 * Math.sin(3 * Math.abs(2) / x)); }
  
    const a_val = 1, b_val = 2, c_val = 3, x_val = 4, R_val = 5;  
  
    console.log("a:", calculate_a(a_val, b_val, c_val));
    console.log("b:", calculate_b(a_val, b_val, c_val));
    console.log("c:", calculate_c(a_val, b_val, c_val));
    console.log("d:", calculate_d(a_val, b_val, c_val));
    console.log("e:", calculate_e(a_val, b_val, c_val));
    console.log("f:", calculate_f(a_val, b_val, c_val));
    console.log("g:", calculate_g(a_val, b_val));
    console.log("h:", calculate_h(a_val, b_val, x_val));
    console.log("i:", calculate_i(b_val, c_val, a_val));
    console.log("j:", calculate_j(R_val, a_val, b_val, c_val));
    console.log("k:", calculate_k(a_val, x_val, b_val, c_val,R_val));
    console.log("l:", calculate_l(a_val, b_val));
    console.log("m:", calculate_m(x_val));
  }
  
  solve();