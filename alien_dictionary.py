from collections import defaultdict, deque

def alien_order(words):
    adj = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}

    for w1, w2 in zip(words, words[1:]):
        for a, b in zip(w1, w2):
            if a != b:
                if b not in adj[a]:
                    adj[a].add(b)
                    indegree[b] += 1
                break

    queue = deque([c for c in indegree if indegree[c] == 0])
    order = []
    while queue:
        c = queue.popleft()
        order.append(c)
        for nei in adj[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return "".join(order) if len(order) == len(indegree) else ""

# 🧪 Test
print("Alien Order:", alien_order(["wrt", "wrf", "er", "ett", "rftt"]))  # "wertf"
