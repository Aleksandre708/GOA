const list = document.createElement("ul");

const item1 = document.createElement("li");
item1.textContent = "Apple";

const item2 = document.createElement("li");
item2.textContent = "Banana";

const item3 = document.createElement("li");
item3.textContent = "Cherry";

// Append items to the <ul>
list.appendChild(item1);
list.appendChild(item2);
list.appendChild(item3);

// Add <ul> to the page
document.body.appendChild(list);
