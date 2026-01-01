use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        // let mut last_index: HashMap<char, usize> = HashMap::new();
        // let mut start = 0;
        // let mut max_len: usize = 0;
        // for (end, c) in s.chars().enumerate() {
        //     if let Some(&prev_index) = last_index.get(&c) {
        //         if prev_index >= start {
        //             start = prev_index + 1;
        //         }
        //     }
        //     last_index.insert(c, end);
        //     max_len = max_len.max(end - start + 1);
        // }
        // return max_len as i32

        let mut last_index = [0; 128];
        let mut start = 0;
        let mut max_len = 0;
        
        for (end, ch) in s.chars().enumerate() {
            start = start.max(last_index[ch as usize]);
            max_len = max_len.max(end - start + 1);
            last_index[ch as usize] = end + 1;
        }
        
        return max_len as i32
    }
}