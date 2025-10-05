#Association Rule Mining
#Step 1: Import Libraries 
import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules

#Step 2: Example Dataset 
# #We’ll create a small transaction dataset like a supermarket: 
dataset = [ ['Milk', 'Bread', 'Eggs'], ['Milk', 'Bread'], ['Milk', 'Eggs'], ['Bread', 'Eggs'], ['Milk', 'Bread', 'Butter'], ['Bread', 'Butter'] ] 
# Convert to one-hot encoded DataFrame 
from mlxtend.preprocessing import TransactionEncoder 
te = TransactionEncoder() 
te_array = te.fit(dataset).transform(dataset) 
df = pd.DataFrame(te_array, columns=te.columns_) 
print(df)

# Step 3: Find Frequent Itemsets (Apriori) 
# # min_support = 0.3 → item must appear in at least 30% of transactions 
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True) 
print(frequent_itemsets)

# Step 4: Generate Association Rules 
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6) 
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])