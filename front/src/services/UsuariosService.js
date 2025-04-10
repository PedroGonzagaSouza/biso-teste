import API from './Api.js';

const CONTEXT = '/usuario';

class UsuarioService {

    postNovoUsuario = async (params) => {

        try {
            const response = await API.post(`${CONTEXT}/create`, params);
            return response.data;
        } catch (error) {
            console.error('Erro ao cadastrar usuário:', error);
            throw error;
        }

    }


}

export default new UsuarioService()