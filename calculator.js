function calculator(num1, num2, operation){
    let result = 0;
    if (operation === 'add'){
         return num1 + num2;
    }
    else if( operation === 'subtract' ){
        return num1 - num2;
    }
    else if (operation === 'divide'){
        return num1 / num2;
    }
    else if (operation === 'multiply'){
        return num1 * num2;
    }
    else if( operation === 'modulus'){
        return num1 % num2;
    }
    
}
 let num1 = 12, num2 = 2;
 let operation = 'subtract';
 console.log(calculator(num1, num2, operation))