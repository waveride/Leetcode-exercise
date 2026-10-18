"""
第1题：有效记录统计（热身，10分钟）

给定n条记录，每条记录包含一个整数数值v和一个质量标记q。

q=0表示有效记录。
q=1表示无效记录。

输出有效记录的数量、数值总和和最大值。如果没有有效记录，输出0 0 0
"""

def num_1(n):
    count_val = 0
    sum_val = 0
    max_val = None
    for _ in range(n):
        v, q = map(int, input().split())
        if q == 0:
            count_val +=1
            sum_val += v

            if max_val is None or v > max_val:
                max_val = v
    if count_val == 0:
        print("0 0 0")
    else:
        print(count_val, sum_val, max_val)

"""
有n个专家，每个专家有编号id和整数匹配分数score。
只考虑分数大于0的专家，按照以下规则排序：
1. 分数高的优先。
2. 分数相同时，编号小的优先。
选取前k个专家，输出他们的编号。如果符合条件的专家不足k个，输出全部；如果没有符合条件的专家，输出-1。
"""
def num_2():
    n, k = map(int, input().split())


    experts = []
    for _ in range(n):
        eid, score = map(int, input().split())
        if score > 0:
            experts.append((eid, score))

    experts.sort(key=lambda x: (-x[1], x[0]))

    selected_experts = experts[:k]
    if selected_experts:
        print(" ".join(str(expert[0]) for expert in selected_experts))
    else:
        print("-1")


"""
第3题：KV缓存稀疏保留（25分钟）
共有L层，每层H个注意力头，每个头有N个token，其注意力分数均为整数。
需要在预算M内选择保留的token。一个保留项由(层编号, 头编号, token下标)确定，不同层或不同头的同一下标分别占用预算。
规则如下：
- 每层每头都必须保留下标为C的token。
- 其余候选按分数从高到低选择。
- 分数相同时，依次按层编号、头编号、token下标升序选择。
- 最终恰好保留M项。
- 各层、各头和token下标均从0开始。
"""

def num_3():
    L, H, N, M, C = map(int, input().split())
    scores = []
    for _ in range(L):
        layer_scores = []
        for _ in range(H):
            row = list(map(int, input().split()))
            layer_scores.append(row)
        scores.append(layer_scores)

    c_socre = set()
    for l in range(L):
        for h in range(H):
            c_socre.add((l, h, C))

    remain = M - L*H

    if remain <0:
        print("Invalid input: M is less than the number of required tokens.")
    else:
        candidates = []
        for l in range(L):
            for h in range(H):
                for n in range(N):
                    if n == C:
                        continue
                    s = scores[l][h][n]
                    candidates.append((-s, l, h, n))
        candidates.sort()
        selected = candidates[:remain]

        res = list(c_socre) + [item[1:] for item in selected]
        for item in res:
            print(item)

"""
平面上有 N 个基站。基站 i 和 j 的距离为：
\(d(i,j)=|x_i-x_j|+|y_i-y_j|\)
距离不超过 E 的基站属于彼此的邻域。每个基站的邻域包含自身。
给定数量门限 K，分类规则如下：
邻域中的基站数量至少为 K：核心点，输出 0。
不是核心点，但邻域中存在至少一个核心点：边界点，输出 1。
其他情况：噪声点，输出 2。
输入格式
第一行三个整数 N E K。
接下来 N 行，每行两个整数 x y。
"""
def num_4():
    N, E, K = map(int, input().split())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    neighbors_count = [[] for _ in range(N)]
    for i in range(N):
        xi, yi = points[i]
        for j in range(N):
            xj, yj = points[j]
            dist = abs(xi - xj) + abs(yi - yj)
            if dist <= E:
                neighbors_count[i].append(j)


"""
定训练集中的n个类别编号，以及测试集中的m个类别编号。
某类别的编码值等于：
\[
编码值=\frac{该类别在训练集中出现的次数}{n}
\]
请输出每个测试类别的编码值。训练集中未出现的类别，编码为0。统计次数时只使用训练集。
"""
def num_5():
    n, m = map(int, input().split())
    "存一个字典遍历训练集中的类别与数量，然后判断测试集中的类别是否在字典中，若在则输出编码值，否则输出0"

    train = list(map(int, input().split()))
    test = list(map(int, input().split()))

    freq = {}

    for category in train:
        if category in freq:
            freq[category] += 1
        else:
            freq[category] = 1

    res = []
    for cat in test:
        if cat in freq:
            val = freq[cat] / n
        else:
            val = 0
        res.append(f"{val:.2f}")

    print(" ".join(res))

