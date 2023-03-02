import React, { useEffect, useState, useCallback } from 'react'; 'react-dom';
import axios from 'axios';
axios.defaults.withCredentials = true;
function ListPresentation() {
    const [bookList, setPresentationList] = useState([]);
    const fetchData = useCallback(async () => {
    try {
        const apiURL = "http://127.0.0.1:8000/api/presentation_app/presentation/list";
        const response = await axios.get(apiURL, { withCredentials: true });
        setPresentationList(response.data);
    } catch (error) {
        console.log(error);
    }
}, []);

useEffect(() => {
    fetchData();
}, [fetchData]);

return (
    <div className="main-section">
        <h1>All Presentation Model</h1>
        <div className="book-list">
            {bookList.map((book, index) => (
                <ul key={index}>
                    <li>Title: {book.title}</li>
                    <li>Text: {book.text}</li>
                    <li>Result: {book.result}</li>
                </ul>
            ))}
        </div>
    </div>
);
}

export default ListPresentation;

