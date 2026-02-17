impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.is_empty() {
            return 0;
        }

        let mut profit = 0;
        let mut best_buy_price = prices[0];
        for &price in &prices[1..] {
            if price < best_buy_price {
                best_buy_price = price;
            } else {
                profit = profit.max(price - best_buy_price);
            }
        }

        profit
    }
}