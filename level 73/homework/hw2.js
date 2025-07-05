const header = document.createElement("h1");
header.textContent = "Welcome to my page!";

const containerDiv = document.createElement("div"); // create the <div>
containerDiv.appendChild(header); // append <h1> to <div>
document.body.appendChild(containerDiv); // add <div> to the body
