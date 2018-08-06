// var number = 4;
// function sum(number){
//     if (number <= 0){
//         return false;
//     }
//     return number + sum(number - 1);
// };
// var result = sum(number);
// console.log(result);


// function pairSumSequence(n){
//     var sum = 0;
//     for (let i = 0; i < n; i++){
//         sum += pairSum(i, i + 1);
//     }
//     return sum;
// }

// function pairSum(a, b){
//     return a + b;
// }

// var test = pairSumSequence(4);
// console.log(test);
// var array = [1,2,3,4,5,6,7,8]

// function reverse(array){
//     var reversedArray = [];

//     for(let i = 0; i < array.length / 2; i++){
//         console.log('--------------------------')
//         console.log('Array divided by 2 ' + array.length / 2)
//         console.log('--------------------------')

//         var other = array.length - i - 1;
//         console.log('step 1: other - ', other);

//         var temp = array[i];
//         console.log('step 2: temp - ', temp);

//         array[i] = array[other];
//         reversedArray.push(array[i]);
//         console.log('step 3: array[i] - ', array[i]);

//         array[other] = temp;
//         reversedArray.push(array[other]);
//         console.log('step 4: array[other] - ', array[other]);
//     }
//     console.log(reversedArray);
// }

// var test = reverse(array);
// console.log(test);


// algorithm that will add everything in the array including the nexted array.
// var array = [1,1,1,[1,1,[1]],1];

// function sumNested(array){
//     var result = 0;
//     for(let i = 0; i < array.length; i++){
//         if(typeof array[i] !== 'number'){
//             result += sumNested(array[i]);
//         } else {
//             result += array[i];
//         }
//     }
//     return result;
// }
// var test = sumNested(array);
// console.log(test)



