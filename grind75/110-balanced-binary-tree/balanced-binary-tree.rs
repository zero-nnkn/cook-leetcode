// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::cell::Ref;
impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn height(node: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
            match node {
                None => 0,
                Some(rc_node) => {
                    let node_ref: Ref<TreeNode> = rc_node.borrow();

                    let left_height: i32 = height(&node_ref.left);
                    if left_height == -1 {
                        return -1;
                    }

                    let right_height: i32 = height(&node_ref.right);
                    if right_height == -1 {
                        return -1;
                    }

                    let diff: i32 = (left_height - right_height).abs();
                    if diff > 1 {
                        return -1;
                    }

                    let max_child_height: i32 = left_height.max(right_height);
                    1 + max_child_height
                }
            }
        }

        height(&root) != -1
    }
}