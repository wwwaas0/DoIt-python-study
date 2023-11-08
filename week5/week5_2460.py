num = 0  
result = [num := num - down + up for down, up in [map(int, input().split()) for _ in range(10)]]
print(max(result))