"""
给定长度为n的实数序列a、窗口半径r和阈值k。
对于下标i，窗口包含从max(0, i-r)到min(n-1, i+r)的所有元素，包括两端。
计算窗口均值avg：
- 如果abs(a[i] - avg) > k，将结果b[i]设为avg。
- 否则，设为a[i]。
所有窗口均值都根据原始序列a计算。
"""
def num_6():
    n, r, k = map(int, input().split())
    a = list(map(float, input().split()))
    b=[0]*n

    for i in range(n):
        left =max(0, i-r)
        right = min(n-1, i+r)
        window = a[left:right+1]
        avg = sum(window)/len(window)
        if abs(a[i]-avg)>k:
            b[i]=avg
        else:
            b[i]=a[i]

    print(" ".join(f"{x:.2f}" for x in b))

"""
第7题：一元线性回归训练
建议用时：25分钟
模型为：
\[
\hat y=wx+b
\]
初始时w=0、b=0。训练共进行T轮，每轮按输入顺序逐条处理训练样本。
每处理一条样本(x, y)：
\[
\begin{aligned}
\delta &= wx+b-y,\\
w &\leftarrow w-\eta\delta x,\\
b &\leftarrow b-\eta\delta.
\end{aligned}
\]
同一条样本的两次参数更新使用同一个、更新前计算的delta。
训练结束后，用最终参数对测试数据进行预测。
输入格式
第一行三个数n T eta，前两个为整数，第三个为实数。
接下来n行，每行两个实数x y。
然后一行整数m。
最后一行m个实数，表示测试数据的x。
输出格式
第一行输出最终的w b。
第二行输出m个预测值。
所有结果保留四位小数。
"""


def num_7():
    n, T, eta = input().split()
    n = int(n)
    T = int(T)
    eta = float(eta)

    train_data = []
    for _ in range(n):
        x, y = map(float, input().split())
        train_data.append((x, y))

    m = int(input())
    test_data = list(map(float, input().split()))

    w, b = 0.0, 0.0

    for _ in range(T):
        for x, y in train_data:
            delta = w*x + b - y
            w -= eta * delta * x    
            b= b - eta * delta

    print(f"{w:.4f} {b:.4f}")
    predictions = [w*x + b for x in test_data]
    print(" ".join(f"{pred:.4f}" for pred in predictions))

"""
有长度为N的三个实数序列Q、K、V。本题每个位置只有一个数值，窗口半径为r。
对于位置i，只考虑满足|i-j| ≤ r且不越界的位置j。
先计算窗口内每个位置的分数：
\[
s_j=Q_iK_j
\]
然后计算稳定的Softmax权重：
\[
p_j=\frac{\exp(s_j-s_{\max})}
{\sum_{u\text{ 在窗口内}}\exp(s_u-s_{\max})}
\]
其中s_max是当前窗口内的最大分数。
最终输出：
\[
O_i=\sum_{j\text{ 在窗口内}}p_jV_j
\]
"""
import math
def num_8():
    N, r = map(int, input().split())
    Q = list(map(float, input().split()))
    K = list(map(float, input().split()))
    V = list(map(float, input().split()))

    res = []
    for i in range(N):
        scores = []
        left = max(0, i-r)
        right = min(N-1, i+r)
        for j in range(left, right+1):
            scores.append(Q[i]*K[j])

        smax = max(scores)

        exp_scores = [math.exp(s - smax) for s in scores]

        sum_exp = sum(exp_scores)


        oi = 0.0
        for k in range(len(exp_scores)):
            pj = exp_scores[k] / sum_exp
            j = left + k
            oi += pj * V[j]
        res.append(oi)

    print(" ".join(f"{o:.4f}" for o in res))


import numpy as np

