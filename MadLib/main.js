


// function evenNumber(a){
//     var total = 0;
//     for (var i =0; i < a.length; i++) {
//         if(a[i]%2==0){
//             total +=1;

//     }
// }
// return total;
// };
// var evens = evenNumber([4,4,5,4,7])
// console.log(evens);

//--------PROMPTS----------------
var name = prompt("Made up name"); //prompting user for a "made up name"
var age = prompt("Random number");
var color = prompt("Random Color");
var year = prompt("Your birth year");
var food = prompt("Fav food");
var weight = prompt("Weight");
var length = prompt("Random Lenght");
var width = prompt("Randome widht");
//-------END PROMPTS--------------

//conditional
if (weight>200){
	console.log ("You're fat");
}else{
	console.log("Youre not fat");
};
//------------

//function
function area(l,w){
	var pArea = l*w;
	return pArea;
}
//--------

console.log(area(length,width));

var favName1 = prompt("Boy name");
var favName2 = prompt("Girl Name");
var favName3 = prompt("Cat name");

var car = {color:color,year:year};


var favNames = [favName1,favName2,favName3];
console.log(name+" "+"Liked to eat lots of chicken nuggets, he was "+age+"Years old "+"Born in the year "+year+"His favorite color was"+color+"his favorite friends were"+"he had a "+car.year+car.color+"Car");
//--------loop
for(var i = 0; i<favNames.length;i++){
	console.log(favNames[i]);

}
//-------



// object 


























