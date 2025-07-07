import {apiFetch} from "./api";

export const fetchUsers = () => apiFetch("/users/");

export const fetchUser = (id) => apiFetch("/users/${id}")

export const createUser = (data) =>
    apiFetch("/users", {
        method: "POST",
        body: JSON.stringify(data),
    });

export const updateUser = (id) => 
        apiFetch("/users/${id}", {
        method: "PUT",
    });
    
export const deleteUser = (id) => 
        apiFetch("/users/${id}", {
        method: "DELETE",
    });