def num_8np():
    N, r = map(int, input().split())
    Q = np.array(list(map(float, input().split())))
    K = np.array(list(map(float, input().split())))
    V = np.array(list(map(float, input().split())))

    res = []

    for i in range(N):
        left = max(0, i-r)
        right = min(N-1, i+r)
        scores = Q[i] * K[left:right+1]

        smax = scores.max()
        exp = np.exp(scores - smax)

        p = exp / exp.sum()

        oi = np.sum(p * V[left:right+1])

        res.append(oi)

    print(" ".join(f"{o:.4f}" for o in res))


def num_9():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 0:
        print(0)
    else:
        dp = [0] * (n + 1)
        dp[1] = max(0, a[0])
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + a[i-1])
        print(dp[n])
    
def num_10():
    a = list(map(int, input().split()))

    dp =[]

    dp[1] = 1 
    dp[2] = 2
    for i in range(3, len(a) + 1):
        dp[i] = dp[i-1] + dp[i-2]

    print(" ".join(f"{d:.4f}" for d in dp[1:]))

"""
第10题：KV缓存页驻留收益——两状态DP
有n页缓存，按顺序编号为1到n。
- 保留第i页，获得收益g[i]，可能为负数。
- 如果第i页和第i+1页都保留，额外获得收益w[i]。
- 每页最多保留一次，可以一页都不保留。
求最大总收益。
"""

def num_11():
    n = int(input())
    g = list(map(int, input().split()))

    if n>1:
        w = list(map(int, input().split()))

    dp = [[0,0] for _ in range(n+1)]
    dp[1][0] = 0
    dp[1][1] = g[0]
    for i in range(2, n+1):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = max(dp[i-1][0]+g[i-1], dp[i-1][1]+w[i-2]+g[i-1])

    res = max(dp[n][0], dp[n][1])
    ans = max(res, 0)
    print(ans)


"""
第11题：任务双配置选择——二选一背包
有n个任务，每个任务必须选择一种配置：
- 配置1消耗c1单位资源，耗时t1。
- 配置2消耗c2单位资源，耗时t2。
所有任务的资源消耗之和不能超过C。
求最小总耗时。如果多个方案总耗时相同，选择资源消耗最少的方案。
"""
def num_12():
    n, C = map(int, input().split())
    tasks = []
    for _ in range(n):
        c1, t1, c2, t2 = map(int, input().split())
        tasks.append((c1, t1, c2, t2))


"""
有n张计算卡，编号为1～n。初始时，每张卡独自属于一个通信组。
需要依次处理q条操作：
- 1 u v：将卡u和卡v所在的两个组合并。如果已经在同一组，则不做任何改变。
- 2 u v：查询卡u和卡v是否在同一组，是则输出YES，否则输出NO。
全部操作结束后，输出剩余通信组的数量。
输入格式
第一行两个整数n q。
接下来q行，每行三个整数，表示一条操作。
输出格式
每条查询操作输出一行YES或NO。
最后一行输出通信组数量。
"""
def num_13():
    n, q = map(int, input().split())
    parent = list(range(n + 1))


    def find(u):
        if parent[u] !=u:
            parent[u] = find(parent[u])
        return parent[u]

    def union1(u,v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_u] = root_v

    def query2(u,v):
        return find(u) == find(v)

    for _ in range(q):
        op, u, v = map(int, input().split())
        if op == 1:
            union1(u, v)
        elif op == 2:
            if query2(u, v):
                print("YES")
            else:
                print("NO")

    count = 0
    for i in range(1, n + 1):
        if find(i) == i:
            count += 1
    print(count)

"""
注意力机制
"""

def scale_dot(q, k, v, dk):
    return softmax(q@k.T/np.sqrt(dk))@v

# 手写softmax（按行）
def softmax(mat):
    exp_mat = np.exp(mat)
    exp_sum = np.sum(exp_mat, axis=1, keepdims=True)
    return exp_mat/exp_sum


    
def num_14():
    X = np.array([
    [1, 2, 1, 2, 1, 2, 1, 2],
    [3, 4, 3, 4, 3, 4, 3, 4],
    [5, 6, 5, 6, 5, 6, 5, 6]
])

