function solution(n, edge) {
    let myArr = Array.from(Array(n+1), () => Array())
    for (let i = 0; i < edge.length; i++) {
        myArr[edge[i][0]].push(edge[i][1]);
    }
    let result = new Array(n+1).fill(0)
    let stack = myArr[1]
    count = 1;
    let temp = []
    while (stack.length !== 0) {
        let value = stack.pop();
        result[value] = count;
        myArr[value].map((val) => {
            temp.push(val);
        })
        console.log(stack);
        if (stack.length === 0 && temp.length !== 0) {
            stack = temp.slice();
            temp.length = 0;
            count += 1;
        }
    }
    console.log(result)
}

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]);