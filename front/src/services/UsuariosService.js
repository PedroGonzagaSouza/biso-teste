import API from './Api.js';

const CONTEXT = '/usuario';

class UsuarioService {

    // async postNovoUsuario(params) {

    //     try {
    //         const response = await API.post(`${CONTEXT}/create`, params);
    //         return response.data;
    //     } catch (error) {
    //         console.error('Erro ao cadastrar usuário:', error);
    //         throw error;
    //     }

    // }

    async login(credentials) {
        try {
            const response = await API.post(`${CONTEXT}/login`, credentials);
            const { access_token } = response.data;
            // Armazena o token no sessionStorage
            sessionStorage.setItem('access_token', access_token);
            // Armazena o token no localStorage 
            localStorage.setItem('access_token', access_token);

            return response.data;
        } catch (error) {
            console.error('Erro ao fazer login:', error);
            throw error.response?.data || error.message;
        }
    }

    async logout() {
        try {
            localStorage.removeItem('access_token');
            sessionStorage.removeItem('access_token');
        } catch (error) {
            console.error('Erro ao fazer logout:', error);
            throw error.message;

        }
    }

    // Método para obter o perfil do usuário logado
    async getProfile() {
        try {

            const token = localStorage.getItem('access_token') || sessionStorage.getItem('access_token');
            if (!token) throw new Error('Token não encontrado');

            const response = await API.get(`${CONTEXT}/me`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            return response.data;
        } catch (error) {
            console.error('Erro ao obter perfil:', error);
            throw error.response?.data || error.message;
        }
    }

    async postNovoUsuario(user) {
        try {
            const response = await API.post(`${CONTEXT}/create/hash`, user);
            return response.data;
        } catch (error) {
            console.error('Erro ao cadastrar usuário:', error);
            throw error.response?.data || error.message;
        }
    }
}

export default new UsuarioService()