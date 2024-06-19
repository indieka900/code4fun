const numbers = [12,45,23,41,74,10]

let sum = 0;

function adder(num){
    sum += num;
}

numbers.forEach(adder)

//console.log(`The sum is: ${sum}`);

let double = numbers.map(num => num*2);
//map will not modify the new array but the for each can modify the new array

//console.log(double);

//example 2 on map
let people = [
    {firstname: "Joseph", secondName:"Indieka", age: 20},
    {firstname: "John", secondName:"Ali", age: 18},
    {firstname: "Karen", secondName:"Mammk", age: 23},
    {firstname: "Bradely", secondName:"Kanyari", age: 15}
]

const results = people.map(person => {
    return [
        person.firstname.toLowerCase(), 
        person.secondName.toUpperCase(), 
        person.age <= 18 ? 'Underage' : "Above age"
    ]
})

//console.log(results);

//challenge
function multi(num){
   return num * 10;
} 
const newNumbers = numbers.map(multi)

console.log(newNumbers);