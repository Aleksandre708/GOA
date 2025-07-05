let count1 = 1;
const interval1 = setInterval(() => {
  console.log(count1);
  count1++;
  if (count1 > 5) clearInterval(interval1);
}, 1000);
