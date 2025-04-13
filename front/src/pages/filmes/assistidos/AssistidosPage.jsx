import React, { useEffect, useState, useContext } from 'react';
import FilmesServices from '@/services/FilmesServices';
import RatingsServices from '@/services/RatingsServices';
import { AuthContext } from '@/AuthContext';
import { CardFilmes } from '../components/cardFilmes';

const movies = [
  {
    id: 1,
    title: 'Inception',
    genre: 'Sci-Fi',
    image: 'https://via.placeholder.com/150',
  },
  {
    id: 2,
    title: 'The Matrix',
    genre: 'Action',
    image: 'https://via.placeholder.com/150',
  },
  {
    id: 3,
    title: 'Interstellar',
    genre: 'Sci-Fi',
    image: 'https://via.placeholder.com/150',
  },
];

export function AssistidosPage() {
  const { user } = useContext(AuthContext);
  const [ratings, setRatings] = useState(0)

  const [filmesAssistidos, setFilmesAssistidos] = useState([]);


  const onChangeNota = rating => {
    setRatings(rating)
    console.log(rating, ',ssss')
  }

  useEffect(() => {

  }, [ratings]);
  useEffect(() => {
    const fetchFilmesAssistidos = async () => {
      try {
        const response = await RatingsServices.getAllByUserId(user.id);
        setFilmesAssistidos(response);
      } catch (error) {
        console.error('Error fetching assistidos:', error);
      }
    };

    fetchFilmesAssistidos();
  }, []);

  useEffect(() => {
    console.log('res', ratings)
    const fetchFilmesAssistidos = async () => {
      try {
        const response = await RatingsServices.getAllByUserId(user.id);
        setFilmesAssistidos(response); // Atualiza a lista de filmes assistidos
      } catch (error) {
        console.error('Error fetching assistidos:', error);
      }
    };

    if (ratings) {
      fetchFilmesAssistidos(); // Atualiza os filmes assistidos quando a nota muda
    }
  }, [ratings, user.id]); // Executa quando `ratings` ou `user.id` mudar
  return (
    <div className="min-h-screen">
      {/* Header */}


      {/* Recommendations Section */}
      <main className="container mx-auto px-4 py-8">
        <h2 className="text-2xl font-semibold mb-6 text-slate-400">Assistidos</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {filmesAssistidos.map((movie, idx) => (
            <CardFilmes key={idx} idFilme={movie.MOVIEID} nota={movie.RATING}
              onChangeNota={onChangeNota}

            />
          ))}
        </div>
      </main>

      {/* Footer */}

    </div>
  );
}