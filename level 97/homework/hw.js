// 1. "2025-08-17" → [year, month, day]
const dateStr = "2025-08-17";
const dateParts = dateStr.split("-");
console.log(dateParts);  // ["2025", "08", "17"]

// 2. "one two three four five" → სიტყვების მასივი
const words = "one two three four five".split(" ");
console.log(words); // ["one", "two", "three", "four", "five"]

// 3. "John,Doe,25,Developer" → მნიშვნელობების მასივი
const csv = "John,Doe,25,Developer".split(",");
console.log(csv); // ["John", "Doe", "25", "Developer"]

// 4. "abc" → სიმბოლოების მასივი
const chars = "abc".split("");
console.log(chars); // ["a", "b", "c"]

// 5. "JavaScript is fun" → სიტყვების მასივი და მეორე სიტყვის მიღება
const sentence = "JavaScript is fun";
const arr = sentence.split(" ");
console.log(arr[1]); // "is"
