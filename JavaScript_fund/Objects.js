var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];

console.log(users[1]);

console.log(users[0].age);

for (var i = 0; i < users.length; i++){
    console.log(users[i].name, "-" , users[i].age);
}