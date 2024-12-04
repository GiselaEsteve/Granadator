def main():
    print("Aquest programa calcularà la teva nota final del curs basant-se en els teus exàmens i treballs.")
    
    notas = [
        {"nombre": "Parcial 1", "nota": 78, "pes": 10},
        {"nombre": "Parcial 2", "nota": 84, "pes": 10},
        {"nombre": "Final", "nota": 100, "pes": 30},
        {"nombre": "Treballs", "pes": 50, 
         "detall": [
            {"treball": "Treball 1", "nota": 14, "possibles": 15},
            {"treball": "Treball 2", "nota": 17, "possibles": 20},
            {"treball": "Treball 3", "nota": 19, "possibles": 25},
            {"seccions": 25, "possibles": 30}
         ]}
    ]
    
    midterm1_weighted = calculate_weighted_score(notas[0]["nota"], notas[0]["pes"])
    midterm2_weighted = calculate_weighted_score(notas[1]["nota"], notas[1]["pes"])
    final_exam_weighted = calculate_weighted_score(notas[2]["nota"], notas[2]["pes"])
    homework_weighted = calculate_homework_score(notas[3])
    
    final_grade = midterm1_weighted + midterm2_weighted + final_exam_weighted + homework_weighted
    
    print(f"\nLa teva nota final ponderada és: {round(final_grade, 1)}%")
    print(f"Has obtingut una qualificació de {assign_letter_grade(final_grade)}.")
    print_final_message(final_grade)

def calculate_weighted_score(score, weight):
    return (score / 100) * weight

def calculate_homework_score(homework_data):
    detall = homework_data["detall"]
    total_score = 0
    total_possible = 0
    
    for item in detall:
        if "seccions" in item:
            total_score += min(item["seccions"], 30)
            total_possible += item["possibles"]
        else:
            total_score += item["nota"]
            total_possible += item["possibles"]
    
    final_homework_score = min(total_score / total_possible, 1) * 100
    return calculate_weighted_score(final_homework_score, homework_data["pes"])

def assign_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def print_final_message(grade):
    if grade >= 90:
        print("Enhorabona! Has excel·lit al curs.")
    elif grade >= 80:
        print("Bon treball! Has fet una bona feina.")
    elif grade >= 70:
        print("Has aprovat, però sempre pots millorar.")
    elif grade >= 60:
        print("Has passat per poc. Considera estudiar més la propera vegada.")
    else:
        print("Lamentablement, no has aprovat. No et rendeixis!")

if __name__ == "__main__":
    main()
