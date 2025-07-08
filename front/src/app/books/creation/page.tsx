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
        <div className = "max-w-xl mx-auto px-4 py-8 text-white">
            <h1 className = "text-3xl font-bold mb-6 text-white"> Ajouter un nouveau livre</h1>
            <form onSubmit = {handleSubmit} className = "space-y-6">

                {/* Titre */}
                <div>
                    <label htmlFor = "title" className = "block text-sm font-medium text-gray-200"> Titre </label>
                    <input type = "text" id = "title" value = {title} onChange= {(e) => setTitle(e.target.value)} placeholder = "Ex: Le Grand Bleu" required className = "mt-1 block w-full rounded-md border border-gray-600 bg-gray-900 p-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"/>
                </div>

                {/* ISBN */}
                <div>
                    <label htmlFor="isbn" className = "block text-sm font-medium text-gray-200"> ISBN </label>
                    <input type = "text" id = "isbn" value = {isbn} onChange = {(e) => setIsbn(e.target.value)} placeholder = "Ex: 198-1234567890" className = "mt-1 block w-full rounded-md border border-gray-600 bg-gray-900 p-2 shadow-sm focus:border-indigo-500 focus: ring-indigo-500"/>
                </div>

                {/* Description */}
                <div>
                    <label htmlFor="description" className="block text-sm font-medium text-gray-200">
                    Description
                    </label>
                    <textarea id = "description" value = {description} onChange = {(e) => setDescription(e.target.value)} rows = {4} placeholder = "Ceci est une description totalement normale." className = "mt-1 block w-full rounded-md border border-gray-600 bg-gray-900 p-2 shadow-sm focus:border-indigo-500 focus: ring-indigo-500">
                    </textarea>
                </div>

                {/* Statut */}
                <div>
                  <label htmlFor="readingStatus" className="block text-sm font-medium text-gray-200">
                    Statut de lecture
                  </label>
                  <select id="readingStatus" value={readingStatus} onChange={(e) => setReadingStatus(e.target.value)} className="mt-1 block w-full rounded-md border border-gray-600 bg-gray-900 p-2 shadow-sm text-white focus:border-indigo-500 focus:ring-indigo-500">
                    <option value="à lire">À lire</option>
                    <option value="en cours">En cours</option>
                    <option value="lu">Lu</option>
                  </select>
                </div>

                {/* Favori */}
                <div className="flex items-center">
                  <input
                    type="checkbox"
                    id="isFavorite"
                    checked={isFavorite}
                    onChange={(e) => setIsFavorite(e.target.checked)}
                    className="h-4 w-4 rounded border-gray-600 text-indigo-500 focus:ring-indigo-500"
                  />
                  <label htmlFor="isFavorite" className="ml-2 text-sm text-gray-200">
                    Désigner en favori
                  </label>
                </div>

                {/* Bouton */}
                <div>
                  <button
                    type="submit"
                    className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded-md shadow"
                  >
                    Enregistrer
                  </button>
                </div>
            </form>
        </div>
    );
}