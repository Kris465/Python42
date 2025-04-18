const prompt = require('prompt-sync')();

function willHitTarget(v0, angleDeg, R, H, P) {
    const g = 9.8;
    const angleRad = angleDeg * Math.PI / 180;
    const cosAngle = Math.cos(angleRad);
    
    if (v0 * cosAngle === 0) return false;
    
    const t = R / (v0 * cosAngle);
    const y = v0 * Math.sin(angleRad) * t - 0.5 * g * Math.pow(t, 2);
    
    return y >= H && y <= H + P;
}

const v0 = parseFloat(prompt('Введите начальную скорость снаряда (м/с): '));
const angleDeg = parseFloat(prompt('Введите угол выстрела (градусы): '));
const R = parseFloat(prompt('Введите расстояние до цели (м): '));
const H = parseFloat(prompt('Введите высоту основания цели (м): '));
const P = parseFloat(prompt('Введите высоту цели (м): '));

if (willHitTarget(v0, angleDeg, R, H, P)) {
    console.log("Снаряд поразит цель!");
} else {
    console.log("Снаряд не попадет в цель.");
}