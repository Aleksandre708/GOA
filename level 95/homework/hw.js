// 1. "dog" არის თუ არა წინადადებაში
const sentence = "The quick brown fox jumps over the lazy dog";
console.log(sentence.includes("dog"));   // true

// 2. ფუნქცია: შეიცავს თუ არა '@' (ძალიან მარტივი email–ის შემოწმება)
function hasAtSymbol(str) {
  return str.includes("@");
}
console.log(hasAtSymbol("test@example.com")); // true
console.log(hasAtSymbol("hello.world"));      // false

// 3. "Java" არის თუ არა "JavaScript"-ში
const lang = "JavaScript";
console.log(lang.includes("Java")); // true

// 4. "apple" არის თუ არა "pineapple"-ში
console.log("pineapple".includes("apple")); // true

// 5. ფუნქცია: წინადადებაში არის თუ არა "not"
function containsNot(str) {
  return str.toLowerCase().includes("not");
}
console.log(containsNot("This is not good.")); // true
console.log(containsNot("All is well."));      // false
