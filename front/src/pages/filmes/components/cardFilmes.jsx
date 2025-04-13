import React, { useEffect, useState, useContext } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Loader2 } from 'lucide-react';
import FilmesServices from '@/services/FilmesServices';
import { StarRating } from '@/components/StarRating'
import { AuthContext } from '@/AuthContext';

import RatingsServices from '@/services/RatingsServices';

export function CardFilmes({ idFilme, nota, onChangeNota, titulo }) {
    const { user } = useContext(AuthContext)
    const [filme, setFilme] = useState({});
    const [loading, setLoading] = useState(true);
    const [ratings, setRatings] = useState(nota || 0)
    const [existingRating, setExistingRating] = useState(null)
    useEffect(() => {
        const fetchFilme = async () => {
            try {
                if (idFilme) {

                    const response = await FilmesServices.getById(idFilme);
                    const existingRating = await RatingsServices.getRatingByUserIdAndMovieId(user.id, idFilme);
                    setExistingRating(existingRating)
                    setFilme(response);
                }
                setLoading(false);
            } catch (error) {
                console.error('Error fetching filme:', error);
                setLoading(false);
            }
        };

        fetchFilme();
    }, [idFilme, ratings]);

    const rating = async () => {
        try {
            // Verificar se já existe uma nota para o filme
            const existingRating = await RatingsServices.getRatingByUserIdAndMovieId(user.id, filme.MOVIEID);
            const nota = {
                MOVIEID: filme.MOVIEID,
                USERID: user.id,
                RATING: ratings.rating, // Nota selecionada
            };
            onChangeNota(ratings.rating);

            if (existingRating.RATING !== null) {
                // Atualizar a nota existente
                await RatingsServices.updateRating(nota);
            } else {
                // Inserir uma nova nota
                await RatingsServices.createRating(nota);
            }
            window.location.reload(); // Recarregar a página após enviar a nota

        } catch (error) {
            console.error('Erro ao enviar nota:', error);
        }
    };

    const handleRatingChange = (movieId, rating) => {
        setRatings({
            movieId,
            rating,
        });

    };

    useEffect(() => {
        if (ratings?.rating) {
            rating()
        }
    }, [ratings])

    return (<>
        <Card>
            {loading &&
                <div className="flex items-center justify-center h-full">
                    <Loader2 className="animate-spin" />
                </div>
            }
            {!loading && <>
                <Card className="rounded-lg text-black p-3">
                    <CardContent>
                        <div>
                            {filme.MOVIEID} {filme.TITLE} {filme.YEAR}
                        </div>
                        <StarRating
                            rating={nota || existingRating?.RATING || 0}
                            onRatingChange={(rating) => handleRatingChange(filme.MOVIEID, rating)}
                        />
                    </CardContent>
                </Card>
            </>
            }
        </Card>
    </>)

}