// 3-read_file_async
\\
async function countStudents(path) {
  try {
    const data = await FileSystem.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = line.slice(1);

    const fields = {};

    students.forEach((student) => {
      const [firstName, , , field] = student.split(',');

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    console.log(`Number of students: ${students.length}`);
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }

    return Promise.resolve();
  } catch (error) {
    return Promise.reject(new Error('Cannot load the database'));
  }
}

module.exports = countStudents;
