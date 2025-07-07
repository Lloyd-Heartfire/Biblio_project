// Importation de la fonction apiFetch définie dans un autre fichier
import {apiFetch} from "./api";

// Fonction permettant de récupérer tous les livres (GET)
export const fetchBooks = () => apiFetch(`/books/`);

// Fonction permettant de récupérer un livre (GET)
export const fetchBook = (id) => apiFetch(`/books/${id}`);

// Fonction créant un nouvel livre (POST)
export const createBook = (data) =>
    apiFetch(`/books/`, {
        method: "POST",
        body: JSON.stringify(data),
    });

// Fonction permettant de modifier un livre (PUT)
export const updateBook = (id, data) => 
    apiFetch(`/books/${id}`, {
        method: "PUT",
        body: JSON.stringify(data),
    });
    
// Fonction permettant de supprimer un livre (DELETE)
export const deleteBook = (id) => 
    apiFetch(`/books/${id}`, {
        method: "DELETE",
    });