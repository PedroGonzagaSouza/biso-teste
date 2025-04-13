import API from './Api.js';


const CONTEXT = '/ratings';

class RatingsServices {

    async getAll() {
        try {
            const response = await API.get(`${CONTEXT}/all`);
            if (response.status === 200) {
                return response.data;
            }
        } catch (error) {
            console.error('Erro ao obter filmes:', error);
            throw error.response?.data || error.message;
        }
    }

    async getAllByUserId(userId) {
        try {
            const response = await API.get(`${CONTEXT}/user/${userId}`);
            if (response.status === 200) {
                return response.data;
            }
        } catch (error) {
            console.error('Erro ao obter filmes:', error);
            throw error.response?.data || error.message;
        }
    }

    async getRatingByUserIdAndMovieId(userId, movieId) {
            const response = await API.get(`${CONTEXT}/user/${userId}/filme/${movieId}`);
            return response.data;
        
    }

    async createRating(rating) {
        try {
            const response = await API.post(`${CONTEXT}/`, rating);
            if (response.status === 201) {
                return response.data;
            }
        } catch (error) {
            console.error('Erro ao criar filme:', error);
            throw error.response?.data || error.message;
        }
    }

    async updateRating(rating) {
        try {
            const response = await API.put(`${CONTEXT}/`, rating);
            if (response.status === 200) {
                return response.data;
            }
        } catch (error) {
            console.error('Erro ao atualizar filme:', error);
            throw error.response?.data || error.message;
        }
    }
    async deleteRating(ratingId) {
        try {
            const response = await API.delete(`${CONTEXT}/${ratingId}`);
            if (response.status === 200) {
                return response.data;
            }
        } catch (error) {
            console.error('Erro ao deletar filme:', error);
            throw error.response?.data || error.message;
        }
    }
}

export default new RatingsServices();