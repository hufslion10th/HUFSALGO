const fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split('\n');
let count = +input[0];
let paper = input
    .slice(1, count + 1)
    .map((item) => item.split(' ').map((item) => +item));
let zero = 0;
let one = 0;

const isPaper = (x, y, line) => {
    if (line === 0) {
        return;
    }
    let prev = paper[x][y];
    let bool = true;
    for (let row = x; row < x + line; row++) {
        for (let col = y; col < y + line; col++) {
            if (paper[row][col] !== prev) {
                bool = false;
                break;
            }
        }
        if (!bool) {
            break;
        }
    }

    if (bool) {
        if (prev === 0) {
            zero += 1;
        } else {
            one += 1;
        }
        return;
    }
    let temp = parseInt(line / 2);

    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            isPaper(x + i * temp, y + j * temp, temp);
        }
    }
};

isPaper(0, 0, count);
console.log(zero, one);
