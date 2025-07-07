import {apiFetch} from "./api";

export const fetchImages = () => apiFetch("/images/");

export const fetchImage = (id) => apiFetch("/images/${id}")

export const createImage = (data) =>
    apiFetch("/images", {
        method: "POST",
        body: JSON.stringify(data),
    });

export const updateImage = (id) => 
        apiFetch("/images/${id}", {
        method: "PUT",
    });
    
export const deleteImage = (id) => 
        apiFetch("/images/${id}", {
        method: "DELETE",
    });