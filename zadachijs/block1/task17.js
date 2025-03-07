function solve() {
    // a) x^2 - 1 / (x^2 + 2)
    function expression_a(x) { return (x * x - 1) / (x * x + 2); }
  
    // б) (x1 * x2) + (x1 * x3) + (x2 * x3)
    function expression_b(x1, x2, x3) { return (x1 * x2) + (x1 * x3) + (x2 * x3); }
  
    // в) v0 * t + (a * t^2) / 2
    function expression_c(v0, a, t) { return v0 * t + (a * t * t) / 2; }
  
    // г) (m * v^2) / 2 - m * g * h
    function expression_d(m, v, g, h) { return (m * v * v) / 2 - m * g * h; }
  
    // д) R1 + R2 / (R1 * R2)
    function expression_e(R1, R2) { return R1 + R2 / (R1 * R2); }
  
    // е) Math.cos(m * g)
    function expression_f(m, g) { return Math.cos(m * g); }
  
    // ж) 2 * R
    function expression_g(R) { return 2 * R; }
  
    // з) Math.sqrt(b^2 - 4 * a * c)
    function expression_h(b, a, c) { return Math.sqrt(b * b - 4 * a * c); }
  
    // и) (m1 * m2) / (r^2)
    function expression_i(m1, m2, r) { return (m1 * m2) / (r * r); }
  
    // к) I^2 * R
    function expression_j(I, R) { return I * I * R; }
  
    // л) Math.sin(a * b) / c
    function expression_k(a, b, c) { return Math.sin(a * b) / c; }
  
    // м) Math.sqrt(a^2 + b^2 - 2 * a * b * Math.cos(c))
    function expression_l(a, b, c) { return Math.sqrt(a * a + b * b - 2 * a * b * Math.cos(c)); }
  
    // н) (a * d - b * c) / (a * d)
    function expression_m(a, b, c, d) { return (a * d - b * c) / (a * d); }
  
    // о) 2 * Math.sin(x) + 1
    function expression_n(x) { return 2 * Math.sin(x) + 1; }
  
    // п) (-b + Math.sqrt(b * b - 4 * a * c)) / (2 * a)
    function expression_o(a, b, c) { return (-b + Math.sqrt(b * b - 4 * a * c)) / (2 * a); }
  
    // р) (x - x1) / (x2 - x1)
    function expression_p(x, x1, x2) { return (x - x1) / (x2 - x1); }
  
    // с) 1 / (x * x)
    function expression_q(x) { return 1 / (x * x); }
  
    // т) 1 / x
    function expression_r(x) { return 1 / x; }
  
    // Примеры использования (нужно задать значения переменных):
    const x_val = 1, x1_val = 2, x2_val = 3, x3_val = 4, v0_val = 5, a_val = 6, t_val = 7, m_val = 8, v_val = 9, g_val = 10, h_val = 11, R1_val = 12, R2_val = 13, I_val = 14, b_val = 15, c_val = 16, d_val = 17, R_val = 18;
  
    console.log("a:", expression_a(x_val));
    console.log("b:", expression_b(x1_val, x2_val, x3_val));
    console.log("c:", expression_c(v0_val, a_val, t_val));
    console.log("d:", expression_d(m_val, v_val, g_val, h_val));
    console.log("e:", expression_e(R1_val, R2_val));
    console.log("f:", expression_f(m_val, g_val));
    console.log("g:", expression_g(R_val));
    console.log("h:", expression_h(b_val, a_val, c_val));
    console.log("i:", expression_i(m_val, m_val, R_val)); //Предположил, что m1 и m2 - это m
    console.log("j:", expression_j(I_val, R_val));
    console.log("k:", expression_k(a_val, b_val, c_val));
    console.log("l:", expression_l(a_val, b_val, c_val));
    console.log("m:", expression_m(a_val, b_val, c_val, d_val));
    console.log("n:", expression_n(x_val));
    console.log("o:", expression_o(a_val, b_val, c_val));
    console.log("p:", expression_p(x_val, x1_val, x2_val));
    console.log("q:", expression_q(x_val));
    console.log("r:", expression_r(x_val));
  
  }
  
  solve();