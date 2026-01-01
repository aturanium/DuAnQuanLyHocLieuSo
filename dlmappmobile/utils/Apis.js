import axios from "axios"

const BASE_URL = 'https://lethanhtruong.pythonanywhere.com/'

export const endpoints = {
    'categories': '/categories/',
    'lessons': '/lessons/',
    'courses': '/courses/',
    'materials': '/materials/',
    'topics': '/topics/',
    'users': '/users/',
    'comments': '/comments/',
    'questions': '/questions/',
    'answers': '/answers/',
    'likes': '/likes/',
    'notes': '/notes/',
}

export default axios.create({
    baseURL: BASE_URL
});