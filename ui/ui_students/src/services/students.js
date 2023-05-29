const API_STUDENTS_URL = "http://localhost:8000/"
export const fetchStudents = () => 
    fetch(API_STUDENTS_URL).then((res) => res.json());
export const createStudent = ({firstName, lastName}) =>
    fetch(API_STUDENTS_URL, {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringlify({
            "first_name": firstName,
            "last_name": lastName,
        }),
    }).then((res)=> res.jeson());
