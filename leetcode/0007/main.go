package main

import (
	"log"
	"math"
)

func reverse(x int) int {
	r := 0
	sign := 1
	if x < 0 {
		x = -x
		sign = -1
	}
	for x != 0 {
		r = r*10 + x%10
		x /= 10
	}
	r *= sign
	if r < math.MinInt32 || r > math.MaxInt32 {
		return 0
	}
	return r
}

func main() {
	tests := []struct {
		in, out int
	}{
		{
			in:  123,
			out: 321,
		},
		{
			in:  -123,
			out: -321,
		},
		{
			in:  120,
			out: 21,
		},
		{
			in:  1,
			out: 1,
		},
		{
			in:  1534236469,
			out: 0,
		},
	}
	for _, v := range tests {
		res := reverse(v.in)
		if res != v.out {
			log.Printf("failed: want (%d), got (%d) \n", v.out, res)
		}
	}
}
