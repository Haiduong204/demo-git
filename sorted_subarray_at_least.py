from collections import deque


def shortestSubarray(nums, k):
    # Bước 1: Khởi tạo deque và mảng tổng tiền tố
    n = len(nums)
    prefix = [0] * (n + 1)  # Mảng tổng tiền tố
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Bước 2: Deque lưu chỉ số và biến theo dõi độ dài nhỏ nhất
    dq = deque()
    min_len = float("inf")

    # Bước 3: Duyệt qua mảng tổng tiền tố
    # Bước 4: Tìm mảng con có tổng >= k
    for i in range(n + 1):

        while dq and prefix[i] - prefix[dq[0]] >= k:
            min_len = min(min_len, i - dq.popleft())

            # Bước 5: Duy trì deque theo thứ tự tăng dần của tổng tiền tố
        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()

            dq.append(i)

    # Bước 6: Trả về kết quả
    return min_len if min_len != float("inf") else -1


nums = [2, -1, 2]
k = 3
print(shortestSubarray(nums, k))
