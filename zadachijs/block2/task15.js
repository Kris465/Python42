const array = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
array.forEach((element, index) => {
  const sqrt = Math.sqrt(element);
  console.log(`Квадратный корень из элемента ${index + 1} (${element}) равен ${sqrt}`);
});