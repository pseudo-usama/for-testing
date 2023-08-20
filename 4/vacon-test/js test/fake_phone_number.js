import { faker } from '@faker-js/faker';


const codes1 = [7, 1]
const codes2 = [20, 31, 47, 51, 63, 64, 48, 40, 65, 82, 34, 66, 90, 84, 33, 30, 49, 36, 91, 92, 62, 98, 39, 81,]
const codes3 = [213, 355, 374, 994, 973, 880, 501, 229, 975, 591, 387, 267, 246, 673, 226, 257, 855, 237,]


let numbers2 = []
for (let i = 0; i < 100; i++) {
  let code = codes2[Math.floor(Math.random() * codes2.length)]
  numbers2.push(faker.phone.number('+' + code + '#########'))
}

let numbers1 = []
for (let i = 0; i < 100; i++) {
  let code = codes1[Math.floor(Math.random() * codes1.length)]
  numbers1.push(faker.phone.number('+' + code + '#########'))
}

let numbers3 = []
for (let i = 0; i < 100; i++) {
  let code = codes3[Math.floor(Math.random() * codes3.length)]
  numbers3.push(faker.phone.number('+' + code + '#########'))
}

console.log(numbers1)
console.log(numbers2)
console.log(numbers3)
