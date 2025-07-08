'use client'; // Indique que ce composant est exécuté côté navigateur (client)

// Importe les fonctions du service pour gérer les livres
import { fetchBooks, deleteBook } from "@/services/bookService";

// Importe SWR pour gérer la récupération des données
import useSWR from "swr";

// Importe Link pour la navigation entre les pages sans rechargement
import Link from "next/link";

// Importe useState pour gérer l’état de suppression
import { useState } from "react";

// Composant principal pour afficher la liste des livres
export default function BookListPage() {
  // SWR pour récupérer les livres depuis l'API + mutation en cas de mise à jour
  const { data: books, error, isLoading, mutate } = useSWR("books", fetchBooks);

  // État local pour suivre quel livre est en cours de suppression
  const [deletingId, setDeletingId] = useState<string | null>(null);

  // Fonction pour supprimer un livre avec confirmation
  const handleDelete = async (id: string) => {
    const confirm = window.confirm("Confirmer la suppression du livre ?");
    if (!confirm) return;

    setDeletingId(id);

    try {
      await deleteBook(id);
      mutate();
    } catch (err) {
      console.error("Erreur suppression :", err);
      alert("Impossible de supprimer ce livre.");
    } finally {
      setDeletingId(null);
    }
  };

  // Affiche un message si il y a une erreur
  if (error)
    return <p className = "text-red-500 px-4 py-8"> Erreur de chargement </p>;

  // Affiche un message si le chargement est en cours
  if (isLoading)
    return <p className = "animate-pulse px-4 py-8 text-gray-300"> Chargement... </p>;

  // Une fois les livres chargés, affichage principal
  return (
    <div className = "max-w-4xl mx-auto px-4 py-8 text-white">
      
      {/* Titre de la page */}
      <h1 className = "text-3xl font-bold mb-6"> Liste des livres </h1>

      {/* Bouton de création de livre */}
      <Link href = "/books/creation" className = "inline-block mb-6 bg-green-600 hover:bg-green-700 text-white font-medium px-4 py-2 rounded shadow">
        Ajouter un livre
      </Link>

      {/* Message si aucun livre n’est présent */}
      {books.length === 0 ? (
        <p className = "text-gray-400"> Aucun livre pour le moment. </p>
      ) : (
        <ul className = "grid gap-6 md:grid-cols-2">
          {books.map((book: any) => (
            <li key = {book.id} className = "border border-gray-700 rounded-lg bg-gray-900 p-4 shadow-md hover:border-indigo-500 transition">

              {/* En-tête : titre + Modifier + Supprimer */}
              <div className = "flex justify-between items-start">
                <div>
                  <Link href = {`/books/${book.id}`} className = "text-xl font-semibold text-indigo-300 hover:underline">
                    {book.title}
                  </Link>

                  {/* Statut de lecture */}
                  <p className = "text-sm text-gray-400 italic mt-1">
                    Statut : {book.reading_status}
                  </p>
                </div>

                {/* Modifier + Supprimer */}
                <div className = "flex flex-col items-end text-sm gap-1">
                  <Link href = {`/books/${book.id}/edit`} className = "text-indigo-400 hover:underline">
                    Modifier
                  </Link>

                  <button onClick = {() => handleDelete(book.id)} disabled = {deletingId === book.id} className = "text-red-500 hover:underline disabled:opacity-50">
                    Supprimer
                  </button>
                </div>
              </div>

              {/* Favori */}
              {book.is_favorite && (
                <span className = "inline-block text-yellow-500 text-sm mt-2"> ★ Favori </span>
              )}

              {/* ISBN */}
              <p className = "text-sm text-gray-300 mt-2">
                <strong> ISBN : </strong> {book.isbn || "—"}
              </p>

              {/* Description */}
              <p className = "text-sm text-gray-300 mt-1">
                {book.description || <em className = "text-gray-500"> Pas de description. </em>}
              </p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
