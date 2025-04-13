import React, { useEffect, useContext, useState } from 'react'
import { PaginationComponente } from '@/components/Pagination'
import FilmesServices from '@/services/FilmesServices'
import { Card, CardContent } from "@/components/ui/card"
import { StarRating } from '@/components/StarRating'

export function FilmesPage() {
    const [filmes, setFilmes] = useState({ filmes: [], total: 0 })
    const [currentPage, setCurrentPage] = useState(1)
    const [moviesPerPage] = useState(10)
    const [ratings, setRatings] = useState(0)

    const fetchFilmes = async () => {
        try {
            const response = await FilmesServices.getAll((currentPage - 1) * moviesPerPage, moviesPerPage)
            setFilmes(response)
        } catch (error) {
            console.error('Error fetching filmes:', error)
        }
    }

    useEffect(() => {
        const fetch = async () => {
            await fetchFilmes()
        }
        fetch()
    }, [currentPage, moviesPerPage])


    useEffect(() => {
        const fetch = async () => {
            await fetchFilmes()
        }
        fetch()
    }, [])

    const totalPages = Math.ceil(filmes.total / moviesPerPage)

    const handleRatingChange = (movieId, rating) => {
        setRatings((prevRatings) => ({
            ...prevRatings,
            [movieId]: rating,
        }));
    };

    useEffect(() => { console.log(ratings) }, [ratings])
    return (<>
        <div className="h-screen min-h-screen">
            {/* Header */}


            {/* Recommendations Section */}
            <main className="container mx-auto px-4 py-8">
                <h2 className="text-2xl font-semibold mb-6 text-slate-400">Filmes</h2>
                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                    {filmes?.filmes?.map((movie, idx) => (
                        <Card key={idx} className="rounded-lg text-black p-3">
                            <CardContent>
                                <div>
                                    {movie.MOVIEID} {movie.TITLE} {movie.YEAR}
                                </div>
                                <StarRating
                                    rating={ratings[movie.MOVIEID] || 0}
                                    onRatingChange={(rating) => handleRatingChange(movie.MOVIEID, rating)}
                                />
                            </CardContent>
                        </Card>
                    ))}
                </div>
            </main>
            <div className='text-black'>
                <PaginationComponente totalPages={totalPages} currentPage={currentPage} onPageChange={setCurrentPage} />
            </div>

            {/* Footer */}
        </div>
    </>)
}