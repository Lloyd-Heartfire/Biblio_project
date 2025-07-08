'use client';

import { getBookById, updateBook } from "@/services/bookService";
import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function EditBookPage() {
    // Récupère l'ID du livre dans l'URL
    const { id } = useParams();
    const router = useRouter();

    // états pour stocker les données du livre à modifier
    const [title, setTitle] = useState('');
    const [readingStatus, setReadingStatus] = useState('à lire');
    const [isbn, setIsbn] = useState('');
    const [description, setDescription] = useState('');
    const [isFavorite, setIsFavorite] = useState(false);
    const [loading, setLoading] = useState(true);

    // Pour chercher les infos du livre au chargement
    useEffect(() => {
    const fetchBook = async () => {
      try {
        const book = await getBookById(id);
        setTitle(book.title);
        setReadingStatus(book.reading_status);
        setIsbn(book.isbn);
        setDescription(book.description);
        setIsFavorite(book.is_favorite);
      } catch (error) {
        console.error("Erreur lors du chargement :", error);
        alert("Livre introuvable !");
      } finally {
        setLoading(false);
      }
    };

    fetchBook();
  }, [id]);

  // Fonction que l'on appelle à la soumission du formulaire
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
        await updateBook(id, {
            title,
            reading_status: readingStatus,
            isbn,
            description,
            is_favorite: isFavorite,
        });

        // Redirige vers la page des détails du livre
        router.push(`/books/${id}`);
    } catch (error) {
        console.error("Erreur lors de la modification :", error);
        alert("Impossible de modifier le livre.");
    }
  };

  if (loading)
    return <p className = "text-gray-300 px-4 py-8 animate-pulse"> Chargement... </p>;

  return (
    <div className = "max-w-xl mx-auto px-4 py-8 text-white">
        <h1 className = "text-3xl font-bold mb-6"> Modifier le livre </h1>

        <form onSubmit = {handleSubmit} className = "space-y-6">

        {/* Titre */}
        <div>
            <label className = "block text-sm font-medium text-gray-200"> Titre </label>
            <input type = "text" value = {title} onChange = {(e) => setTitle(e.target.value)} required className = "mt-1 block w-full rounded-md border border-gray-600 bg-gray-900 p-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"/>
        </div>

        {/* ISBN */}
        <div>
            <label className = "block text-sm font-medium text-gray-200"> ISBN </label>
            <input type = "text" value = {isbn} onChange = {(e) => setIsbn(e.target.value)} className = "mt-1 block w-full rounded-md border border-gray-600 bg-gray-900 p-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"/>
        </div>

        {/* Description */}
        <div>
            <label className = "block text-sm font-medium text-gray-200"> Description </label>
            <textarea value = {description} onChange = {(e) => setDescription(e.target.value)} className = "mt-1 block w-full rounded-md border border-gray-600 bg-gray-900 p-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"/>
        </div>

        {/* Statut */}
        <div>
            <label className = "block text-sm font-medium text-gray-200"> Statut de lecture </label>
            <select value = {readingStatus} onChange = {(e) => setReadingStatus(e.target.value)} className = "mt-1 block w-full rounded-md border border-gray-600 bg-gray-900 p-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
            <option value = "à lire"> À lire </option>
            <option value = "en cours"> En cours </option>
            <option value = "lu"> Lu </option>
            </select>
        </div>

        {/* Favori */}
        <div className = "flex items-center">
            <input type = "checkbox" checked = {isFavorite} onChange= {(e) => setIsFavorite(e.target.checked)} className = "h-4 w-4 rounded border-gray-600 text-indigo-500 focus:ring-indigo-500"/>
            <label className = "ml-2 text-sm text-gray-200"> Désigner en favori </label>
        </div>

        {/* Bouton Enregistrer */}
        <button type = "submit" className = "w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded shadow">
            Enregistrer
        </button>
        </form>
    </div>
  );
}