def main():
    input_file_name = "C:/temp/work/points.txt"
    grades_file_name = "C:/temp/work/grades.txt"
    error_file_name = "C:/temp/work/error.txt"

    records_read = 0
    good_records = 0
    error_records = 0

    count_A = count_B = count_C = count_D = count_F = 0

    try:
        input_file = open(input_file_name, "r")
        grades_file = open(grades_file_name, "w")
        error_file = open(error_file_name, "w")
    except FileNotFoundError:
        print("Error: input file not found.")
        return

    line = input_file.readline()
    while line != "":
        records_read += 1
        line = line.strip()

        if line == "":
            line = input_file.readline()
            continue

        fields = line.split(",")
        error_message = None

        if len(fields) != 3:
            error_message = "Invalid number of fields"
            error_file.write(line + "," + error_message + "\n")
            error_records += 1
            line = input_file.readline()
            continue

        id_number = fields[0].strip()
        name = fields[1].strip()
        points_str = fields[2].strip()

        try:
            points = float(points_str)
        except ValueError:
            error_message = "Points must be numeric"

        if error_message is None:
            if points < 0:
                error_message = "Points cannot be negative"
            elif points > 1000:
                error_message = "Points must be between 0 and 1000"
            else:
                if 900 <= points <= 1000:
                    grade = "A"
                    count_A += 1
                elif 800 <= points <= 899:
                    grade = "B"
                    count_B += 1
                elif 700 <= points <= 799:
                    grade = "C"
                    count_C += 1
                elif 600 <= points <= 699:
                    grade = "D"
                    count_D += 1
                else:
                    grade = "F"
                    count_F += 1

                grades_file.write(f"{id_number},{name},{points_str},{grade}\n")
                good_records += 1

        if error_message:
            error_file.write(f"{id_number},{name},{points_str},{error_message}\n")
            error_records += 1

        line = input_file.readline()

    input_file.close()
    grades_file.close()
    error_file.close()

    print("Records read:", records_read)
    print("Number of A's:", count_A)
    print("Number of B's:", count_B)
    print("Number of C's:", count_C)
    print("Number of D's:", count_D)
    print("Number of F's:", count_F)
    print("Good records:", good_records)
    print("Error records:", error_records)

main()
