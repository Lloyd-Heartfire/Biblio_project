'use client';

import { getBookById} from "@/services/bookService";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";

export default function BookDetailPage() {
    const { id} = useParams();
    const [book, setBook] = useState<any>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchBook = async () => {
            try {
                const data = await getBookById(id);
                setBook(data);
            } catch (error) {
                console.error("Erreur lors du chargement du livre :", error);
            } finally {
                setLoading(false);
            }
        };

        fetchBook();
    }, [id]);

    if (loading)
        return <p className = "text-gray-300 px-4 py-8 animate-pulse"> Chargement... </p>;

    if (!book)
        return <p className = "text-red-500 px-4 py-8"> Livre introuvable </p>;

    return (
        <div className = "max-w-2xl mx-auto px-4 py-8 text-white">
            <h1 className = "text-3xl font-bold mb-2"> {book.title} </h1>


            <p className = "text-sm text-gray-300 mb-2">
                <strong> ISBN :</strong> {book.isbn || "-"}
            </p>

            <p className = "text-sm text-gray-300">
                <strong> Description :</strong><br />
                {book.description || <em className = "text-gray-500"> Pas de description. </em>}
            </p>

            <p className = "text-sm text-gray-400 italic mb-4"> Statut : {book.reading_status}</p>

            {book.is_favorite && (
                <span className = "inline-block text-yellow-500 text-sm mb-4"> Favori </span>
            )}
            
            <p className = "mt-8">
                <Link href = "/books/" className = "text-green-500 hover:underline"> Retour à la liste </Link>
            </p>
        </div>
    )
}