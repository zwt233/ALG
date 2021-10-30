### **Problem Definition**:

Our problem is quite similar to the classical NP-hard problem: Maximum Coverage. In the Maximum Coverage problem, we are given $n$ sets $M=\{M_1,...,M_n\}$, each of which is a subset of a common set $U$. Given a selection budget $b_{total}$, the goal is to select $b_{total}$ out of the $n$ sets, $S=\{S_1,...,S_{b_{total}}\}\subset M$, which maximizes $|\bigcup S|$, the carnality of the union of the selected $b_{total}$ sets. 

We further define a specific Maximum Coverage problem by adding additional constraints to the classical one as follows:
1) We separate the $n$ sets for selection into $k$  *disjoint* partitions, and we have a selection budget $b_i$ for the $i$-th group such that $\sum_{i=1}^{k}b_i=b_{total}$, which means we can only select $b_i$ sets from the $i$-th group; 

2) We also assign a weight $e_i$ to each element, and the optimization goal changes to maximize the sum of weights in the union of the selected $b_{total}$ sets.

This specific Maximum Coverage problem is also NP-hard because, with a polynomial algorithm of this problem, we can set $k$ and each weight $e_i$ to 1, and the budget of this unique group to $b_{total}$ so that the classical Maximum Coverage problem can be solved in polynomial time. This reduction proves the NP-hardness of this specific Maximum Coverage problem. 

Note that our ERF selection during each node selection iteration is also a special case of this specific problem. We describe relation between ERF selection with the specific Maximum Coverage problem as follows: 1) Suppose that we have the labeled and unlabeled node set $\mathcal{V_l}$ and $\mathcal{V_u}$ before selection. We consruct the common set $U=\mathcal{V_u}$. Then we construct $\\$ $|\mathcal{V}_u|$ subsets $M=\{M_1,...,M_{|\mathcal{V}_u|}\}$, in which $M_i=RF(v_i)-RF(\mathcal{V}_l) \subset \mathcal{V}_u$ for each node $v_i \in \mathcal{V_u}$; 2) Each node $v_i$ is assigned with an effectiveness score as its weight; 3) The budget $b_{total}$ is set to the selection budget $b$ for each iteration mentioned in Algorithm 2 and $b_i$ for each cluster is set to $b_{total}/k$.

### **Theorem**: 

During each node selection iteration, our greedy strategy returns a 1/2-approximate solution to the optimum for ERF maximization with the cluster constraint.

### **Proof**:
We prove this theorem on the specific Maximum Coverage problem defined above. First we clarify some notations. Let $M$ be $\{M_1,...,M_n\}$, the universal set of the sets to be selected. The partition of $M$ can be represented by $k$ subsets of $M$, $P_1,...,P_k$ such that $\bigcup_{i=1}^kP_i=M$, and $P_i \cap P_j=\varnothing$, for $\forall i \neq j$, $i,j \in \{1,...,k\}$. And we denote the sum of weights in set $A$ as $Sum(A)$. Our goal is to find a subset $S \subset M$, under the constraint that $|S \cap P_i|=b_i$, for $i \in \{1,...,k\}$, and $Sum(\bigcup S)$ is the greatest.

Suppose the optimal solution is $O_0=\{O_{0,1},...O_{0,b_{total}}\}$, and $ Sum(\bigcup O_0)=T$. Our greedy solution is $G_0=\{G_{0,1},...G_{0,b_{total}}\}$, and  $Sum(\bigcup G_0)=T_{greedy}$. We aim to prove $T \leq 2 T_{greedy}$. Since the order of $O_{0,1},...O_{0,b_{total}}$ can be changed at will, we suppose that each $O_{0,i}$ and $G_{0,i}$ belong to the same partition. 

We obtain $O_i$ and $G_i$ iteratively as follows. In the $i$-th iteration, we calculate $G_{i,j}=G_{i-1,j}-G_{i-1,i}$, for $\forall j \in \{1,...,b_{total}\}$.  And we calculate $O_{i,j}=O_{i-1,j}-G_{i-1,i}$, for $\forall j \neq i, j \in \{1,...,b_{total}\}$, and $O_{i,i}=\varnothing$. 
After $b_{total}$ iterations, it's obvious that both $O_{b_{total}}$ and $G_{b_{total}}$ become $\{ \varnothing,...,\varnothing \}$. In addition, since we choose sets greedily, $Sum(G_{i-1,i}) \geq Sum(O_{i-1,i})$. Then we have:
$$
Sum(\bigcup G_{i-1})-Sum(\bigcup G_i)=Sum(G_{i-1,i}),
$$
and
$$
\begin{aligned}
Sum(\bigcup O_{i-1})-Sum(\bigcup O_i)&=Sum(\bigcup O_{i-1})-Sum(\bigcup O_{i-1}-O_{i-1,i}-G_{i-1,i})\\
        &=Sum(O_{i-1,i})+Sum((\bigcup O_{i-1}-O_{i-1,i})\cap G_{i-1,i})\\
        &\leq Sum(O_{i-1,i})+Sum(G_{i-1,i})\\
        &\leq 2Sum(G_{i-1,i}).
\end{aligned}
$$
Based on the above equations, we have:
$$
\begin{aligned}
        T&=Sum(\bigcup O_0)-Sum(\bigcup O_{b_{total}})\\
        &=\sum_{i=1}^{b_{total}}Sum(\bigcup O_{i-1})-Sum(\bigcup O_{i})\\
        &\leq 2\sum_{i=1}^{b_{total}}Sum(\bigcup G_{i-1})-Sum(\bigcup G_{i})\\
        &=2(Sum(\bigcup G_0)-Sum(\bigcup G_{b_{total}}))\\
        &=2T_{greedy}.
    \end{aligned}
$$
This $1/2$ bound is also tight considering the following example:
Suppose that $U$ is the common set with $2r-1$ elements and each element has the weight of 1. Its subsets are $M_1=\{v_1,v_2,...,v_r\}$, $M_2=\{v_{r+1},v_{r+2},...,v_{2r-1}\}$, $M_3=\{v_1,v_2,...,v_{r-1}\}$. The two partitions are $P_1=\{M_1,M_2\},P_2=\{M_3\}$, and the budget for each partition $ b_1 = b_2 = 1$. The optimal solution is $\{M_2,M_3\}$, which collects a total weight of $2r-1$, while the greedy solution is $\{M_1,M_3\}$, which only collects a total weight of $r$. When $r \to \infty$, it shows that $1/2$ bound is indeed tight. 







