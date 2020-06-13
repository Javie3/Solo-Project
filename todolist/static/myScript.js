var today = new Date();
var hourNow = today.getHours();
var greeting;

if (hourNow >  18) {
    greeting = 'Good Evening, What Should We do Today!';

} else if (hourNow > 12 ){
    greeting = 'Good Afternoon, What Should We do Today!';

}else if (hourNow > 0 ){
    greeting = 'Good Morning, What Should We do Today! '
}
document.write(greeting);


