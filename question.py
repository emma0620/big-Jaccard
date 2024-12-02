import pandas as pd
from itertools import combinations
from collections import defaultdict
from similarity import jaccard_index, recommendation_index

# Step 1: 讀取並處理資料
data_file = "data.txt"
data = pd.read_csv(data_file, sep="\t")

user_datasets = defaultdict(set)
for _, row in data.iterrows():
    user_datasets[row["User ID"]].add(row["Dataset ID"])

# Step 2: 找出雅卡爾指數最高的兩位使用者
highest_jaccard = 0
most_similar_users = None

for user1, user2 in combinations(user_datasets.keys(), 2):
    jaccard = jaccard_index(user_datasets[user1], user_datasets[user2])
    if jaccard > highest_jaccard:
        highest_jaccard = jaccard
        most_similar_users = (user1, user2)

# Step 3: 計算推薦指數 R(HX, S) / # 找出 andrew 尚未使用過的資料集
andrew_history = user_datasets["andrew"]
all_datasets = set(data["Dataset ID"])
candidate_datasets = all_datasets - andrew_history

# 計算每個候選資料集的推薦指數
recommendations = {
    dataset: recommendation_index(user_datasets, "andrew", dataset)
    for dataset in candidate_datasets
}

# 找出推薦指數最高的三個資料集
top_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:3]

# Step 4: 輸出結果
print("1. 最相似的兩位使用者及雅卡爾指數:")
print(f"   使用者: {most_similar_users}, 雅卡爾指數: {highest_jaccard:.2f}")

print("\n2. 最應推薦給 andrew 的三個資料集:")
for i, (dataset, score) in enumerate(top_recommendations, start=1):
    print(f"   第{i}名: 資料集 {dataset}, 推薦指數: {score:.2f}")