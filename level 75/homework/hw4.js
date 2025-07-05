const interval4 = setInterval(() => {
  const now = new Date();
  console.log(now.toLocaleTimeString());
}, 1000);

setTimeout(() => {
  clearInterval(interval4);
  console.log("Stopped showing time after 15 seconds");
}, 15000);
