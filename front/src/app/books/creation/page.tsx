'use client'

import { createBook } from '@/services/bookService';
import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function NewBookPage() {
    const [title, setTitle] = useState('');
    const [readingStatus, setReadingStatus] = useState('à lire')
    const [isbn, setIsbn] = useState('');
    const [description, setDescription] = useState('');
    const [isFavorite, setIsFavorite] = useState(false);
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        try {
            await createBook({
                title,
                reading_status: readingStatus,
                isbn,
                description,
                is_favorite: isFavorite,
            });
            router.push('/books/');
        } catch (error) {
            console.error("Erreur lors de la création :", error);
            alert("Une erreur est survenue !");
        }
    };

    return (
        <div className = "max-w-lg mx-auto px-4 py-8">
            <h1 className = "text-2xl font-bold mb-4"> Ajouter un nouveau livre</h1>
            <form onSubmit = {handleSubmit} className = "space-y-4">
                <div>
                    <label className = "block text-sm font-medium text-gray-700"> Titre </label>
                    <input type = "text" value = {title} onChange= {(e) => setTitle(e.target.value)} required className = "mt-1 block w-full border border-gray-300 rounded px-3 py-2"/>
                </div>

                <div>
                    <label className = "block text-sm font-medium text-gray-700"> Statut </label>
                    <select value = {readingStatus} onChange = {(e) => setReadingStatus(e.target.value)} className = "mt-1 block w-full border border-gray-300 rounded px-3 py-2">
                        <option value = "à lire"> À lire </option>
                        <option value = "en cours"> En cours </option>
                        <option value = "lu"> Lu </option>
                    </select>
                </div>

                <button type = "submit" className = "bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded"> Enregistrer </button>
            </form>
        </div>
    );
}