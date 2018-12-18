var fibonacci = (n) => {
    if (n < 2){
        return n;
    }
    return fibonacci (n-1) + fibonacci(n-2);
}

var gcd = (a, b) =>{
    var ctr = 1;
    var gcd= 0; 
    var min;
    
    if (a < b){
        min = a;
    }
    else{
        min = b;
    }    
    while (ctr <= min){
     
        if (a%ctr == 0 && b%ctr == 0){
            gcd = ctr;
        }
        ctr += 1;
    }
    return gcd;
}
var randomStudent = () =>{
    var students = ['jerry','clara','jason'];
    var index = Math.floor((Math.random() * students.length));
    return students[index];
}
