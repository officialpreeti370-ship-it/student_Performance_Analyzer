import pandas as pd
import matplotlib.pyplot as plt


# ==============================
# 1. READ STUDENT DATA
# ==============================

df = pd.read_csv("student_data.csv")

subjects = [
    "Python",
    "Math",
    "DBMS",
    "Computer_Networks",
    "OS"
]


# ==============================
# 2. CALCULATE TOTAL & PERCENTAGE
# ==============================

df["Total"] = df[subjects].sum(axis=1)

df["Percentage"] = df["Total"] / 5


# ==============================
# 3. CALCULATE GRADE
# ==============================

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


df["Grade"] = df["Percentage"].apply(calculate_grade)


# ==============================
# 4. PASS / FAIL
# ==============================

df["Result"] = df["Percentage"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)


# ==============================
# 5. DISPLAY STUDENT RESULTS
# ==============================

print("\n")
print("=" * 55)
print("          STUDENT PERFORMANCE ANALYZER")
print("=" * 55)

print("\nSTUDENT RESULTS\n")

print(
    df[
        ["Name", "Total", "Percentage", "Grade", "Result"]
    ].to_string(index=False)
)


# ==============================
# 6. CLASS ANALYSIS
# ==============================

class_average = df["Percentage"].mean()

topper = df.loc[df["Percentage"].idxmax()]

lowest_student = df.loc[df["Percentage"].idxmin()]

print("\n")
print("=" * 55)
print("              CLASS ANALYSIS")
print("=" * 55)

print(f"\nTotal Students: {len(df)}")

print(f"Class Average: {class_average:.2f}%")

print(
    f"Topper: {topper['Name']} "
    f"- {topper['Percentage']:.2f}%"
)

print(
    f"Lowest Percentage: {lowest_student['Name']} "
    f"- {lowest_student['Percentage']:.2f}%"
)


# ==============================
# 7. TOP 3 STUDENTS
# ==============================

top_three = df.sort_values(
    by="Percentage",
    ascending=False
).head(3)

print("\n")
print("TOP 3 STUDENTS")
print("-" * 35)

for position, (_, student) in enumerate(
    top_three.iterrows(),
    start=1
):

    print(
        f"{position}. {student['Name']} "
        f"- {student['Percentage']:.2f}%"
    )


# ==============================
# 8. SUBJECT-WISE ANALYSIS
# ==============================

subject_average = df[subjects].mean()

print("\n")
print("=" * 55)
print("          SUBJECT-WISE ANALYSIS")
print("=" * 55)

for subject, average in subject_average.items():

    print(
        f"{subject}: {average:.2f}"
    )


best_subject = subject_average.idxmax()

lowest_subject = subject_average.idxmin()

print(
    f"\nBest Performing Subject: "
    f"{best_subject}"
)

print(
    f"Lowest Performing Subject: "
    f"{lowest_subject}"
)


# ==============================
# 9. STUDENT SEARCH
# ==============================

print("\n")
print("=" * 55)
print("              STUDENT SEARCH")
print("=" * 55)

search_name = input(
    "\nEnter student name to search: "
)

student = df[
    df["Name"].str.lower()
    == search_name.lower()
]


if not student.empty:

    student = student.iloc[0]

    print("\nStudent Found!")

    print(f"Name: {student['Name']}")
    print(f"Total Marks: {student['Total']}")
    print(f"Percentage: {student['Percentage']:.2f}%")
    print(f"Grade: {student['Grade']}")
    print(f"Result: {student['Result']}")

else:

    print("\nStudent not found.")


# ==============================
# 10. GRAPH 1 — STUDENT PERFORMANCE
# ==============================

plt.figure(figsize=(10, 5))

plt.bar(
    df["Name"],
    df["Percentage"]
)

plt.xlabel("Students")

plt.ylabel("Percentage")

plt.title(
    "Student Performance Analysis"
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "student_performance_chart.png"
)

plt.show()


# ==============================
# 11. GRAPH 2 — SUBJECT AVERAGE
# ==============================

plt.figure(figsize=(9, 5))

plt.bar(
    subject_average.index,
    subject_average.values
)

plt.xlabel("Subjects")

plt.ylabel("Average Marks")

plt.title(
    "Subject-Wise Performance"
)

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "subject_performance_chart.png"
)

plt.show()