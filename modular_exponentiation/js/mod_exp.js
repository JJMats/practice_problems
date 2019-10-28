let s = 5;
let r = 3;
let n = 2;
let p = 1;

while(r > 0){
    if(r % 2 == 1){
        p = p*s % n;
    }
    s = s*s % n;
    r = r / 2;
}