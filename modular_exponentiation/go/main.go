package main

func main(){
	s := 5;
	r := 3;
	n := 2;
	p := 1;

	while(r > 0){
		if(p % 2 == 1){
			p = p*s % n;
		}
		s = s*s % n;
		r = r / 2;
	}

	fmt.Println(p);
}