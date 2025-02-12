import axios from 'axios';

// Connect fromt end to backend
const api   = axios.create({
    baseURL: 'http://localhost:8000',
})


export default api