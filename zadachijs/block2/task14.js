const array = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100) + 1);

console.log("Массив:", array);

for (const item of [...array].reverse()) {
  console.log(item);
}