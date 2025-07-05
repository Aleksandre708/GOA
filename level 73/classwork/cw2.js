function modifyDiv() {
  const div = document.getElementById('myDiv');
  const button = document.getElementById('myButton');
  if (button) {
    div.removeChild(button);
  }
  const paragraph = document.getElementById('myParagraph');
  if (paragraph) {
    const italic = document.createElement('i');
    italic.textContent = "ეს არის შეცვლილი ტექსტი i თეგში";
    div.replaceChild(italic, paragraph);
  }
}
window.onload = modifyDiv;
