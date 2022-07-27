// N * N 사이즈만큼 별들을 그려놓고
// 별의 가운데를 재귀적으로 지우는 로직을 기반으로 한다.

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = undefined;

rl.on('line', (line) => {
    // input 데이터 정제
    input = +line;
    rl.close();
}).on('close', () => {
    solution(input);
    process.exit();
});

const solution = () => {
    // 헬퍼메서드 형태
    // N*N 별 그리기
    let arr = [];
    for (let i = 0; i < input; i++) {
        arr.push([]);
        for (let j = 0; j < input; j++) {
            arr[i].push('*');
        }
    }

    // 재귀함수
    // 변의 길이가 N이고
    // 몇 번째 조각을 나타내는지 row, col로 가리킴
    const helper = (N, row, col) => {
        // 변의 길이가 1일 경우 재귀 종료 - 바닥조건
        if (N === 1) {
            return;
        }

        // 가운데 뚫는 로직
        // 가운데 인덱스를 나타내는 N/3 ~ (2*N)/3-1
        // 가운데 뚫는 로직이 현재 사각형 크기 기준으로 곱하기 3 크기의 사각형 나머지 8조각 중 row, col에 해당하는 조각의 가운데를 뚫어야함
        // N*row, N*col 인덱스로 접근해야 곱하기 3 크기 사각형 나머지 8조각 중 하나를 유일하게 선택하게 됨
        for (let i = N / 3; i < (2 * N) / 3; i++) {
            for (let j = N / 3; j < (2 * N) / 3; j++) {
                arr[i + N * row][j + N * col] = ' ';
            }
        }

        // 9조각 나누어 재귀호출
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                // 변의 길이 나누기 3만큼의 크기를 가지는 사각형 조각
                // 조각을 가리키되 현재 row, col은 9조각으로 쪼개진 조각 기준으로 3을 곱한 위치를 가리켜야 함
                // 길이가 9인 변을 9조각으로 나눈 조각 중 2번째 조각은
                // 길이가 3인 부분 조각들 중 3*2+1부터 시작해야함
                helper(N / 3, i + 3 * row, j + 3 * col);
            }
        }
    };

    helper(input, 0, 0);
    arr.forEach((item) => console.log(item.join('')));
};
