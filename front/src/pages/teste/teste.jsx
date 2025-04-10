import React from 'react';

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

export function RecommendationsPage() {
  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      

      {/* Recommendations Section */}
      <main className="container mx-auto px-4 py-8">
        <h2 className="text-2xl font-semibold mb-6">Recommended for You</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {movies.map((movie) => (
            <div
              key={movie.id}
              className="bg-white shadow-md rounded-lg overflow-hidden"
            >
              <img
                src={movie.image}
                alt={movie.title}
                className="w-full h-48 object-cover"
              />
              <div className="p-4">
                <h3 className="text-lg font-bold">{movie.title}</h3>
                <p className="text-gray-600">{movie.genre}</p>
                <button className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                  View Details
                </button>
              </div>
            </div>
          ))}
        </div>
      </main>

      {/* Footer */}
      
    </div>
  );
}