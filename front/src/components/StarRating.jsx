import React, { useState } from 'react';
import { Star } from 'lucide-react'; // Biblioteca de ícones (ou substitua por outro ícone)

export function StarRating({ rating, onRatingChange }) {
    const [hovered, setHovered] = useState(0);

    const handleMouseEnter = (index) => setHovered(index);
    const handleMouseLeave = () => setHovered(0);
    const handleClick = (index) => onRatingChange(index);

    return (
        <div className="flex items-center gap-1">
            {[1, 2, 3, 4, 5].map((index) => (
                <Star
                    key={index}
                    className={`w-6 h-6 cursor-pointer ${
                        index <= (hovered || rating) ? 'text-yellow-500' : 'text-gray-300'
                    }`}
                    onMouseEnter={() => handleMouseEnter(index)}
                    onMouseLeave={handleMouseLeave}
                    onClick={() => handleClick(index)}
                />
            ))}
        </div>
    );
}