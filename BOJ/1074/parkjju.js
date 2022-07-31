const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// 전역변수로 쓰레기값을 선언할 수 없기 때문에 undefined 선언
let input = undefined;
rl.on('line', (line) => {
    // 데이터 정제
    input = line
        .trim()
        .split(' ')
        .map((item) => +item);
    rl.close();
}).on('close', () => {
    // 함수 호출
    console.log(helper(input[0], input[1], input[2]));
    process.exit();
});

const helper = (N, r, c) => {
    // 2*2사이즈일때 행 / 열 판단하여 0,1,2,3값 리턴
    if (N === 1) {
        if (r === c && r === 0) {
            return 0;
        } else if (r < c) {
            return 1;
        } else if (r > c) {
            return 2;
        } else {
            return 3;
        }
    }

    if (r < 2 ** (N - 1) && c < 2 ** (N - 1)) {
        // 행 / 열이 1사분면일때
        // 사각형 사이즈만 2^(N-1) by 2^(N-1)로 줄인다.
        const temp = helper(N - 1, r, c);
        return temp;
    } else if (r < 2 ** (N - 1) && c >= 2 ** (N - 1)) {
        // 행 / 열이 2사분면일때
        // 1사분면 사이즈만큼 숫자를 더해주고
        // 재귀적으로 2사분면에서의 행 / 열 위치값을 계산해준다.
        const temp = helper(N - 1, r, c - 2 ** (N - 1)) + (2 ** (N - 1)) ** 2;
        return temp;
    } else if (r >= 2 ** (N - 1) && c < 2 ** (N - 1)) {
        // 행 / 열이 3사분면일때
        // 1,2사분면 사이즈를 합친 것 만큼 숫자를 더해주고
        // 재귀적으로 3사분면에서의 행 / 열 위치값을 계산해준다.
        const temp =
            helper(N - 1, r - 2 ** (N - 1), c) + (2 ** (N - 1)) ** 2 * 2;
        return temp;
    } else {
        // 동일
        const temp =
            helper(N - 1, r - 2 ** (N - 1), c - 2 ** (N - 1)) +
            (2 ** (N - 1)) ** 2 * 3;
        return temp;
    }
};
