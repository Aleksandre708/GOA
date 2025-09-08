// 1. პირველი სიმბოლო
const str1 = "JavaScript";
console.log(str1.at(0));  // "J"

// 2. ბოლო სიმბოლო უარყოფითი ინდექსით
const str2 = "OpenAI";
console.log(str2.at(-1)); // "I"

// 3. მეხუთე სიმბოლო (0-იდან ვითვლით, ამიტომ 4)
const str3 = "Programming";
console.log(str3.at(4));  // "r"

// 4. ფუნქცია შუა სიმბოლოს დასაბრუნებლად
function getMiddleChar(s) {
  const mid = Math.floor(s.length / 2);
  // თუ სიგრძე ლუწია, mid არის "მარჯვენა შუა"; თუ კენტია, mid არის ზუსტად შუა
  return s.at(mid);
}

console.log(getMiddleChar("OpenAI"));    // "n" (lenght 6 → mid 3)
console.log(getMiddleChar("JavaScript"));// "S" (lenght 10 → mid 5)

// 5. მეორე-ბოლო სიმბოლო
const str5 = "Hello World";
console.log(str5.at(-2)); // "l"
