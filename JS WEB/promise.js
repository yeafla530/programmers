findUser(1).then(function (user) {
    console.log('user:', user)
//     waited 0.1 sec.
//     user: {id: 1, name: "User1", email: "1@test.com"}
})

function findUser(id) {
    return new Promise(function (resolve) {
        setTimeout(function () {
            console.log("waited 0.1 sec")
            const user = {
                id : id,
                name: "User" + id,
                email: id + "@test.com"
            }
            resolve(user)
        }, 100)
    })
}

function devide(numa, numb) {
    return new Promise((resolve, reject) => {
        if (numb === 0) reject(new Error("Unable to devide by "))
        else resolve(numa/numb)
    })
}

devide(8, 2)
    .then((result) => console.log('성공', result)) //성공 4
    .catch((error) => console.log("실패", error)) // Error: Unable to devide by 


// fetch 사용
// npm i node-fetch --save
// const fetch = require("node-fetch");
const fetch = require("node-fetch");
fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then((response) =>  response.json())
    .then((post) => post.userId)
    .then((userId) => "https://jsonplaceholder.typicode.com/users/" + userId)
    .then((url) => fetch(url))
    .then((res) => res.json())
    .then((user) => console.log('user', user))
    .catch((error) => console.log("err", error))
