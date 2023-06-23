var result = document.getElementById('result');

function addToResult(value) {
    result.value += value;
}

function calculateResult() {
    var expression = result.value;
    var answer = eval(expression);
    result.value = answer;
}

function clearResult() {
    result.value = '';
}
