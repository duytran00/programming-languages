//Duy Tran
//1002190361
//2-25-2025

//#1
const inputtable = [1,2,3,4,5,6,7,8,9,10]; //create array called inputtable containing 1-10

//#2
const fiveTable = inputtable.map(x => x * 5);
console.log(fiveTable);
//create set of multiples of 5 from inputtable by multiplying each element by 5
const thirteenTable = inputtable.map(x => x * 13);
console.log(thirteenTable);
//create set of multiples of 13 from inputtable by multiplying each element by 13
const squaresTable = inputtable.map(x => x * x); 
console.log(squaresTable);
//create set of squares from inputtable by multliplying each element by itself

//#3
const multiplesOfFive = Array.from({length:20}, (_, i) => (i + 1) * 5);
//create array by multiplying each number by 5 until 100
const odds = multiplesOfFive.filter(x => x % 2 !== 0);
//filter multiples of 5 that are not divisible by 2
console.log(odds);

//#4
const multiplesOfSeven = Array.from({length:14},  (_, i) => (i + 1) * 7);
//create array by multiplying each number by 7 until 98
const evens = multiplesOfSeven.filter(x => x % 2 === 0);
//filter multiples of 7 that are divisible by 2
const sum = evens.reduce((total, y) => total + y, 0);
//staring at 0 reduce evens into single number by callback
console.log(sum);

//#5
const cylinder_volume = r => h => 3.14 * r * r * h;
//This version of cylinder_volume takes one parameter now then another one later
console.log(cylinder_volume(5)(10));
//the second parameter taken later by cylinder_volume
console.log(cylinder_volume(5)(17));
console.log(cylinder_volume(5)(11));

//#6
makeTag = function(beginTag, endTag){ 
    return function(textcontent){ 
       return beginTag +textcontent +endTag; 
    } 
}
//Higher-order rule: outer then inner
//Equivalent to grandparent(begin,end) returning parent(content)
const table = makeTag("<table>\n","</table>\n");
const tr = makeTag("<tr>\n","</tr>\n");
const th = makeTag("<th>","</th>\n");
const td = makeTag("<td>", "</td>\n");
//Equivalent to parent functions (table, tr,...) store grandparent values (maketag)
const header =  tr(th("city") + th("state") + th("zip code"));
const content1 = tr(td("atlanta") + td("georgia") + td("111"));
const content2 = tr(td("wichita") + td("kansas") + td("222"));
//Equivalent to children (td, th) are made inside parent functions
const htmlTable = table(header + content1 + content2);
//output order through htmlTable by outermost
//Equivalent to parent funtions (table) store children values (header,content)
console.log(htmlTable);

//#7
const getMultiplesOrSum = (multiple) => (isOdd) => (shouldSum) => {
    //Curried multiple parameters accepted one at a time
    let remainder = 0;
    if (isOdd) {
        remainder = 1;
    }
    
    const numbers = Array.from({ length: 100 }, (_, i) => i + 1)
        .filter(x => x % multiple === 0 && x % 2 === remainder);
    //Target mulitples are not hard coded. Handled by mod of variable "multiple"

    if (shouldSum) {
        return numbers.reduce((total, y) => total + y, 0);
    }
    return numbers;
};
const oddMultiplesOf11 = getMultiplesOrSum(11)(true);
//First function call retains values of 11 and odd
console.log(oddMultiplesOf11(false)); //Remembers odd multiples of 11 and takes next value
//Closure: function retains values for the next call
console.log(getMultiplesOrSum(3)(false)(true));