# 权重
    Wq = np.ones((8,8)) * 0.1
    Wk = np.ones((8,8)) * 0.2
    Wv = np.ones((8,8)) * 0.3
    Wo = np.ones((8,8)) * 0.5

    h = 4          # 头数
    d_model = 8    # 总维度
    dk = d_model // h # 每个头维度 = 2
    seq_len = X.shape[0]

    Q = X @Wq
    K = X@Wk
    V = X@Wv

    Q = Q.reshape(seq_len, h, dk).transpose(0,1)
    K = K.reshape(seq_len, h, dk).transpose(0,1)
    V = V.reshape(seq_len, h, dk).transpose(0,1)

    headout = []
    for i in range(h):
        q = Q[i]
        k = K[i]
        v = V[i]
        headi = scale_dot( q, k ,v ,dk
        )
        headout.append(headi)

    headout = np.stack(headout, axis=0)
    headout = headout.transpose(1,0,2)
    concat = headout.reshape(seq_len, d_model)




    out = concat @ Wo

    for row in out:
        print(" ".join(f"{val:.4f}" for val in row))

def num_15():
    X = np.array([
    [1, 2, 1, 2, 1, 2, 1, 2],
    [3, 4, 3, 4, 3, 4, 3, 4],
    [5, 6, 5, 6, 5, 6, 5, 6]
])

# 权重矩阵
    Wq = np.ones((8, 8)) * 0.1   # Q投影：8维输入，8维输出（4头×2维）
    Wk = np.ones((8, 4)) * 0.2   # K投影：8维输入，4维输出（2头×2维）
    Wv = np.ones((8, 4)) * 0.3   # V投影：8维输入，4维输出（2头×2维）
    Wo = np.ones((8, 8)) * 0.5   # 输出投影：8维输入，8维输出

    h = 4       # Q头总数
    h_kv = 2    # K/V头总数
    d_model = 8
    dk = d_model // h   # 单个头维度 = 2
    g = h // h_kv       # 每组包含的Q头数 = 2
    seq_len = X.shape[0]

    Q = X @ Wq
    K = X @ Wk
    V = X @ Wv

    Q = Q.reshape(seq_len, h, dk).transpose(1,0,2)
    K = K.reshape(seq_len, g, dk).transpose(1,0,2)
    V = V.reshape(seq_len, g, dk).transpose(1,0,2)

    headout = []
    for idx in range(h):
        group = idx//g
        k = K[group]
        v = V[group]

        att = scale_dot(Q[idx], k, v, dk)
        headout.append(att)

    concat = np.concatenate(headout, axis=1)

    out = concat @ Wo

    for raw in out:
        print(" ".join (f"{x:.4f}" for x in raw))

def num_16():
    """kmeans"""
    np.random.seed(42)
    X1 = np.random.normal(loc=[2, 2], scale=0.3, size=(50, 2))
    X2 = np.random.normal(loc=[5, 5], scale=0.3, size=(50, 2))
    X3 = np.random.normal(loc=[8, 2], scale=0.3, size=(50, 2))
    X = np.vstack([X1, X2, X3])
    k=3

    n_samples, n_feat = X.shape
    idx = np.random.choice(n_samples, size=k, replace=False)
    centers = X[idx].copy()


    for _ in range(iter):

        for i in range(n_samples):
            sample = X[i]
            min_dist = float("inf")
            labels = np.zeros(n_samples)
            cluster=0

            for c in range(k):
                dist = (X[i]-centers[c]) **2

                if dist<min_dist:
                    min_dist = dist
                    cluster = c
            labels[i]=cluster

        # 更新中心

        newcen = centers
        for c in range(k):
            group = X[labels==c]
            if len(group)>0:
                newcen[c] = group.mean(axis=0)


