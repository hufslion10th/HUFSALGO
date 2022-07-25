const fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split('\n');
let count = +input[0];
let paper = input
    .slice(1, count + 1)
    .map((item) => item.split(' ').map((item) => +item));
let zero = 0;
let one = 0;

// 재귀 함수
const isPaper = (x, y, line) => {
    if (line === 0) {
        return;
    }
    // 맨 처음 순회하는 값
    // 앞으로 순회하다가 prev와 다른 값이 등장하면 그 즉시 순회 중단
    let prev = paper[x][y];

    // 탈출을 위한 flag 설정
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

    // 전역변수에 접근 - 0 및 1로만 이루어진 사각형이면 + 1
    if (bool) {
        if (prev === 0) {
            zero += 1;
        } else {
            one += 1;
        }
        return;
    }
    // 변 길이 / 2
    let temp = parseInt(line / 2);

    // 네 조각으로 쪼개진 사각형 순회
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            isPaper(x + i * temp, y + j * temp, temp);
        }
    }
};

isPaper(0, 0, count);
console.log(zero, one);
