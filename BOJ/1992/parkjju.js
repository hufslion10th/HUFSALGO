const fs = require('fs');
const input = fs.readFileSync('./input.txt').toString().trim().split('\n');

// 변의 길이
const size = +input[0];

// 쿼드트리 저장 공간
const quadTree = input.slice(1, size + 1);

const solution = (row, col, line) => {
    // 더 이상 압축할 수 없으면 해당 문자열 리턴
    if (size === 1) {
        return quadTree[row][col];
    }

    // 사각형 맨 처음 값
    const initValue = quadTree[row][col];

    // 내부 요소 중 다른 값 포함여부 플래그
    let bool = true;

    // 전체 요소 순회
    for (let i = row; i < row + line; i++) {
        for (let j = col; j < col + line; j++) {
            // 다른 값이 섞여있으면 순회 중단
            if (quadTree[i][j] !== initValue) {
                bool = false;
                break;
            }
        }
        if (!bool) {
            break;
        }
    }

    // 전체 값이 동일하면 초기값 리턴
    if (bool) {
        return initValue;
    }

    // 네 조각으로 쪼개기
    const halfSize = line / 2;

    // 네 조각으로 쪼갠 후 결과문자열
    let result = '';

    // 네 조각 순회
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            // 한 조각마다 순회 결과를 문자열 변수에 push
            const pressed = `${solution(
                row + i * halfSize,
                col + j * halfSize,
                halfSize
            )}`;
            result += pressed;
        }
    }
    // 템플릿 리터럴로 네 조각에 대한 압축결과를 리턴
    return `(${result})`;
};

console.log(solution(0, 0, size));
