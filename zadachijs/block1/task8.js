const four_random_numbers = Array.from({length: 4}, () => Math.floor(Math.random() * 101));

const joinedString = four_random_numbers.join(" ");
console.log(joinedString);