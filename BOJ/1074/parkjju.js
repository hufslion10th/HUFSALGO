const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = undefined;
rl.on('line', (line) => {
    input = line
        .trim()
        .split(' ')
        .map((item) => +item);
    rl.close();
}).on('close', () => {
    Z(input[0], input[1], input[2]);
    process.exit();
});

const Z = (N, r, c) => {
    let result = [];
    const helper = (N, r, c) => {
        if (N === 1) {
            if (r === c && r === 0) {
                return 1;
            } else if (r < c) {
                return 2;
            } else if (r > c) {
                return 3;
            } else {
                return 4;
            }
        }
        if (r < 2 ** (N - 1) && c < 2 ** (N - 1)) {
            const a = helper(N - 1, r, c);
        } else if (r < 2 ** (N - 1) && c >= 2 ** (N - 1)) {
            result.push(
                helper(N - 1, r, c - 2 ** (N - 1)) + (2 ** (N - 1)) ** 2
            );
        } else if (r >= 2 ** (N - 1) && c < 2 ** (N - 1)) {
            result.push(
                helper(N - 1, r - 2 ** (N - 1), c) + (2 ** (N - 1)) ** 2 * 2
            );
        } else {
            result.push(
                helper(N - 1, r - 2 ** (N - 1), c - 2 ** (N - 1)) +
                    (2 ** (N - 1)) ** 2 * 3
            );
        }
    };
    helper(N, r, c);
    console.log(result);
};
