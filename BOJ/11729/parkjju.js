// 데이터 정제
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// 출발지점, 거쳐가는 지점, 도착 지점
let start = 0;
let mid = 1;
let end = 2;
let board = 0;

rl.on('line', (line) => {
    // board : 원판 개수
    board = +line;
    rl.close();
}).on('close', () => {
    // start에서 출발하여
    // mid를 거쳐
    // end까지
    // board개 만큼의 원판을 옮긴다.
    hanoi(start, mid, end, board);

    process.exit();
});

const hanoi = (start, mid, end, boardCount) => {
    // 옮길 블록이 없으면 재귀 호출 종료.
    if (boardCount === 0) {
        return;
    }

    // start에서 mid까지 end를 거쳐 옮기는데
    // 맨 밑바닥 원판은 옮기지 않는다.
    hanoi(start, end, mid, boardCount - 1);

    // 맨 밑바닥 원판을 옮긴다.
    console.log(start + 1, end + 1);

    // mid에서 대기중인 N-1개의 원판을
    // start를 거쳐
    // end로 옮긴다.
    hanoi(mid, start, end, boardCount - 1);
};
