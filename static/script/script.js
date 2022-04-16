
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1; //January is 0!
var yyyy = today.getFullYear();

var someday = new Date(yyyy - 50, 1, 1);
var dd1 = someday.getDate();
var mm1 = someday.getMonth();
var yyyy1 = someday.getFullYear();

function check_date(number) {
   if (number < 10) {
      number = '0' + number;
   }
   return number
}

today = yyyy + '-' + check_date(mm) + '-' + (dd);
someday = yyyy1 + '-' + check_date(mm1) + '-' + check_date(dd1);
// console.log(someday)
// console.log(today)
document.getElementById("date").setAttribute("max", today);
document.getElementById("date").setAttribute("value", today);
document.getElementById("date").setAttribute("min", someday);