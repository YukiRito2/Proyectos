/*const cards = [
    '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼',
    '🐯', '🦁', '🐮', '🐷', '🐸', '🐵', '🐔', '🐧'
];
*/

const cards = [
    '🐶', '🐱', '🐭', '🐹'
];


let selectedCards = [];
let matchedCards = [];
let startTime;
let elapsedTime = 0;
let timerInterval;


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
    if (selectedCards.length < 2 && !matchedCards.includes(card) && !selectedCards.includes(cardElement)) {
        const cardFront = cardElement.querySelector('.card-front');
        cardFront.classList.toggle('hidden'); // Alternar la visibilidad del icono
        cardElement.classList.add('flipped');
        selectedCards.push({ cardElement, card });
        backgroundAudio.play();
        if (selectedCards.length === 2) {
            setTimeout(checkMatch, 500);
            backgroundAudio.play();
            
        }
    }
}

const matchSound = new Audio('css/mp3/mario-coin.mp3'); //


function checkMatch() {
    const card1 = selectedCards[0];
    const card2 = selectedCards[1];
    const card1Front = card1.cardElement.querySelector('.card-front');
    const card2Front = card2.cardElement.querySelector('.card-front');
    const card1Text = card1.card;
    const card2Text = card2.card;

    if (card1Text === card2Text) {
        card1Front.classList.add('hidden');
        card2Front.classList.add('hidden');
        card1.cardElement.classList.add('matched');
        card2.cardElement.classList.add('matched');
        matchedCards.push(card1Text);
        selectedCards = [];
        playMatchSound();
        checkWin();
    } else {
        setTimeout(() => {
            card1Front.classList.toggle('hidden');
            card2Front.classList.toggle('hidden');
            card1.cardElement.classList.remove('flipped');
            card2.cardElement.classList.remove('flipped');
            selectedCards = [];
        }, 500);
    }
}

function playMatchSound() {
    matchSound.play();
}


function restartGame() {
    clearInterval(timerInterval);
    startTime = null;
    elapsedTime = 0;
    isGameWon = false;
    location.reload();
    const grid = document.querySelector('.grid');
    grid.innerHTML = '';
    selectedCards = [];
    matchedCards = [];
    createCards();
    backgroundAudio.play();
    startTime();
}

let isGameWon = false;

function checkWin() {
    if (matchedCards.length === cards.length && !isGameWon) {
        clearInterval(timerInterval);
        const elapsedTimeString = formatElapsedTime(elapsedTime);
        setTimeout(() => {
            alert(`¡Has ganado el juego en ${elapsedTimeString}!`);
            backgroundAudio.pause(); 
            isGameWon = true; //marcar el juego como ganado
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
    startTimer();
    createCards();
});

