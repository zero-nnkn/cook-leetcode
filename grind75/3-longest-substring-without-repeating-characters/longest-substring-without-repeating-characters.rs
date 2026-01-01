use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut seen: HashMap<char, usize> = HashMap::new();
        let mut left = 0;
        let mut max_len = 0;

        for (right, c) in s.chars().enumerate() {
            if let Some(&prev_index) = seen.get(&c) {
                if prev_index >= left {
                    left = prev_index + 1;
                }
            }
            seen.insert(c, right);
            max_len = max_len.max(right - left + 1);
        }
        return max_len as i32
    }
}