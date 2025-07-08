'use client'; // Indique que ce composant est exécuté côté client (navigateur)

// Importe la fonction qui va chercher les livres dans le backend
import { fetchBooks } from "@/services/bookService";

// Importe SWR : bibliothèque qui aide à gérer le chargement de données
import useSWR from "swr";

// Importe Link : permet de créer des liens entre les pages sans rechargement
import Link from "next/link";

// Composant principal pour afficher la liste des livres
export default function BookListPage() {

  // Utilise SWR pour récupérer les livres depuis l'API
  const { data: books, error, isLoading } = useSWR("books", fetchBooks);

  // Si une erreur se produit pendant le chargement, affiche un message
  if (error)
    return <p className = "text-red-500 px-4 py-8"> Erreur de chargement </p>;

  // Si les livres sont en cours de chargement, affiche un message
  if (isLoading)
    return <p className = "animate-pulse px-4 py-8 text-gray-300"> Chargement... </p>;

  // Une fois les livres chargés, affiche le contenu principal
  return (
    <div className = "max-w-4xl mx-auto px-4 py-8 text-white">

      {/* Titre de la page */}
      <h1 className = "text-3xl font-bold mb-6"> Liste des livres </h1>

      {/* Bouton vers la page de création de livre */}
      <Link
        href = "/books/creation"
        className = "inline-block mb-6 bg-blue-600 hover:bg-blue-700 text-white font-medium px-4 py-2 rounded shadow"
      >
        + Ajouter un livre
      </Link>

      {/* Si aucun livre n’a été créé */}
      {books.length === 0 ? (
        <p className = "text-gray-400"> Aucun livre pour le moment. </p>
      ) : (

        // Sinon, affiche chaque livre dans une carte
        <ul className = "grid gap-6 md:grid-cols-2">
          {books.map((book: any) => (
            <li
              key = {book.id_book}
              className = "border border-gray-700 rounded-lg bg-gray-900 p-4 shadow-md hover:border-indigo-500 transition"
            >

              {/* En-tête de la carte : titre + lien "modifier" */}
              <div className = "flex justify-between items-start">
                <div>

                  {/* Titre du livre, cliquer pour voir les détails */}
                  <Link
                    href = {`/books/${book.id_book}`}
                    className = "text-xl font-semibold text-indigo-300 hover:underline"
                  >
                    {book.title}
                  </Link>

                  {/* Statut de lecture */}
                  <p className = "text-sm text-gray-400 italic mt-1">
                    Statut : {book.reading_status}
                  </p>
                </div>

                {/* Lien pour modifier le livre */}
                <Link
                  href = {`/books/${book.id_book}/edit`}
                  className = "text-sm text-indigo-400 hover:underline"
                >
                  Modifier
                </Link>
              </div>

              {/* Si le livre est marqué comme favori */}
              {book.is_favorite && (
                <span className = "inline-block text-yellow-500 text-sm mt-2"> ★ Favori </span>
              )}

              {/* Affichage de l’ISBN */}
              <p className = "text-sm text-gray-300 mt-2">
                <strong> ISBN : </strong> {book.isbn || "—"}
              </p>

              {/* Affichage de la description ou texte par défaut */}
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