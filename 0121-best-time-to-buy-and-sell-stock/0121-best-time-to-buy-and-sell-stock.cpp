class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int bestBuy = prices[0];
        int max_profit = 0;

        for(int i =1;i<prices.size();i++){
            if (prices[i] > bestBuy) {
                max_profit = max(max_profit,prices[i]-bestBuy);

            }
            bestBuy = min(bestBuy,prices[i]);
        }
        return max_profit;
        
        
    }
};