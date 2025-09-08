let count = 10;

const timer = setInterval(() => {
  console.log(count);

  if (count === 0) {
    console.log("Time's up!");
    clearInterval(timer); // ინტერვალის გაჩერება
  }

  count--; // დავაკლოთ 1
}, 1000); // ყოველ 1000 მილიწამში = 1 წამში
