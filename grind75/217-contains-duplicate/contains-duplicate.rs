use std::collections::HashSet;


impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::new();

        for num in nums {
            let is_new = seen.insert(num);
            if !is_new {
                return true;
            }
        }
        false
    }
}