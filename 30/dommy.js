// recursive function for returning nth number in the fibonacci sequence
var fibonacci = (n) => {
    if (n < 2){
        return n;
    }
    return fibonacci (n-1) + fibonacci(n-2);
}

/**************
 gcd returns the greatest common denominator for ints a, b
 This method uses Euclid's algorithm to find GCD recursively.                
 First, the larger and smaller inputs are identified.  
 If either is equal to 0, then 0 is returned. 
 If large is divisible by small, then small is returned      
 Otherwise, large becomes largest - small and the gcdER of these two integers
 is called.
***************/
var gcd = (a, b) =>{
    var large = max(a, b);
    var small = min(a, b);
    if (small == 0){
        return 0;
    }
    if (large %small == 0){
        return small;}
    else {
            large = large - small;
        return gcd(large, small);
    }
}

// helper function return max of a and b
var max = (a, b) => {
    if (a > b){
	return a;
    }
    return b;    
}

// helper function returns min of a and b
var min = (a, b) => {
    if (a < b){
	return a;
    }
    return b;
}


// function for returning random 
var randomStudent = () =>{
    var students = ['jerry','clara','jason'];
    var index = Math.floor((Math.random() * students.length));
    return students[index];
}

// change heading function
var changeHeading = function(e){
    var h = document.getElementById("h");
    h.innerHTML = e.target.innerHTML;
}

// function to remove an item from list
var removeItem = function(e){
    e.target.remove(); //can replace e.target with 'this'
};

// for every liste item, do :
var lis = document.getElementsByTagName("li");
for (var i = 0; i < lis.length; i++){
    // if mouse hovers over, change heading
    lis[i].addEventListener("mouseover", changeHeading);
    // if mouse goes away, go back to original heading
    lis[i].addEventListener("mouseout", function(){
	h.innerHTML = "Hello World!";
    })
    // if click on li, remove
    lis[i].addEventListener("click", removeItem);
}

// add item using button
var addItem = function(e){
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    list.appendChild(item);
};

// when button is clicked, call addItem
var button = document.getElementById("b");
button.addEventListener("click", addItem);

// fibnum keeps track of where in fibonacci sequence we are at
var fibnum = 0;
// checks if there is a fib list. if not, it creates
var addFib = function(e){
    console.log(e);
    if (document.getElementById("fib") == null){
	var list = document.createElement("ol");
	list.setAttribute("id", "fib");
	document.body.appendChild(list);
	console.log(list);	
    }
    // call fib2() to add item
    addFib2();
};

// add list item based on where we are in fib sequence
var addFib2 = function(e) {
    console.log("made it here");
    var list = document.getElementById("fib");
    var item = document.createElement("li");
    item.innerHTML = fibonacci(fibnum);
    list.appendChild(item);
    fibnum += 1;
};

// if click on button, add to fib sequence
var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
