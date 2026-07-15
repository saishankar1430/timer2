function add(a, b) {
    console.log("addition of the numbers is:");
    console.log(a + b);
}

function subtract(a, b) {   
    console.log("subtraction of the numbers is:");
    console.log(a - b);
}

function multiply(a, b) {
    console.log("multiplication of the numbers is:");
    console.log(a * b);
}

function maths(a,b, operation) {    
    console.log("The result of the operation is:");
    operation(a,b);
}

maths(10, 5, add);