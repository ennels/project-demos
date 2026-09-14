import statistics as s
data = [[64, 0, 0, 52, 69, 46, 58, 67, 0, 55],[0, 37, 53, 71, 0, 60, 72, 75, 43, 0],[0, 61, 49, 58, 0, 73, 71, 75, 41, 66],[43, 0, 71, 29, 0, 74, 72, 47, 0, 62],[67, 64, 0, 0, 61, 42, 70, 0, 59, 30],[0, 72, 69, 67, 0, 41, 62, 0, 48, 59],[50, 74, 69, 0, 42, 0, 38, 0, 73, 61],[0, 0, 59, 64, 31, 48, 62, 0, 53, 46],[57, 0, 68, 73, 59, 75, 0, 27, 62, 0],[35, 54, 0, 0, 29, 62, 75, 71, 0, 48]]
for i, row in enumerate(data):
    data[data.index(row)] = [round(s.mean(num for num in row if num != 0), 1) if item == 0 else item for item in row]
    print(f"{data[i]}\t\t{round(s.mean(num for num in row if num != 0), 1)}")