import React, { useEffect, useState, useContext } from 'react';
import FilmesServices from '@/services/FilmesServices';
import { AuthContext } from '@/AuthContext';
import { CardFilmes } from '../components/cardFilmes';
import { PaginationComponente } from '@/components/Pagination'


export function RecomendacoesPage() {
  const { user } = useContext(AuthContext);
  const [ratings, setRatings] = useState(0)
  const [currentPage, setCurrentPage] = useState(1)
  const [moviesPerPage] = useState(10)

  const [filmesAssistidos, setFilmesAssistidos] = useState([]);


  const onChangeNota = rating => {
    setRatings(rating)
  }

  useEffect(() => {

  }, [ratings]);

  useEffect(() => {
    const fetchFilmesAssistidos = async () => {
      try {
        const response = await FilmesServices.getRecomendacoes(user.id);
        setFilmesAssistidos(response);
      } catch (error) {
        console.error('Error fetching assistidos:', error);
      }
    };

    fetchFilmesAssistidos();
  }, []);

  useEffect(() => {
    const fetchFilmesAssistidos = async () => {
      try {
        const response = await FilmesServices.getRecomendacoes(user.id);
        setFilmesAssistidos(response); // Atualiza a lista de filmes assistidos
      } catch (error) {
        console.error('Error fetching assistidos:', error);
      }
    };

    if (ratings) {
      fetchFilmesAssistidos(); // Atualiza os filmes assistidos quando a nota muda
    }
  }, [ratings, user.id]);

  
  return (
    <div className="min-h-screen">
      {/* Recommendations Section */}
      <main className="container mx-auto px-4 py-8">
        <h2 className="text-2xl font-semibold mb-6 text-slate-400">Assistidos</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {filmesAssistidos.map((movie, idx) => (
            <CardFilmes key={idx} idFilme={movie?.MOVIEID || movie?.movieId} nota={movie.RATING} titulo={movie?.title}
              onChangeNota={onChangeNota}

            />
          ))}
        </div>
      </main>

      {/* Footer */}

    </div>
  );
}