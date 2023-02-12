const quizContainer = document.getElementById("quiz-container");
const scoreBoard = document.createElement("div");
scoreBoard.id = "score-board";
document.body.appendChild(scoreBoard);

let score = 0;
let questions = [];

fetch("data.json")
  .then((response) => response.json())
  .then((data) => {
    questions = data;
    showQuestion();
  })
  .catch((error) => console.error(error));

function showQuestion() {
  quizContainer.innerHTML = `
    <h1>Q & A Paper 1</h1>
    ${questions.map((question, i) => `
      <div>
        <h2>${question.question}</h2>
        <ul class="options">
          ${question.options.map((option, index) => `
          <li>
          <input type="radio" name="question${i}" id="option${i}-${index}" value="${option}" required>
          <label for="option${i}-${index}" class="option">${option}</label>
        </li>
        
          `).join("")}
        </ul>
      </div>
    `).join("")}
  `;
  
  const options = document.querySelectorAll("input[type='radio']");
  options.forEach((option) => {
    option.addEventListener("click", handleOptionClick);
  });
}

function handleOptionClick() {
  const questionIndex = parseInt(this.name.replace("question", ""));
  const selectedOption = this.value;
  const question = questions[questionIndex];
  const optionLabel = this.nextElementSibling;

  if (selectedOption.startsWith(question.answer)) {
    score++;
    optionLabel.classList.add("correct");
  } else {
    optionLabel.classList.add("incorrect");
  }

  document.querySelectorAll(`input[name='question${questionIndex}']`).forEach((opt) => {
    opt.removeEventListener("click", handleOptionClick);
    if (opt.value.startsWith(question.answer)) {
      opt.nextElementSibling.classList.add("correct");
    }
  });

  scoreBoard.innerHTML = `<p>Score: ${score} / ${questions.length}</p>`;
}
