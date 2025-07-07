import {apiFetch} from "./api";

export const fetchSeries = () => apiFetch(`/series/`);

export const fetchSerie = (id) => apiFetch(`/series/${id}`)

export const createSerie = (data) =>
    apiFetch(`/series`, {
        method: "POST",
        body: JSON.stringify(data),
    });

export const updateSerie = (id, data) => 
    apiFetch(`/series/${id}`, {
        method: "PUT",
        body: JSON.stringify(data),
    });
    
export const deleteSerie = (id) => 
    apiFetch(`/series/${id}`, {
        method: "DELETE",
    });