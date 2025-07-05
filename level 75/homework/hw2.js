const interval2 = setInterval(() => {
  console.log("This message appears every 2 seconds");
}, 2000);

setTimeout(() => {
  clearInterval(interval2);
  console.log("Message stopped after 10 seconds");
}, 10000);
