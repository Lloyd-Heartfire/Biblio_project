import {apiFetch} from "./api";

export const fetchAuthors = () => apiFetch(`/authors/`);

export const fetchAuthor = (id) => apiFetch(`/authors/${id}`)

export const createAuthor = (data) =>
    apiFetch(`/authors`, {
        method: "POST",
        body: JSON.stringify(data),
    });

    export const updateAuthor = (id, data) => 
        apiFetch(`/authors/${id}`, {
        method: "PUT",
        body: JSON.stringify(data),
    });
    
    export const deleteAuthor = (id) => 
        apiFetch(`/authors/${id}`, {
        method: "DELETE",
    });