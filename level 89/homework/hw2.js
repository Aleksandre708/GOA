let isHello = true;

const titleInterval = setInterval(() => {
  document.title = isHello ? "Hello" : "Goodbye";
  isHello = !isHello;
}, 1000); // ყოველ 1 წამში ცვლა

// 6 წამში გაჩერება
setTimeout(() => {
  clearInterval(titleInterval);
  console.log("Title flashing stopped.");
}, 6000);
