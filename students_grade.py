class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, value):
        result = []
        for i in range(len(self.scores)):
            if self.scores[i] == value:
                result.append(i)
        return result

    def get_sorted(self):
        scores = list(self.scores)
        for i in range(len(scores)):
            for val in range(len(scores) - 1):
                if scores[val] > scores[val + 1]:
                    scores[val], scores[val + 1] = scores[val + 1], scores[val]
        return scores




results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    stud = results.count()
    print(stud)
    for i,student in enumerate(results.scores, start=0):
        print(f"Student {i}: {student} points - {results.get_grade(i)} ")
    print(results.find(100))
    print(results.get_sorted())

    from sorting import random_numbers

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())









"""""    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.get_grade(-4))
    print(results.find(73))
    print(results.get_sorted())"""
if __name__ == "__main__":
    main()