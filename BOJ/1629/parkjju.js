const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
let input = [];
rl.on('line', (line) => {
    input = [
        ...line
            .trim()
            .split(' ')
            // BigInt라는 매우 큰 정수를 저장할 수 있는 자료형
            // map메서드로 각 요소들을 BigInt로 타입 변환 진행
            .map((item) => BigInt(item)),
    ];
    rl.close();
}).on('close', () => {
    console.log(Number(solution(input[0], input[1], input[2])));

    process.exit();
});

// 재귀함수 정의
const solution = (A, B, C) => {
    // B === 1n이면 A%C를 반환해야한다.
    // A를 B번 곱해야하는데 1번 곱하는 것이므로 연산이 끝난다.
    if (B === 1n) {
        return A % C;
    } else if (B === 0n) {
        return 1n;
    }

    // A^2 = A*A
    // A^4 = A^2*A^2
    // 제곱수를 홀/짝수로 나누어 재귀적으로 함수를 호출한다.
    // A를 4번 곱하고 C로 나눈 나머지를 구하는 것은
    // A제곱을 두번 곱하고 C로 나눈 나머지를 구하는 것과 동일하다.
    // A제곱을 C로 나눈 나머지를 제곱하여 C로 다시 나눈 나머지를 구하는건 뭘까?
    // A^B / C + temp1
    // A^B/2 / C + temp2
    // -> 모듈러 성질
    const temp = BigInt(solution(A, B / 2n, C));
    if (B % 2n === 0n) {
        return (temp * temp) % C;
    } else {
        return (A * (temp * temp)) % C;
    }
};

// const solution = (A, B) => {
//     if (B === 1n) {
//         return A;
//     } else if (B === 0n) {
//         return 1n;
//     }

//     if (B / 2n === 0n) {
//         return solution(A, BigInt(B / 2n)) * solution(A, BigInt(B / 2n));
//     } else {
//         return A * solution(A, BigInt(B / 2n)) * solution(A, BigInt(B / 2n));
//     }
// };
