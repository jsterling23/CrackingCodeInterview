var n = 5;
function fib(n){
    if( n <= 0) return false;
    else if (n == 1) return 1;
    console.log(fib(n - 1) + fib(n - 2));
}

var test = fib(n);
console.log(test);