// 1. ობიექტის შექმნა გასაღებებით და მეთოდებით
const person = {
  name: "ნიკა",
  surname: "ბერიძე",
  academy: "OpenAI Academy",
  city: "თბილისი",
  role: "სტუდენტი",
  favColor: "ლურჯი",

  // მეთოდი სახელი + გვარის გამოსატანად
  fullName: function() {
    console.log(this.name + " " + this.surname);
  },

  // მეთოდი საყვარელი ფერის გამოსატანად
  showFavColor: function() {
    console.log("საყვარელი ფერი არის: " + this.favColor);
  }
};

// 2. კონსოლში დაბეჭდეთ მთლიანი ობიექტი
console.log(person);

// 3. კონსოლში დაბეჭდეთ ნებისმიერი კუთვნილება, მაგალითად role
console.log(person.role);

// 4. გამოიძახეთ ობიექტის რომელიმე მეთოდი
person.fullName();
person.showFavColor();

// 5. შეცვალეთ ობიექტის რომელიმე მნიშვნელობა და დაბეჭდეთ
person.city = "ბათუმი";
console.log("ცვლილებული ქალაქი:", person.city);
