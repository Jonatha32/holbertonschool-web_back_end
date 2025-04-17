function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students) || !Array.isArray(newGrades)) {
    return [];
  }

  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const GradObj = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: GradObj ? GradObj.grade : 'N/A',
      };
    });
}

export default updateStudentGradeByCity;
