interface Person {
    name: String,
    age: number
}

let  id = 2332

function greet({name, age} : Person) {
    console.log(`Hello ${name}, you're ${age} years old`);
}

const person : Person = {name: "Joseph", age: 23}

greet(person);