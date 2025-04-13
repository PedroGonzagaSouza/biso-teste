import API from './Api.js';


const CONTEXT = '/filme';

class FilmesService {

    async getAll(offset, limit) {
        try {
            const response = await API.get(`${CONTEXT}/all/${offset}/${limit}`);
            if (response.status === 200) {
                return response.data;
            }
        } catch (error) {
            console.error('Erro ao obter filmes:', error);
            throw error.response?.data || error.message;
        }
    }

    async getById(id) {
        try {
            const response = await API.get(`${CONTEXT}/${id}`);
            if (response.status === 200) {
                return response.data;
            }
        } catch (error) {
            console.error('Erro ao obter filme:', error);
            throw error.response?.data || error.message;
        }
    }

    async getByTitle(offset, limit, title) {
        try {
            const response = await API.get(`${CONTEXT}/title/${title}/${offset}/${limit}`);
            if (response.status === 200) {
                return response.data;
            }
        } catch (error) {
            console.error('Erro ao obter filme por título:', error);
            throw error.response?.data || error.message;
        }
    }

    async getRecomendacoes(id_usuario) {
        try {
            const response = await API.get(`${CONTEXT}/${id_usuario}/recomendacoes`);
            if (response.status === 200) {
                return response.data;
            }
        } catch (error) {
            console.error('Erro ao obter recomendações:', error);
            throw error.response?.data || error.message;
        }
    }

}

export default new FilmesService();