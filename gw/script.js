const quizData = {
    math: [
        {
            question: "რამდენია 12 + 7?",
            options: ["19", "21", "18", "20"],
            answer: "19"
        },
        {
            question: "რამდენია 5 * 6?",
            options: ["30", "20", "25", "35"],
            answer: "30"
        }
    ],
    geo: [
        {
            question: "რომელი მდინარეა ყველაზე გრძელი მსოფლიოში?",
            options: ["ნილოსი", "ამაზონი", "იანძე", "მეკონგი"],
            answer: "ამაზონი"
        },
        {
            question: "რომელ კონტინენტზე მდებარეობს საქართველო?",
            options: ["აზია", "ევროპა", "აფრიკა", "ამერიკა"],
            answer: "აზია"
        }
    ],
    history: [
        {
            question: "ვინ იყო დავით აღმაშენებელი?",
            options: ["მეფე", "მწერალი", "მეცნიერი", "ხატვის მასწავლებელი"],
            answer: "მეფე"
        },
        {
            question: "რომელ წელს გამოცხადდა საქართველოს დამოუკიდებლობა?",
            options: ["1918", "1991", "1921", "2000"],
            answer: "1918"
        }
    ]
};

let currentSubject = "";
let currentQuestionIndex = 0;
let score = 0;

const questionEl = document.getElementById("question");
const optionsEl = document.getElementById("options");
const nextBtn = document.getElementById("next-btn");
const resultEl = document.getElementById("result");

function loadSubject(subject) {
    currentSubject = subject;
    currentQuestionIndex = 0;
    score = 0;
    resultEl.textContent = "";
    document.getElementById("quiz-container").style.display = "block";
    loadQuestion();
}

function loadQuestion() {
    const q = quizData[currentSubject][currentQuestionIndex];
    questionEl.textContent = q.question;
    optionsEl.innerHTML = "";

    q.options.forEach(option => {
        const button = document.createElement("button");
        button.textContent = option;
        button.onclick = () => selectAnswer(option);
        optionsEl.appendChild(button);
    });
}

function selectAnswer(selected) {
    const correct = quizData[currentSubject][currentQuestionIndex].answer;
    if (selected === correct) {
        score++;
    }
    currentQuestionIndex++;
    if (currentQuestionIndex < quizData[currentSubject].length) {
        loadQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    document.getElementById("quiz-container").style.display = "none";
    resultEl.textContent = `თქვენ დააგროვეთ ${score} ქულა ${quizData[currentSubject].length} კითხვიდან.`;
}

nextBtn.addEventListener("click", () => {
    if (currentQuestionIndex < quizData[currentSubject].length) {
        loadQuestion();
    }
});