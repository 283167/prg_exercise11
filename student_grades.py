from sorted import random_numbers

class StudentsGrades:
    def __init__(self, scores): #vraci bodove hodnoceni
        self.scores = scores

    def get_by_index(self, index): #vraci body na konkretnim indexu
        return self.scores[index]

    def count(self): #vraci delku seznamu znamek studentu
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)
        if score in range(90, 100 + 1):
            return "A"
        elif score in range(80, 89 + 1):
            return "B"
        elif score in range(70, 79 + 1):
            return "C"
        elif score in range(60, 69 + 1):
            return "D"
        elif score in range(50, 59 + 1):
            return "E"
        elif score in range(0, 49 + 1):
            return "F"

    def find(self, searched_score):
        score_indexes = []
        for i, score in enumerate(self.scores):
            if score == searched_score:
                score_indexes.append(i)
        return score_indexes

    def get_sorted(self):
        scores = self.scores.copy()
        for i in range(len(scores)):
            swapped = False
            for x in range(1, len(scores) - i):
                if scores[x - 1] > scores[x]:
                    scores[x - 1], scores[x] = scores[x], scores[x - 1]
                    swapped = True
            if swapped == False:
                return scores
        return scores



if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)

    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []

    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

    print(results.count())
    for i, item in enumerate(results.scores):
        print(f"Student {i}: {item} points - {results.get_grade(i)}")
    print(results.find(100))
    print(results.get_sorted())
    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())