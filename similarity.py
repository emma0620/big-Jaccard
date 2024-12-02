def jaccard_index(set_a, set_b):
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union != 0 else 0



def recommendation_index(user_datasets, target_user, dataset):
    target_history = user_datasets[target_user]
    other_histories = [
        user_datasets[other_user]
        for other_user in user_datasets
        if dataset in user_datasets[other_user]
    ]
    if not other_histories:  # 沒有其他使用者使用該資料集
        return 0
    jaccard_sums = sum(jaccard_index(target_history, history) for history in other_histories)
    return jaccard_sums / len(other_histories)