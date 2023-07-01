/* const cards = [
    '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼',
    '🐯', '🦁', '🐮', '🐷', '🐸', '🐵', '🐔', '🐧'
];
*/

const cards = [
    '🐶', '🐱', '🐭', '🐹'
];

let selectedCardElements = [];
let selectedCards = [];
let matchedCards = [];
let startTime;
let elapsedTime = 0;
let timerInterval;
let isFlipping = false;
let isTimerRunning = false;

const timerElement = document.getElementById("timer");

function createCardElement(card) {
    const cardElement = document.createElement('div');
    cardElement.classList.add('card');
    cardElement.innerHTML = `<div class="card-front">${card}</div><div class="card-back"></div>`;
    cardElement.addEventListener('click', () => flipCard(cardElement, card));
    return cardElement;
}

function createCards() {
    const shuffledCards = [...cards, ...cards].sort(() => Math.random() - 0.5);
    const grid = document.querySelector('.grid');
    for (const card of shuffledCards) {
        const cardElement = createCardElement(card);
        grid.appendChild(cardElement);
    }
}

function flipCard(cardElement, card) {
    if (isFlipping || selectedCards.length === 2 || matchedCards.includes(card) || selectedCardElements.includes(cardElement)) {
        return;
    }

    const cardFront = cardElement.querySelector('.card-front');
    cardFront.classList.toggle('hidden');
    cardElement.classList.add('flipped');
    selectedCardElements.push(cardElement);
    selectedCards.push(card);
    backgroundAudio.play();

    if (selectedCards.length === 2) {
        isFlipping = true;
        setTimeout(checkMatch, 500);
        backgroundAudio.play();
    }

    if (selectedCards.length === 1 && !isTimerRunning) {
        isTimerRunning = true;
        startTimer();
    }
}

const matchSound = new Audio('css/mp3/mario-coin.mp3');

function checkMatch() {
    const card1 = selectedCardElements[0];
    const card2 = selectedCardElements[1];
    const card1Front = card1.querySelector('.card-front');
    const card2Front = card2.querySelector('.card-front');
    const card1Text = selectedCards[0];
    const card2Text = selectedCards[1];

    if (card1Text === card2Text) {
        card1Front.classList.add('hidden');
        card2Front.classList.add('hidden');
        card1.classList.add('matched');
        card2.classList.add('matched');
        matchedCards.push(card1Text);
        selectedCardElements = [];
        selectedCards = [];
        playMatchSound();
        checkWin();
    } else {
        setTimeout(() => {
            card1Front.classList.toggle('hidden');
            card2Front.classList.toggle('hidden');
            card1.classList.remove('flipped');
            card2.classList.remove('flipped');
            selectedCardElements = [];
            selectedCards = [];
        }, 90);
    }
    isFlipping = false;
}

function playMatchSound() {
    matchSound.play();
}

function restartGame() {
    clearInterval(timerInterval);
    startTime = null;
    elapsedTime = 0;
    isGameWon = false;
    isTimerRunning = false;
    location.reload();
    const grid = document.querySelector('.grid');
    grid.innerHTML = '';
    selectedCardElements = [];
    selectedCards = [];
    matchedCards = [];
    createCards();
    backgroundAudio.play();
}

let isGameWon = false;

function checkWin() {
    if (matchedCards.length === cards.length && !isGameWon) {
        clearInterval(timerInterval);
        const elapsedTimeString = formatElapsedTime(elapsedTime);
        setTimeout(() => {
            alert(`¡Has ganado el juego en ${elapsedTimeString}!`);
            backgroundAudio.pause();
            isGameWon = true;
            isTimerRunning = false;
        }, 500);
    }
}

function startTimer() {
    startTime = new Date().getTime();

    timerInterval = setInterval(() => {
        const now = new Date().getTime();
        elapsedTime = now - startTime;

        const elapsedTimeString = formatElapsedTime(elapsedTime);

        timerElement.textContent = elapsedTimeString;
    }, 1000);
}

function formatElapsedTime(time) {
    const minutes = Math.floor(time / (1000 * 60));
    const seconds = Math.floor((time % (1000 * 60)) / 1000);
    const minutesString = minutes.toString().padStart(2, '0');
    const secondsString = seconds.toString().padStart(2, '0');
    return `${minutesString}:${secondsString}`;
}

const backgroundAudio = document.getElementById('background-audio');

document.addEventListener('DOMContentLoaded', () => {
    backgroundAudio.play();
    createCards();
});
