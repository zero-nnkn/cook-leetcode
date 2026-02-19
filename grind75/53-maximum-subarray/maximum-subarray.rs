impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut current: i32 = nums[0];
        let mut best: i32 = nums[0];

        for &num in nums.iter().skip(1) {
            current = num.max(current + num);
            best = best.max(current);
        }

        best
    }
}