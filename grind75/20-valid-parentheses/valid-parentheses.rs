use std::collections::HashMap;


impl Solution {
    pub fn is_valid(s: String) -> bool {
        let parentheses = HashMap::from([
            (')', '('),
            ('}', '{'),
            (']', '['),
        ]);
        let mut stack: Vec<char> = Vec::new();

        for c in s.chars(){
            if parentheses.contains_key(&c){
                if let (Some(prev_p), Some(&open_p)) = (stack.pop(), parentheses.get(&c)) {
                    if prev_p != open_p {
                        return false
                    }
                } else{
                    return false
                }
            } else{
                stack.push(c)
            }
        }
        return stack.is_empty()
    }
}