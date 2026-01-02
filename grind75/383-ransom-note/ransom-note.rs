use std::collections::HashMap;


impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut counts: HashMap<char, i32> = HashMap::new();

        // Count characters in magazine
        for ch in magazine.chars() {
            *counts.entry(ch).or_insert(0) += 1;
        }

        // Use characters for ransom_note
        for ch in ransom_note.chars() {
            match counts.get_mut(&ch) {
                Some(count) if *count > 0 => {
                    *count -= 1;
                }
                _ => return false,
            }
        }

        return true
    }
}