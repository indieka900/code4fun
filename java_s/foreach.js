const numbers = [12,45,23,41,74,10]

let sum = 0;

function adder(num){
    sum += num;
}

numbers.forEach(adder)

//console.log(`The sum is: ${sum}`);

let double = numbers.map(num => num*2);
//map will not modify the new array but the for each can modify the new array

console.log(double);