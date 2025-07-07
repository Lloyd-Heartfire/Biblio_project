'use client';

import { fetchBooks } from "@/services/bookService";
import useSWR from "swr";
import Link from "next/link";

export default function BookListPage() {
    const {data: books, error, isLoading} = useSWR("books", fetchBooks);

    if (error)
        return <p className = "text-red-500"> Erreur de chargement </p>;
    if (isLoading)
        return <p className = "animate-pulse"> Chargement... </p>
    
    return (
        <div className = "max-w-3xl mx-auto px-4 py-8">
            <h1 className = "text-2xl font-bold mb-4"> Liste des livres </h1>

            <Link href = "/books/creation" className = "bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded mb-6 inline-block"> Ajouter un livre </Link>

            <ul className = "space-y-4">
                {books.map((book: any) => (
                    <li key = {book.id_book} className = "border p-4 rounded shadow-sm flex justify-between items-center">
                        <div>
                            <Link href = {"/books/${book.id_book}"} className = "text-lg font-semibold hover:underline"> {book.title} </Link>
                            <p className = "text-sm text-blue-600"> Status : {book.reading_status} </p>
                        </div>
                        <Link href = {"/books/${book.id_book}/edit"} className = "text-sm text-blue-600 hover:underline"> Modifier </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}