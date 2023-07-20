def longest_common_subsequence(s1, s2):
    # Function to find the length of the longest common subsequence of two strings
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the longest common subsequence
    lcs = []
    i, j = n, m
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()
    return "".join(lcs)

def main():
    # Challenge: Find the longest common subsequence of two strings
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    lcs = longest_common_subsequence(str1, str2)
    print(f"Longest Common Subsequence: {lcs}")

if __name__ == "__main__":
    main()
