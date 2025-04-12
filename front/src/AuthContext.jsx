import React, { createContext, useState, useEffect } from 'react';
import UsuariosService from './services/UsuariosService';
import { jwtDecode } from 'jwt-decode'; // Importa a função decode corretamente

export const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null); // Estado para armazenar o usuário logado
    const [loading, setLoading] = useState(true); // Estado para indicar carregamento

    // Função para login
    const login = async (credentials) => {
        try {
            const response = await UsuariosService.login(credentials);
            console.log('Resposta do login:', response);

            // Armazena o token no localStorage e sessionStorage
            localStorage.setItem('access_token', response.access_token);
            sessionStorage.setItem('access_token', response.access_token);

            const token = localStorage.getItem('access_token') || sessionStorage.getItem('access_token');
            console.log('Token armazenado:', token);
            if (token) {
                const decoded = jwtDecode(token);
                console.log('Token decodificado:', decoded);

                // Busca informações completas do usuário na API
                const userProfile = await UsuariosService.getProfile();
                console.log('Perfil do usuário:', userProfile);

                // Atualiza o estado do usuário
                setUser({ ...userProfile, login: decoded.sub });
            }
        } catch (error) {
            console.error('Erro ao fazer login:', error);
            throw error;
        }
    };

    // Função para carregar o usuário logado
    const loadUser = async () => {
        const token = localStorage.getItem('access_token') || sessionStorage.getItem('access_token');
        console.log('Token encontrado:', token);

        if (token) {
            try {
                // Decodifica o token JWT
                const decoded = jwtDecode(token);
                console.log('Token decodificado:', decoded);

                // Busca informações completas do usuário na API
                const userProfile = await UsuariosService.getProfile();
                console.log('Perfil do usuário:', userProfile);

                // Atualiza o estado do usuário
                setUser({ ...userProfile, login: decoded.sub });
            } catch (error) {
                console.error('Erro ao carregar o usuário:', error);
                logout(); // Remove o token em caso de erro
            }
        } else {
            console.log('Nenhum token encontrado.');
        }
        setLoading(false); // Finaliza o carregamento
    };

    // Função para logout
    const logout = () => {
        // Remove o token do armazenamento
        sessionStorage.removeItem('access_token');
        localStorage.removeItem('access_token');

        // Limpa o estado do usuário
        setUser(null);

        window.location.reload(); // Recarrega a página para atualizar o estado
    };

    // Carrega o usuário ao montar o componente
    useEffect(() => {
        const fetchUser = async () => {
            await loadUser();
        };

        fetchUser();
    }, []);

    return (
        <AuthContext.Provider value={{ user, login, logout, loading }}>
            {children}
        </AuthContext.Provider>
    );
}