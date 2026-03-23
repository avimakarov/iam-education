impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut x = x as i64;
        let mut r = 0 as i64;
        let sign: i64 = if x < 0 { x = -x; -1 } else { 1 };

        while x != 0 {
            r = r * 10 + x % 10;
            x /= 10;
        }
        r *= sign;
        if r < i32::MIN as i64 || r > i32::MAX as i64 {
            return 0;
        }
        r as i32
    }
}

struct Solution;

fn main() {
     println!("{}", Solution::reverse(123));
}