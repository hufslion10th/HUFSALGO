// JS 입력받기
const fs = require('fs');

// 입력값 데이터 정제 과정
let input = fs.readFileSync('./input.txt').toString().split('\n');

// 소 이동하는 정보 저장할 배열
let cows = [];

// 소들이 이동하는 횟수 N을 숫자 데이터로 변환
input[0] = +input[0];

// 소 이동 데이터가 문자열로 되어있는 것을 숫자데이터로 변환
for (let i = 1; i < input.length; i++) {
    cows.push(input[i].split(' ').map((item) => +item));
}

// 이동한 소의 위치 표시, N번 소가 오른쪽에 있으면 {N:1}, 왼쪽에 있으면 {N:0}으로 표기됨
let movePosition = {};

// 소의 위치가 변경될때마다 cnt + 1
let cnt = 0;

// cows 배열 인덱스 순회
for (let i in cows) {
    // N번 소가 처음 발견되면 현재 순회중인 소 위치로 초기화
    if (movePosition[cows[i][0]] === undefined) {
        movePosition[cows[i][0]] = cows[i][1];
    } else if (movePosition[cows[i][0]] === cows[i][1]) {
        // 소의 위치가 그대로인 채로 발견되면 배열 계속 순회
        continue;
    } else {
        // 소의 위치가 기존 위치랑 다른 경우
        cnt += 1;

        // 소가 오른쪽에 있으면 왼쪽으로 이동
        if (movePosition[cows[i][0]] === 1) {
            movePosition[cows[i][0]] = 0;
        } else {
            // 소가 왼쪽에 있으면 오른쪽으로 이동
            movePosition[cows[i][0]] = 1;
        }
    }
}

console.log(cnt);
