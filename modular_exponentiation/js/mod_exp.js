let s = 79;
let r = 859;
let n = 1829;
let p = 1;

while(r > 0){
    if(r % 2 == 1){
        p = p*s % n;
    }
    s = s*s % n;
    r = Math.floor(r / 2);
}

console.log(p);