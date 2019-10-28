package main

import "fmt"

func Mod_exp(s, r, n int) int {
	p := 1
	for r > 0 {
		if r%2 == 1 {
			p = p * s % n
		}
		s = s * s % n
		r = int(r / 2)
		//fmt.Println(r)
	}
	return p
}

func main() {
	s := 78
	r := 859
	n := 1829

	fmt.Println(Mod_exp(s, r, n))
}
