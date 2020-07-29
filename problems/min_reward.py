def min_reward_naive(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[i + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1])
                j -= 1
    return sum(rewards)


def min_reward_fastest(scores):
    rewards = [1 for _ in range(len(scores))]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    for i in reversed(range(len(scores) -1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)
