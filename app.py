from flask import Flask, render_template, request

app = Flask(__name__)

# Strictly allowed coin denominations
VALID_COINS = {1, 2, 5, 10, 20}

def get_coin_logic(amount, coins):
    # 1. DP: Count Total Ways
    ways = [0] * (amount + 1)
    ways[0] = 1
    # Sort ascending for standard combination counting
    for coin in sorted(coins):
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]
            
    # 2. DP: Find Minimum Coins Needed
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    
    result_min = min_coins[amount] if min_coins[amount] != float('inf') else "Not Possible"
    
    # 3. DFS: Generate Combinations (Capped at 100 to prevent crashing)
    combinations = []
    coins_desc = sorted(coins, reverse=True) # Sort descending to show largest coins first
    
    def dfs(remain, start_idx, current_combo):
        if len(combinations) >= 100: 
            return # Stop if we hit the limit
        if remain == 0:
            # Format the list [20, 20, 5] into a dictionary {20: 2, 5: 1}
            freq = {}
            for c in current_combo:
                freq[c] = freq.get(c, 0) + 1
            combinations.append(freq)
            return
            
        for i in range(start_idx, len(coins_desc)):
            if coins_desc[i] <= remain:
                dfs(remain - coins_desc[i], i, current_combo + [coins_desc[i]])
                
    dfs(amount, 0, [])
    
    return ways[amount], result_min, combinations

@app.route('/')
def index():
    
    return render_template("index.html", total_ways=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        amount = int(request.form.get('amount'))
        
        # Get selected coins from the checkboxes
        selected_coins = request.form.getlist('coins')
        # Filter strictly against our VALID_COINS list
        coins = sorted([int(c) for c in selected_coins if int(c) in VALID_COINS])
        
        if not coins:
            return "Error: Please select at least one valid coin.", 400
        if amount <= 0:
            return "Error: Amount must be greater than 0.", 400

        total_ways, min_needed, combinations = get_coin_logic(amount, coins)
        
        return render_template('index.html', 
                               amount=amount, 
                               selected_coins=coins,
                               total_ways=total_ways, 
                               min_needed=min_needed,
                               combinations=combinations)
    except Exception as e:
        return f"Error: Check your inputs. Details: {e}", 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)