const fs = require('fs');
let input = fs
    .readFileSync('/dev/stdin')
    .toString()
    .split('\n')
    .map((item) => item.trim());

const size = +input[0];
let square = [];
for (let i = 1; i < input.length; i++) {
    square.push(input[i]);
}
square = square.map((item) => item.split(' ').map((item) => +item));
let answer = [0, 0, 0];
const solution = (row, col, size) => {
    let first = square[row][col];
    let same = true;

    for (let i = row; i < row + size; i++) {
        for (let j = col; j < col + size; j++) {
            if (first !== square[i][j]) {
                same = false;
                break;
            }
        }
        if (!same) {
            break;
        }
    }

    if (same) {
        answer[first + 1] += 1;
        return;
    }

    let k = size / 3;

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            solution(row + i * k, col + j * k, k);
        }
    }
};
solution(0, 0, size);
console.log(answer.at(0));
console.log(answer.at(1));
console.log(answer.at(2));
