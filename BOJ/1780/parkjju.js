const fs = require('fs');
let input = fs
    .readFileSync('/dev/stdin')
    .toString()
    .split('\n')
    .map((item) => item.trim());

// 데이터 정제, -1,0,1로 이루어진 사각형 개수 저장을 위한 배열 마련
const size = +input[0];
let square = [];
for (let i = 1; i < input.length; i++) {
    square.push(input[i]);
}
square = square.map((item) => item.split(' ').map((item) => +item));
let answer = [0, 0, 0];

// 시작지점 row, col
// 변 길이 size
const solution = (row, col, size) => {
    let first = square[row][col];
    let same = true;

    // row~row+size
    // col~col+size까지 순회
    for (let i = row; i < row + size; i++) {
        for (let j = col; j < col + size; j++) {
            // 맨 처음 시작지점 값과 다른 값이 섞여 있으면 그 즉시 탈출
            // 탈출 후 9조각으로 사각형을 쪼개어 각각 순회
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

    // 종이를 9조각으로 쪼개서 순회
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
