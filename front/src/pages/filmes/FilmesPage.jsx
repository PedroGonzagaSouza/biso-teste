import React, { useEffect, useContext, useState } from 'react'
import { PaginationComponente } from '@/components/Pagination'
import FilmesServices from '@/services/FilmesServices'
import { CardFilmes } from './components/cardFilmes'
import { Input } from '@/components/ui/input'
export function FilmesPage() {
    const [filmes, setFilmes] = useState({ filmes: [], total: 0 })
    const [currentPage, setCurrentPage] = useState(1)
    const [moviesPerPage] = useState(15)
    const [ratings, setRatings] = useState(null)
    const [searchTerm, setSearchTerm] = useState('')

    const fetchFilmes = async () => {
        try {
            let response
            if (searchTerm === '') {
                response = await FilmesServices.getAll((currentPage - 1) * moviesPerPage, moviesPerPage)
            } else {
                response = await FilmesServices.getByTitle((currentPage - 1) * moviesPerPage, moviesPerPage, searchTerm)

            }
            setFilmes(response)
        } catch (error) {
            console.error('Error fetching filmes:', error)
        }
    }

    const fetchFilmesSearch = async () => {
        try {
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
    }, [currentPage, moviesPerPage, searchTerm])


    useEffect(() => {
        const fetch = async () => {
            await fetchFilmes()
        }
        fetch()
    }, [])

    const totalPages = Math.ceil(filmes.total / moviesPerPage)

<<<<<<< HEAD

    const onChangeNota = rating => {
        setRatings(rating)
    }
=======
 
  const onChangeNota = rating => {
    setRatings(rating)
  }
>>>>>>> c41aeeec06336971acad87eef6b8fc208507a25d

    return (<>
        <div className="h-screen min-h-screen">
            {/* Header */}


            {/* Recommendations Section */}
            <main className="container mx-auto px-4 py-8">
                <h2 className="text-2xl font-semibold mb-6 text-slate-400">Filmes</h2>
                <div className='flex justify-between mb-4'>
                    <Input type="text" placeholder="Digite o nome do filme..." className="w-1/2 text-black"
                        onChange={(e) => setSearchTerm(e.target.value)}
                        value={searchTerm}
                    />
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                    {filmes?.filmes?.map((movie, idx) => (
                        <CardFilmes key={idx} idFilme={movie?.MOVIEID || movie?.movieId}
                            onChangeNota={onChangeNota}

                        />
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