def num_17():
    n, d, k = map(int, input().split())
    x = []
    for _ in range(n):
        xi = list(map(float, input().split()))
        x.append(xi)

    x = np.array(x)

    cen = x[:k].copy
    labels= np.zeros(n)
    tol = 1e-4
    max_tir = 100


    for i in range(max_tir):
        #外循环
        for i in range(n):
            #遍历样本
            min_dist = float("inf")
            
            cluster = 0

            for c in range(k):
                # 计算距离

                for id_d in range(d):

                    dist += abs(x[i][id_d]-cen[c][id_d])

                if dist < min_dist:
                    min_dist = dist
                    cluster = c

            labels[i] = cluster

        #更新中心
        new_cen = cen.cpoy()
        for c in range(k):
            inertia = []

            group = x[labels==c]
            if len(group)>0:
                new_cen[c] = np.median(group, axis=0)
        cen = new_cen

        #计算inertia
        inertia_x = np.zeros(k)
        for c in range(k):
            group = x[labels==c]

            if len(group==0):
                inertia_x[c]=0.0
                continue

            total = 0
            for pts in group:
                disty = 0
            
                for j in range(d):
            
                    disty += np.abs(x[i,j]-cen[c,j])
                total += disty
            inertia_x[c]=total

    print(" ".join(f"{l}" for l in labels))
    for i in range(k):
        pts = new_cen[i]
        print(" ".join(f"{kk:.6f}" for kk in pts))

    print(" ".join(f"{x:.6f}" for x in inertia_x))


def dfs(current_layer, last_check, used_mem, current_cost):
    global ans
    # 剪枝显存超过预算
    if used_mem>maxmem:
        return

    # 处理边界
    if current_layer == N:
        final_cost = current_cost + cost[last_check][N]

        if final_cost< ans:
            ans = final_cost
        return

    # 选择1，不在currentlayer打检查点，往前走
    dfs = (current_layer+1, last_check, used_mem, current_cost)

    #选择2，在1-n-1打检查点
    if 1<=current_layer<=N-1:
        add_mem = memory[current_layer-1]

        if used_mem+add_mem <= maxmem:
            add_cost = cost[last_check][current_layer]
            dfs(current_layer + 1, current_layer, used_mem + add_mem, current_cost + add_cost)


def main_18():
    cost = [[0]*(N+1) for _ in range(N+1)]
    for c in range(N+1):
        for d in range(c+1, N+1):
            total = 0
            for k in range(c+1,d):
                total += forward_time[k-1] * (d-k)
            cost[c][d] = total

    ans = float("inf")







def main_19():
    N, MaxMem = map(int, input().split())
    forward_time = list(map(int, input().split()))
    memory = list(map(int, input().split()))

    cost = np.zeros((N+1, N+1))
    for c in range(N+1):
        for d in range(c+1, N+1):
            total = 0
            for k in range(c+1, d):
                total += forward_time[k-1]*(d-k)
            cost[c,d]=total

    def dfs19(current_layer, last_ckpt, used_mem, current_cost):
        # nonlocal ans
    # 剪枝
        if used_mem > MaxMem:
            return

    # 边界
        if current_layer == N:
            final_cost = cost[last_ckpt][N] + current_cost

            if final_cost <= ans:
                ans = final_cost
            return

    #不取，前进
        dfs19(current_layer+1, last_ckpt, used_mem, current_cost)

    #取，即打检查点
        if 1<= current_layer < N:
            addmem = memory[current_layer-1]
            if used_mem + addmem <= Maxmem:
                new_cost = current_cost + cost[last_ckpt, current_layer]
                dfs19(current_layer+1, current_layer, used_mem + addmem, new_cost)

    dfs19(1,0,0,0)
    print(ans)


def main_19():
    n,m = map(int, input().split())

    x_train = np.zeros((n,3))
    for i in range(n):
        row = list(map(int, input().split()))
        x_train[i] = row

    x_test = np.zeros(m)
    for i in range(m):
        x_test[i] = int(input())

    ui = x_train[:,2]
    mask = ui.astype(bool)

    x_feat = x_train[:,:2]
    x_feat_val = x_feat[mask]
    s = len(x_feat_val)

    if s>0:

        sx = x_feat_val[:,0].sum()
        sy = x_feat_val[:,1].sum()
        sxx = np.sum(x_feat_val[:,0]**2)
        sxy = np.sum(x_feat_val[:,0]*x_feat_val[:,1])

        D = s * sxx - sx**2

        if abs(D)>1e-12:
            w = (s * sxy - sx*sy)/D
            b = (sy - w*sx)/s
        else:
            w = 0
            b = sy/s

    else:
        w=0
        b=0

    y_test = w*x_test + b


    for j in range(len(y_test)):
        print(f"{y_test[j]:.4f}")





if __name__ == "__main__":
    main_18()

