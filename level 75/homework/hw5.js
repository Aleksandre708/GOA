let seconds = 0;
const interval5 = setInterval(() => {
  seconds++;
  console.log(`Timer: ${seconds} second${seconds > 1 ? "s" : ""}`);
  if (seconds === 10) {
    clearInterval(interval5);
    console.log("Timer stopped at 10 seconds");
  }
}, 1000);
