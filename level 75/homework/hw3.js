let changeCount = 0;
const interval3 = setInterval(() => {
  document.body.style.backgroundColor = getRandomColor();
  changeCount++;
  if (changeCount === 5) {
    clearInterval(interval3);
    console.log("Background stopped changing after 5 times");
  }
}, 3000);

function getRandomColor() {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
}
