use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut map: HashMap<char, i32> = HashMap::new();
        for c in s.chars() {
            *map.entry(c).or_insert(0) += 1
        }

        for c in t.chars() {
            if let Some(count) = map.get_mut(&c) {
                *count -= 1;

                if *count < 0 {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true
    }
}