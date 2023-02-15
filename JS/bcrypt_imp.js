const bcrypt = require("bcryptjs");
// const plainTextPassword1 = "1234";
/*
for (let saltRounds = 10; saltRounds < 21; saltRounds++) {
  console.time(`bcryptt | cost: ${saltRounds}, time to hash`);
  bcrypt.hashSync(plainTextPassword1, saltRounds);
  console.timeEnd(`bcryptt | cost: ${saltRounds}, time to hash`);
}
*/
// let saltRounds = 12;
// console.time(`bcrypt | 4 digit | time to hash`);
// for (let value = 1000; value <= 9999; value++){
//   bcrypt.hashSync(value,saltRounds);
// }
// console.timeEnd(`bcrypt | 4 digit | time to hash`);


const saltRounds = 4;
console.time(`bcrypt | 4 digit | time to hash`);

for (let value = 1000; value <= 9999; value++) {
    bcrypt
        .hash(value.toString(), saltRounds)
        // .then(hash => {
        //     // console.log(`Hash: ${hash}`);
            // if (value % 100==0)
                // console.log(`hello + ${value}`);
                
            // Store hash in your password DB.
        // })
        // .catch(err => console.error(err.message));
}

console.timeEnd(`bcrypt | 4 digit | time to hash`);

