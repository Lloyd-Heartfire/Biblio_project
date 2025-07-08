// Fonction pour appeler une API REST
export async function apiFetch(path, options = {}) {

    // Concatène l’URL de base (env) avec le chemin donné
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}${path}`, {

        // Ajoute les headers pour dire qu’on envoie du JSON
        headers: { "Content-Type": "application/json" },
        ...options,
    });

    // Si la réponse n’est pas OK (ex. 404, 500), ça renvoie un message d'erreur
    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        const message = err.detal || err.message || JSON.stringify(err) || res.statusText;
        throw new Error(message);
    }

    // Si tout est OK, on retourne les données JSON
    return res.json();
}