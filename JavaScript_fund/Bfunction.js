// 9 correct out of 13

function a() {
    return 35;
}
console.log(a()) // console it will log on 35;

function a() {
    return 4;
}
console.log(a() + a()); // console it will log on 8. because it's 4 inside of each a(). so a(4)+a(4)=8;

function a(b) {
    return b;
}
console.log(a(2) + a(4));// console it will log on 6. because it's already number's inside of each a() so a(2)+a(4)=6;

function a(b) {
    console.log(b);
    return b * 3;
}
console.log(a(3)); // console it will log on 3, 9. i didn't predict that one correct. my prediction it was just 9. that is false because theretwo console.log()

function a(b) {
    return b * 4;
    console.log(b);
}
console.log(a(10)); // console it will log on 40. i didn't predict that one correct. my prediction it was 16, 40. that is false.

function a(b) {
    if (b < 10) {
        return 2;
    }
    else {
        return 4;
    }
    console.log(b);
}
console.log(a(15));// console it will log on 4. because the only actual value of (b) we know is 15 and that makes it greater than 10. and the first console.log() is inside the loop and that's where it logs.

function a(b, c) {
    return b * c;
}
console.log(10, 3);
console.log(a(3, 10));// console it will log on 10,3,30. the difference with this one and the one above is that both console .log() here is outside the loop, so we have to run the loop twice.

function a(b) {
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    return i;
}
console.log(3);
console.log(4);// i didn't predict that one correct either.

function a() {
    for (var i = 0; i < 10; i++) {
        i = i + 2;
        console.log(i);
    }
}
a();// console it 2,5,8,11.

function a(b, c) {
    for (var i = b; i < c; i++) {
        console.log(i);
    }
    return b * c;
}
a(0, 10);
console.log(a(0, 10)); // console it will log on 0-9 and again 0-9 and then 0.

function a() {
    for (var i = 0; i < 10; i++) {
        for (var j = 0; j < 10; j++) {
            console.log(j);
        }
        console.log(i); // really don't know why but i can't find an output for this one.
    }
}

function a() {
    for (var i = 0; i < 10; i++) {
        for (var j = 0; j < 10; j++) {
            console.log(i, j);
        }
        console.log(j, i); // The same here no output.
    }
}

var z = 10;
function a() {
    var z = 15;
    console.log(z);
}
console.log(z); //console it will log on 10, var z inside the loop it doesn't count.

var z = 10;
function a() {
    var z = 15;
    console.log(z);
}
a();
console.log(z); // console it will log on 15,10.

var z = 10;
function a() {
    var z = 15;
    console.log(z);
    return z;
}
z = a();
console.log(z);// console it will log on on 15, 15.