const arr = [1, 2, 4, 3, 4, 5, 6, 7, 7, 8, 6, 10]

let unique = []
let duplicated = []

for (let i = 0; i < arr.length - 1; i++) {
    if (unique.find(e => e == arr[i]))
        duplicated.push(arr[i])
    else
        unique.push(arr[i])
}


console.log(duplicated)