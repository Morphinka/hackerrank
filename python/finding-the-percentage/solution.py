if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    final = sum(student_marks[query_name])/3.00
    format_final = "{:.2f}".format(final)
    print(format_final)
