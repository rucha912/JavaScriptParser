var name = 'Rucha';

function logName() {
	// 'name' is accessible here and everywhere else
    console.log(name); 
}

// Global Scope
function someFunction() {
    var local;
    function someOtherFunction() {
        var another_local;
    }
}

if (true) {
    // this 'if' conditional block doesn't create a new scope
    // name is still in the global scope
	var my_name = 'Rucha'; 
}


if (true) {
    // this 'if' conditional block doesn't create a scope

    // name is in the global scope because of the 'var' keyword
    var new_name = 'Rucha';
    // likes is in the local scope because of the 'let' keyword
    let likes = 'Coding';
    // skills is in the local scope because of the 'const' keyword
    const skills = 'JavaScript and PHP';
}

//Case #1 for if else statements  
if(isTrue)
    doSomething();
else
    doSomethingElse();


//Case #2 for if else statements  
if(isTrue)
{    
    doSomething();
}
else
{    
    doSomethingElse();
}

//Case #3 for if else statements  
if(isTrue){
    doSomething();
    someOtherFunction();
}    
else
    doSomethingElse();


function grandfather() {
    var name_again = 'Rucha';
    // love is not accessible here
    function parents() {
        // name is accessible here
        // love is not accessible here
        function child() {
            // Innermost level of the scope chain
            // name is also accessible here
            var love = 'Coding';
        }
    }
}

console.log(another_local);
console.log(new_local);
console.log(love);