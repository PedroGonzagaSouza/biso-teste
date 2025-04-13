import React from 'react';
import { Button } from './ui/button';
import {
    Pagination,
    PaginationContent,
    PaginationItem,
    PaginationLink,
    PaginationPrevious,
    PaginationNext,
} from '@/components/ui/pagination';

export function PaginationComponente({ totalPages, currentPage, onPageChange }) {
    // Calcula as páginas a serem exibidas
    const getVisiblePages = () => {
        const pages = [];
        for (let i = Math.max(1, currentPage - 2); i <= Math.min(totalPages, currentPage + 2); i++) {
            pages.push(i);
        }
        return pages;
    };

    const visiblePages = getVisiblePages();

    return (
        <Pagination>
            {/* Botão Anterior */}
            <Button>
                <PaginationPrevious
                    onClick={() => onPageChange(currentPage - 1)}
                    disabled={currentPage === 1}
                />
            </Button>

            {/* Páginas Visíveis */}
            <PaginationContent>
                {visiblePages.map((page) => (
                    <PaginationItem key={page}>
                        <PaginationLink
                            isActive={currentPage === page}
                            onClick={() => onPageChange(page)}
                        >
                            {page}
                        </PaginationLink>
                    </PaginationItem>
                ))}
            </PaginationContent>

            {/* Botão Próximo */}
            <Button>
                <PaginationNext
                    onClick={() => onPageChange(currentPage + 1)}
                    disabled={currentPage === totalPages}
                />
            </Button>
        </Pagination>
    );
}